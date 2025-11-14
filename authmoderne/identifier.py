import typing

import dishka
import email_validator

from .exceptions import AuthmoderneException
from .storage import StorageProtocol
from .subject import Subject


class IdentifierError(AuthmoderneException): ...


class InvalidIdentifierFormat(IdentifierError):
    """Raised when identifier doesn't match expected type/structure."""

    def __init__(
        self, message: str = "The provided identifier format is invalid."
    ) -> None:
        super().__init__(message)


class IdentifierVerificationError(IdentifierError):
    """Raised when identifier fails business logic validation."""

    def __init__(self, message: str = "The identifier verification failed.") -> None:
        super().__init__(message)


class IdentifierProtocol[S: Subject](typing.Protocol):
    async def get_by_identifier(self, identifier: typing.Any) -> S: ...

    async def parse_identifier(self, identifier: typing.Any) -> typing.Any: ...

    async def verify_identifier(self, identifier: typing.Any) -> typing.Any: ...


class IdentifierProvider[S: Subject](dishka.Provider):
    """Base class for identifier providers."""


class EmailSubjectModel(Subject):
    email: str


class EmailIdentifier[S: EmailSubjectModel](IdentifierProtocol[S]):
    def __init__(self, email_storage: StorageProtocol[S]) -> None:
        self.email_storage = email_storage

    async def get_by_identifier(self, identifier: str) -> S:
        return await self.email_storage.get_one_by(email=identifier)

    async def parse_identifier(self, identifier: typing.Any) -> str:
        if not isinstance(identifier, str):
            raise InvalidIdentifierFormat()
        return identifier

    async def verify_identifier(self, identifier: str) -> str:
        try:
            validated_email = email_validator.validate_email(identifier)
        except email_validator.EmailNotValidError as e:
            raise IdentifierVerificationError(str(e)) from e
        else:
            return validated_email.normalized


class EmailIdentifierProvider[S: EmailSubjectModel](IdentifierProvider[S]):
    @dishka.provide(scope=dishka.Scope.REQUEST)
    def identifier[_S: EmailSubjectModel](
        self, subject: type[_S], email_storage: StorageProtocol[_S]
    ) -> IdentifierProtocol[_S]:
        return EmailIdentifier[_S](email_storage)
