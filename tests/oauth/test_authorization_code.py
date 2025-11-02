import dataclasses
import typing

import pytest

from authmoderne.oauth.authorization_code import (
    AuthorizationCodeGrant,
    AuthorizationCodeGrantRedirectionError,
    MissingOrInvalidClientIDError,
)
from authmoderne.oauth.models import OAuthClientProtocol
from tests.conftest import MockStorage


@dataclasses.dataclass
class MockOAuthClient(OAuthClientProtocol):
    client_id: str


@pytest.fixture
def authorization_code_grant(mock_storage: MockStorage) -> AuthorizationCodeGrant:
    return AuthorizationCodeGrant(
        storage=mock_storage, oauth_client_model=MockOAuthClient
    )


@pytest.mark.anyio
class TestAuthorizationCodeGrantValidateRequest:
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
        payload: dict[str, typing.Any],
        authorization_code_grant: AuthorizationCodeGrant,
    ) -> None:
        with pytest.raises(AuthorizationCodeGrantRedirectionError) as exc_info:
            await authorization_code_grant.validate_request(payload)

        assert exc_info.value.error == "invalid_request"

    async def test_missing_client_id(
        self, authorization_code_grant: AuthorizationCodeGrant
    ) -> None:
        payload = {"response_type": "code"}

        with pytest.raises(MissingOrInvalidClientIDError):
            await authorization_code_grant.validate_request(payload)
