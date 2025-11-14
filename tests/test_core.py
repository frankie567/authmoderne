import dataclasses

import pytest

from authmoderne.core import Authmoderne, SubjectConfiguration
from authmoderne.identifier import (
    EmailIdentifierProvider,
    EmailSubjectModel,
)
from authmoderne.oauth.authorization_code import (
    AuthorizationCodeGrant,
    AuthorizationCodeGrantProvider,
)
from authmoderne.oauth.models.sqlalchemy import (
    OAuthAuthorizationCode,
    OAuthClient,
    OAuthGrant,
)
from authmoderne.storage.sqlalchemy import SQLAlchemyEngineProvider
from tests.conftest import MockModel, MockStorage, MockStorageProvider


@pytest.mark.anyio
class TestAuthmoderneGetStorage:
    async def test_single_storage(self) -> None:
        authmoderne = Authmoderne(MockStorageProvider({}))
        async with authmoderne() as authmoderne_request:
            storage = await authmoderne_request.get_storage(MockModel)
            assert isinstance(storage, MockStorage)

    async def test_multiple_storages(self) -> None:
        class FirstMockStorage[Model](MockStorage[Model]):
            pass

        @dataclasses.dataclass
        class FirstMockModel: ...

        class SecondMockStorage[Model](MockStorage[Model]):
            pass

        @dataclasses.dataclass
        class SecondMockModel: ...

        authmoderne = Authmoderne(
            (
                MockStorageProvider(
                    {}, models=[FirstMockModel], storage_class=FirstMockStorage
                ),
                MockStorageProvider(
                    {}, models=[SecondMockModel], storage_class=SecondMockStorage
                ),
            )
        )
        async with authmoderne() as authmoderne_request:
            first_storage = await authmoderne_request.get_storage(FirstMockModel)
            assert isinstance(first_storage, FirstMockStorage)

            second_storage = await authmoderne_request.get_storage(SecondMockModel)

            assert isinstance(second_storage, SecondMockStorage)


@pytest.mark.anyio
async def test_subject_configuration() -> None:
    @dataclasses.dataclass
    class MockSubject(EmailSubjectModel):
        id: str
        email: str

    authmoderne = Authmoderne(
        MockStorageProvider(
            {
                MockSubject: [
                    MockSubject(id="1", email="john@example.com"),
                ]
            }
        ),
        subject_configuration=SubjectConfiguration(EmailIdentifierProvider()),
    )

    async with authmoderne() as authmoderne_request:
        identifier = await authmoderne_request.get_identifier(MockSubject)
        subject = await identifier.get_by_identifier("john@example.com")
        assert subject.id == "1"


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_authorization_code_provider(anyio_backend: str) -> None:
    authmoderne = Authmoderne(
        SQLAlchemyEngineProvider("sqlite+aiosqlite:///:memory:"),
        plugins=[AuthorizationCodeGrantProvider("SECRET_KEY")],
    )
    async with authmoderne() as authmoderne_request:
        authorization_code_grant = await authmoderne_request.get(
            AuthorizationCodeGrant[OAuthClient, OAuthGrant, OAuthAuthorizationCode]
        )
        assert isinstance(authorization_code_grant, AuthorizationCodeGrant)
        assert authorization_code_grant.oauth_client_storage.model is OAuthClient
