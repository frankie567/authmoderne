import typing
from datetime import UTC, datetime, timedelta

import dishka
from pydantic import AnyUrl, BaseModel, Field, HttpUrl, ValidationError

from authmoderne.crypto import generate_token_hash_pair
from authmoderne.oauth.models import OAuthAuthorizationCodeModel
from authmoderne.subject import Subject

from ..exceptions import AuthmoderneException
from ..storage import DoesNotExist, StorageProtocol
from .models import OAuthClientModel, OAuthGrantModel
from .types import CodeChallengeMethod


class OAuthClientError(AuthmoderneException):
    """Base exception for all OAuth client-related errors."""


AuthorizationCodeGrantErrorCode = typing.Literal[
    "invalid_request",
    "unauthorized_client",
    "access_denied",
    "unsupported_response_type",
    "invalid_scope",
    "server_error",
    "temporarily_unavailable",
]


class AuthorizationCodeGrantError(OAuthClientError):
    """Base exception for all Authorization Code Grant errors."""


class UnauthenticatedSubjectError(AuthorizationCodeGrantError):
    """Error raised when the subject is not authenticated."""

    def __init__(self) -> None:
        message = "The subject is not authenticated."
        super().__init__(message)


class MissingOrInvalidClientIDError(AuthorizationCodeGrantError):
    """Error raised when the client_id is missing or invalid in the request."""

    def __init__(self) -> None:
        message = "The 'client_id' parameter is missing or invalid."
        super().__init__(message)


class AuthorizationCodeGrantRedirectionError(AuthorizationCodeGrantError):
    """Error that's meant to be redirected to the client application."""

    error: AuthorizationCodeGrantErrorCode
    error_description: str | None = None
    error_uri: HttpUrl | None = None

    def __init__(
        self,
        error: AuthorizationCodeGrantErrorCode,
        error_description: str | None = None,
        error_uri: HttpUrl | None = None,
    ):
        self.error = error
        self.error_description = error_description
        self.error_uri = error_uri
        super().__init__(error)


class AuthorizationCodeGrantRequest(BaseModel):
    response_type: str
    client_id: str
    redirect_uri: AnyUrl | None = None
    scope: str | None = None
    state: str | None = None
    code_challenge: typing.Annotated[str, Field(pattern=r"^[A-Za-z0-9\-\._~]{43,128}$")]
    code_challenge_method: CodeChallengeMethod = "plain"


class AuthorizationCodeGrantConsentResponse[S: Subject]:
    subject: S
    client: OAuthClientModel
    scope: str | None
    redirect_uri: str | None
    state: str | None
    code_challenge: str
    code_challenge_method: CodeChallengeMethod

    def __init__(
        self,
        *,
        client: OAuthClientModel,
        scope: str | None,
        redirect_uri: str | None,
        state: str | None,
        code_challenge: str,
        code_challenge_method: CodeChallengeMethod,
    ) -> None:
        self.client = client
        self.scope = scope
        self.redirect_uri = redirect_uri
        self.state = state
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method


class AuthorizationCodeGrantGrantedResponse[S: Subject]:
    subject: S
    client: OAuthClientModel
    code: str
    authorization_code: OAuthAuthorizationCodeModel

    def __init__(
        self,
        *,
        subject: S,
        client: OAuthClientModel,
        code: str,
        authorization_code: OAuthAuthorizationCodeModel,
    ) -> None:
        self.subject = subject
        self.client = client
        self.code = code
        self.authorization_code = authorization_code


_DEFAULT_CODE_PREFIX = "am_code_"


class AuthorizationCodeGrant[
    OC: OAuthClientModel,
    OG: OAuthGrantModel,
    OAC: OAuthAuthorizationCodeModel,
]:
    def __init__(
        self,
        oauth_client_storage: StorageProtocol[OC],
        oauth_grant_storage: StorageProtocol[OG],
        oauth_authorization_code_storage: StorageProtocol[OAC],
        code_hash_key: str,
        code_prefix: str = _DEFAULT_CODE_PREFIX,
    ) -> None:
        self.oauth_client_storage = oauth_client_storage
        self.oauth_grant_storage = oauth_grant_storage
        self.oauth_authorization_code_storage = oauth_authorization_code_storage
        self.code_hash_key = code_hash_key
        self.code_prefix = code_prefix

    async def __call__[S: Subject](
        self, subject: S | None, payload: dict[str, typing.Any]
    ) -> (
        AuthorizationCodeGrantConsentResponse[S]
        | AuthorizationCodeGrantGrantedResponse[S]
    ):
        if subject is None:
            raise UnauthenticatedSubjectError()

        try:
            request = AuthorizationCodeGrantRequest.model_validate(payload)
        except ValidationError as e:
            errors = e.errors()
            client_id_error = next(
                (err for err in errors if err["loc"] == ("client_id",)), None
            )
            if client_id_error and client_id_error["type"] == "missing":
                raise MissingOrInvalidClientIDError() from e
            raise AuthorizationCodeGrantRedirectionError(error="invalid_request") from e

        try:
            client = await self.oauth_client_storage.get_one_by(
                client_id=request.client_id
            )
        except DoesNotExist as e:
            raise MissingOrInvalidClientIDError() from e

        try:
            _ = await self.oauth_grant_storage.get_one_by(
                client_id=client.client_id, subject_id=subject.id
            )
        except DoesNotExist:
            return AuthorizationCodeGrantConsentResponse(
                client=client,
                scope=request.scope,
                redirect_uri=str(request.redirect_uri),
                state=request.state,
                code_challenge=request.code_challenge,
                code_challenge_method=request.code_challenge_method,
            )
        else:
            code, code_hash = generate_token_hash_pair(
                self.code_hash_key, prefix=self.code_prefix
            )
            authorization_code = await self.oauth_authorization_code_storage.create(
                code=code_hash,
                client_id=client.client_id,
                subject_id=subject.id,
                expires_at=datetime.now(UTC) + timedelta(minutes=10),
                response_type=request.response_type,
                redirect_uri=str(request.redirect_uri),
                scope=request.scope,
                code_challenge=request.code_challenge,
                code_challenge_method=request.code_challenge_method,
            )
            return AuthorizationCodeGrantGrantedResponse(
                subject=subject,
                client=client,
                code=code,
                authorization_code=authorization_code,
            )


class AuthorizationCodeGrantProvider(dishka.Provider):
    def __init__(
        self, code_hash_key: str, code_prefix: str = _DEFAULT_CODE_PREFIX
    ) -> None:
        super().__init__()
        self.code_hash_key = code_hash_key
        self.code_prefix = code_prefix

    @dishka.provide(scope=dishka.Scope.REQUEST)
    def get_authorization_code_grant[
        OC: OAuthClientModel,
        OG: OAuthGrantModel,
        OAC: OAuthAuthorizationCodeModel,
    ](
        self,
        oauth_client_storage: StorageProtocol[OC],
        oauth_grant_storage: StorageProtocol[OG],
        oauth_authorization_code_storage: StorageProtocol[OAC],
    ) -> AuthorizationCodeGrant[OC, OG, OAC]:
        return AuthorizationCodeGrant(
            oauth_client_storage=oauth_client_storage,
            oauth_grant_storage=oauth_grant_storage,
            oauth_authorization_code_storage=oauth_authorization_code_storage,
            code_hash_key=self.code_hash_key,
            code_prefix=self.code_prefix,
        )
