import dataclasses
import typing

import pytest
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

from authmoderne.exceptions import InvalidRequestError
from authmoderne.factors.password import (
    InvalidCredentialsError,
    PasswordFactor,
    PasswordSubjectModel,
)
from authmoderne.identifier import IdentifierProtocol, InvalidIdentifierFormat
from tests.conftest import MockStorage


@dataclasses.dataclass
class MockPasswordSubject(PasswordSubjectModel):
    id: str
    username: str
    hashed_password: str | None


class MockIdentifier(IdentifierProtocol[MockPasswordSubject]):
    def __init__(self, storage: MockStorage[MockPasswordSubject]) -> None:
        self.storage = storage

    async def get_by_identifier(self, identifier: str) -> MockPasswordSubject:
        return await self.storage.get_one_by(username=identifier)

    async def parse_identifier(self, identifier: typing.Any) -> str:
        if not isinstance(identifier, str):
            raise InvalidIdentifierFormat()
        return identifier

    async def verify_identifier(self, identifier: str) -> str:
        return identifier


@pytest.fixture
def storage() -> MockStorage[MockPasswordSubject]:
    return MockStorage(MockPasswordSubject, [])


@pytest.fixture
def identifier(storage: MockStorage[MockPasswordSubject]) -> MockIdentifier:
    return MockIdentifier(storage)


@pytest.fixture
def password_factor(
    storage: MockStorage[MockPasswordSubject], identifier: MockIdentifier
) -> PasswordFactor[MockPasswordSubject]:
    return PasswordFactor(identifier, storage, PasswordHash.recommended())


@pytest.mark.anyio
class TestAuthenticate:
    @pytest.mark.parametrize(
        "payload",
        [
            {},
            {"identifier": "john"},
            {"password": "secret"},
        ],
    )
    async def test_invalid_request(
        self,
        payload: dict[str, typing.Any],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        with pytest.raises(InvalidRequestError):
            await password_factor.authenticate(payload)

    async def test_invalid_identifier(
        self, password_factor: PasswordFactor[MockPasswordSubject]
    ) -> None:
        with pytest.raises(InvalidRequestError):
            await password_factor.authenticate(
                {"identifier": 123, "password": "secret"}
            )

    async def test_not_existing_identifier(
        self, password_factor: PasswordFactor[MockPasswordSubject]
    ) -> None:
        with pytest.raises(InvalidCredentialsError):
            await password_factor.authenticate(
                {"identifier": "john", "password": "secret"}
            )

    async def test_not_set_hashed_password(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        await storage.create(id="1", username="john", hashed_password=None)

        with pytest.raises(InvalidCredentialsError):
            await password_factor.authenticate(
                {"identifier": "john", "password": "secret"}
            )

    async def test_invalid_password(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        hashed_password = password_factor.hasher.hash("password")
        await storage.create(id="1", username="john", hashed_password=hashed_password)

        with pytest.raises(InvalidCredentialsError):
            await password_factor.authenticate(
                {"identifier": "john", "password": "wrong_password"}
            )

    async def test_valid(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        hashed_password = password_factor.hasher.hash("password")
        await storage.create(id="1", username="john", hashed_password=hashed_password)

        subject = await password_factor.authenticate(
            {"identifier": "john", "password": "password"}
        )

        assert subject.id == "1"
        assert subject.hashed_password == hashed_password

    async def test_valid_hash_upgrade(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        hashed_password = Argon2Hasher(time_cost=1).hash("password")
        await storage.create(id="1", username="john", hashed_password=hashed_password)

        subject = await password_factor.authenticate(
            {"identifier": "john", "password": "password"}
        )

        assert subject.id == "1"
        assert subject.hashed_password != hashed_password


@pytest.mark.anyio
class TestEnroll:
    async def test_invalid_request(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        subject = await storage.create(id="1", username="john", hashed_password=None)
        with pytest.raises(InvalidRequestError):
            await password_factor.enroll(subject, {})

    async def test_valid(
        self,
        storage: MockStorage[MockPasswordSubject],
        password_factor: PasswordFactor[MockPasswordSubject],
    ) -> None:
        subject = await storage.create(id="1", username="john", hashed_password=None)

        updated_subject = await password_factor.enroll(
            subject, {"password": "password"}
        )

        assert updated_subject.id == "1"
        assert updated_subject.hashed_password is not None
