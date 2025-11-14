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
def mock_data_store() -> dict[typing.Any, list[typing.Any]]:
    return {
        MockUser: [],
        MockOAuthClient: [],
        MockOAuthGrant: [],
        MockOAuthAuthorizationCode: [],
    }


@pytest.fixture
async def oauth_client(
    mock_data_store: dict[typing.Any, list[typing.Any]],
) -> MockOAuthClient:
    oauth_client = MockOAuthClient(client_id="CLIENT_ID")
    mock_data_store[MockOAuthClient].append(oauth_client)
    return oauth_client


@pytest.fixture
async def oauth_grant(
    mock_data_store: dict[typing.Any, list[typing.Any]],
    subject: MockUser,
    oauth_client: MockOAuthClient,
) -> MockOAuthGrant:
    oauth_grant = MockOAuthGrant(
        client_id=oauth_client.client_id,
        subject_id=subject.id,
        granted_at=datetime.now(UTC),
        scope="read write",
    )
    mock_data_store[MockOAuthGrant].append(oauth_grant)
    return oauth_grant


@pytest.fixture
def authorization_code_grant(
    mock_data_store: dict[typing.Any, list[typing.Any]],
) -> AuthorizationCodeGrant[
    MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
]:
    return AuthorizationCodeGrant(
        oauth_client_storage=MockStorage(
            MockOAuthClient, mock_data_store[MockOAuthClient]
        ),
        oauth_grant_storage=MockStorage(
            MockOAuthGrant, mock_data_store[MockOAuthGrant]
        ),
        oauth_authorization_code_storage=MockStorage(
            MockOAuthAuthorizationCode, mock_data_store[MockOAuthAuthorizationCode]
        ),
        code_hash_key="SECRET",
    )


@pytest.mark.anyio
class TestAuthorizationCodeGrantValidateRequest:
    async def test_missing_subject(
        self,
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
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
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
    ) -> None:
        with pytest.raises(AuthorizationCodeGrantRedirectionError) as exc_info:
            await authorization_code_grant(subject, payload)

        assert exc_info.value.error == "invalid_request"

    async def test_missing_client_id(
        self,
        subject: MockUser,
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
    ) -> None:
        payload = {"response_type": "code"}

        with pytest.raises(MissingOrInvalidClientIDError):
            await authorization_code_grant(subject, payload)

    async def test_invalid_client(
        self,
        subject: MockUser,
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
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
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
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
        authorization_code_grant: AuthorizationCodeGrant[
            MockOAuthClient, MockOAuthGrant, MockOAuthAuthorizationCode
        ],
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
