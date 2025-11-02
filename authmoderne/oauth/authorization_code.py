import typing

from pydantic import AnyUrl, BaseModel, Field, HttpUrl, ValidationError

from ..exceptions import AuthmoderneException
from ..storage import DoesNotExist, StorageProtocol
from .models import OAuthClientProtocol


class OAuthClientError(AuthmoderneException):
    """Base exception for all OAuth client-related errors."""


class AuthorizationCodeGrantRequest(BaseModel):
    response_type: str
    client_id: str
    redirect_uri: AnyUrl | None = None
    scope: str | None = None
    state: str | None = None
    code_challenge: typing.Annotated[str, Field(pattern=r"^[A-Za-z0-9\-\._~]{43,128}$")]
    code_challenge_method: typing.Literal["plain", "S256"] = "plain"


class AuthorizationCodeGrantConsentResponse:
    client: OAuthClientProtocol
    scope: str | None
    redirect_uri: str | None
    state: str | None
    code_challenge: str
    code_challenge_method: typing.Literal["plain", "S256"]

    def __init__(
        self,
        *,
        client: OAuthClientProtocol,
        scope: str | None,
        redirect_uri: str | None,
        state: str | None,
        code_challenge: str,
        code_challenge_method: typing.Literal["plain", "S256"],
    ) -> None:
        self.client = client
        self.scope = scope
        self.redirect_uri = redirect_uri
        self.state = state
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method


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


class AuthorizationCodeGrant:
    def __init__(
        self, storage: StorageProtocol, oauth_client_model: type[OAuthClientProtocol]
    ) -> None:
        self.storage = storage
        self.oauth_client_model = oauth_client_model

    async def validate_request(
        self, payload: dict[str, typing.Any]
    ) -> AuthorizationCodeGrantConsentResponse:
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
            client = await self.storage.get_by_id(
                model=self.oauth_client_model, id=request.client_id
            )
        except DoesNotExist as e:
            raise MissingOrInvalidClientIDError() from e

        return AuthorizationCodeGrantConsentResponse(
            client=client,
            scope=request.scope,
            redirect_uri=str(request.redirect_uri),
            state=request.state,
            code_challenge=request.code_challenge,
            code_challenge_method=request.code_challenge_method,
        )
