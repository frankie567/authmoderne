import typing

from pydantic import BaseModel, ValidationError

from authmoderne.exceptions import AuthmoderneException, InvalidRequestError
from authmoderne.identifier import IdentifierProtocol, InvalidIdentifierFormat
from authmoderne.storage import DoesNotExist, StorageProtocol
from authmoderne.subject import Subject


class PasswordFactorError(AuthmoderneException):
    """Base exception for password factor errors."""


class InvalidCredentialsError(PasswordFactorError):
    """Raised when the provided credentials are invalid."""

    def __init__(self) -> None:
        super().__init__("Invalid credentials provided.")


class PasswordHasherProtocol(typing.Protocol):
    def verify_and_update(
        self, password: str | bytes, hash: str | bytes
    ) -> tuple[bool, str | None]: ...  # pragma: no cover

    def hash(
        self,
        password: str | bytes,
        *,
        salt: bytes | None = None,
    ) -> str: ...  # pragma: no cover


class PasswordSubjectModel(Subject):
    hashed_password: str | None


class PasswordAuthenticateRequest(BaseModel):
    identifier: typing.Any
    password: str


class PasswordEnrollRequest(BaseModel):
    password: str


class PasswordFactor[S: PasswordSubjectModel]:
    def __init__(
        self,
        identifier: IdentifierProtocol[S],
        subject_storage: StorageProtocol[S],
        hasher: PasswordHasherProtocol,
    ) -> None:
        self.identifier = identifier
        self.subject_storage = subject_storage
        self.hasher = hasher

    async def authenticate(self, payload: dict[str, typing.Any]) -> S:
        try:
            request = PasswordAuthenticateRequest.model_validate(payload)
        except ValidationError as e:
            raise InvalidRequestError.from_validation_error(e) from e

        try:
            identifier = await self.identifier.parse_identifier(request.identifier)
        except InvalidIdentifierFormat as e:
            raise InvalidRequestError(
                [
                    {
                        "type": "value_error",
                        "loc": ("identifier",),
                        "msg": e.message,
                        "input": request.identifier,
                    }
                ]
            )

        try:
            subject = await self.identifier.get_by_identifier(identifier)
        except DoesNotExist:
            self._raise_invalid_credentials_timing_safe(request.password)

        if subject.hashed_password is None:
            self._raise_invalid_credentials_timing_safe(request.password)

        # Verify the password
        is_valid, updated_hash = self.hasher.verify_and_update(
            request.password, subject.hashed_password
        )

        if not is_valid:
            raise InvalidCredentialsError()

        # Update the password hash if needed
        if updated_hash is not None:
            subject = await self.subject_storage.update(
                subject, hashed_password=updated_hash
            )

        return subject

    async def enroll(self, subject: S, payload: dict[str, typing.Any]) -> S:
        try:
            request = PasswordEnrollRequest.model_validate(payload)
        except ValidationError as e:
            raise InvalidRequestError.from_validation_error(e) from e

        hashed_password = self.hasher.hash(request.password)

        subject = await self.subject_storage.update(
            subject, hashed_password=hashed_password
        )

        return subject

    def _raise_invalid_credentials_timing_safe(self, password: str) -> typing.Never:
        """
        Raise InvalidCredentialsError while running the hasher to mitigate timing attacks.

        Inspired from Django: https://code.djangoproject.com/ticket/20760
        """
        self.hasher.hash(password)
        raise InvalidCredentialsError()
