import typing

import email_validator

from .exceptions import AuthmoderneException
from .models import model_protocol
from .storage import StorageProtocol
from .subject import Subject


class IdentifierError(AuthmoderneException): ...


class InvalidIdentifier(IdentifierError):
    def __init__(self, message: str = "The provided identifier is invalid.") -> None:
        super().__init__(message)


class IdentifierProtocol[S: Subject, Identifier](typing.Protocol):
    async def get_by_identifier(self, identifier: Identifier) -> S: ...

    async def validate_identifier(self, identifier: Identifier) -> Identifier: ...


@model_protocol
class EmailSubjectProtocol(Subject, typing.Protocol):
    @property
    def email(self) -> str: ...

    @email.setter
    def email(self, value: str) -> None: ...


class EmailIdentifier[S: EmailSubjectProtocol](IdentifierProtocol[S, str]):
    def __init__(self, email_storage: StorageProtocol[S]) -> None:
        self.email_storage = email_storage

    async def get_by_identifier(self, identifier: str) -> S:
        return await self.email_storage.get_one_by(email=identifier)

    async def validate_identifier(self, identifier: str) -> str:
        try:
            validated_email = email_validator.validate_email(identifier)
        except email_validator.EmailNotValidError as e:
            raise InvalidIdentifier(str(e)) from e
        else:
            return validated_email.normalized
