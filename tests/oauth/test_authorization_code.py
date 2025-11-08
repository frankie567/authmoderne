import dataclasses
import typing
from datetime import UTC, datetime

import pytest

from authmoderne.crypto import get_token_hash
from authmoderne.oauth.authorization_code import (
    AuthorizationCodeGrant,
    AuthorizationCodeGrantConsentResponse,
    AuthorizationCodeGrantGrantedResponse,
    AuthorizationCodeGrantRedirectionError,
    MissingOrInvalidClientIDError,
    UnauthenticatedSubjectError,
)
from authmoderne.oauth.types import CodeChallengeMethod
from authmoderne.subject import Subject
from tests.conftest import MockStorage


@dataclasses.dataclass
class MockUser(Subject):
    id: str


@dataclasses.dataclass
class MockOAuthClient:
    client_id: str

    @property
    def id(self) -> str:
        return self.client_id


@dataclasses.dataclass
class MockOAuthGrant:
    client_id: str
    subject_id: str
    granted_at: datetime
    scope: str

    @property
    def id(self) -> str:
        return f"{self.client_id}:{self.subject_id}"


@dataclasses.dataclass
class MockOAuthAuthorizationCode:
    code: str
    client_id: str
    subject_id: str
    expires_at: datetime
    response_type: str
    redirect_uri: str | None
    scope: str
    code_challenge: str
    code_challenge_method: CodeChallengeMethod

    @property
    def id(self) -> str:
        return self.code


@pytest.fixture
def subject() -> MockUser:
    return MockUser(id="user_123")


@pytest.fixture
async def oauth_client(mock_storage: MockStorage) -> MockOAuthClient:
    return await mock_storage.create(MockOAuthClient, client_id="CLIENT_ID")


@pytest.fixture
async def oauth_grant(
    mock_storage: MockStorage, subject: MockUser, oauth_client: MockOAuthClient
) -> MockOAuthGrant:
    return await mock_storage.create(
        MockOAuthGrant,
        client_id=oauth_client.client_id,
        subject_id=subject.id,
        granted_at=datetime.now(UTC),
        scope="read write",
    )


@pytest.fixture
def authorization_code_grant(mock_storage: MockStorage) -> AuthorizationCodeGrant:
    return AuthorizationCodeGrant(
        storage=mock_storage,
        oauth_client_model=MockOAuthClient,
        oauth_grant_model=MockOAuthGrant,
        oauth_authorization_code_model=MockOAuthAuthorizationCode,
        code_hash_key="SECRET",
    )


@pytest.mark.anyio
class TestAuthorizationCodeGrantValidateRequest:
    async def test_missing_subject(
        self, authorization_code_grant: AuthorizationCodeGrant
    ) -> None:
        payload = {"response_type": "code"}

        with pytest.raises(UnauthenticatedSubjectError):
            await authorization_code_grant(None, payload)

    @pytest.mark.parametrize(
        "payload",
        [
            pytest.param(
                {"response_type": "code", "client_id": "CLIENT_ID"},
                id="missing code_challenge",
            ),
            pytest.param(
                {
                    "response_type": "code",
                    "client_id": "CLIENT_ID",
                    "code_challenge": "A" * 43,
                    "code_challenge_method": "INVALID",
                },
                id="invalid code_challenge_method",
            ),
            pytest.param(
                {
                    "response_type": "code",
                    "client_id": "CLIENT_ID",
                    "code_challenge": "A" * 512,
                    "code_challenge_method": "plain",
                },
                id="invalid code_challenge",
            ),
        ],
    )
    async def test_invalid_request(
        self,
        subject: MockUser,
        payload: dict[str, typing.Any],
        authorization_code_grant: AuthorizationCodeGrant,
    ) -> None:
        with pytest.raises(AuthorizationCodeGrantRedirectionError) as exc_info:
            await authorization_code_grant(subject, payload)

        assert exc_info.value.error == "invalid_request"

    async def test_missing_client_id(
        self, subject: MockUser, authorization_code_grant: AuthorizationCodeGrant
    ) -> None:
        payload = {"response_type": "code"}

        with pytest.raises(MissingOrInvalidClientIDError):
            await authorization_code_grant(subject, payload)

    async def test_invalid_client(
        self, subject: MockUser, authorization_code_grant: AuthorizationCodeGrant
    ) -> None:
        payload = {
            "response_type": "code",
            "client_id": "INVALID_CLIENT_ID",
            "code_challenge": "A" * 43,
            "code_challenge_method": "plain",
        }

        with pytest.raises(MissingOrInvalidClientIDError):
            await authorization_code_grant(subject, payload)

    async def test_not_granted(
        self,
        subject: MockUser,
        oauth_client: MockOAuthClient,
        authorization_code_grant: AuthorizationCodeGrant,
    ) -> None:
        payload = {
            "response_type": "code",
            "client_id": oauth_client.client_id,
            "code_challenge": "A" * 43,
            "code_challenge_method": "plain",
        }

        response = await authorization_code_grant(subject, payload)

        assert isinstance(response, AuthorizationCodeGrantConsentResponse)
        assert response.client == oauth_client

    async def test_granted(
        self,
        subject: MockUser,
        oauth_client: MockOAuthClient,
        oauth_grant: MockOAuthGrant,
        authorization_code_grant: AuthorizationCodeGrant,
    ) -> None:
        payload = {
            "response_type": "code",
            "client_id": oauth_client.client_id,
            "code_challenge": "A" * 43,
            "code_challenge_method": "plain",
        }

        response = await authorization_code_grant(subject, payload)

        assert isinstance(response, AuthorizationCodeGrantGrantedResponse)
        assert response.client == oauth_client
        assert response.code.startswith(authorization_code_grant.code_prefix)
        assert response.authorization_code.client_id == oauth_client.client_id
        assert response.authorization_code.subject_id == subject.id
        assert response.authorization_code.code == get_token_hash(
            response.code, authorization_code_grant.code_hash_key
        )
