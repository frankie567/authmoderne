"""Base exceptions for the authmoderne package."""

import typing

from pydantic import ValidationError
from pydantic_core import ErrorDetails


class AuthmoderneException(Exception):
    """Base exception for all authmoderne exceptions."""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class InvalidRequestError(AuthmoderneException):
    """Exception raised for invalid requests."""

    def __init__(self, errors: list[ErrorDetails]):
        message = "Invalid request"
        self.errors = errors
        super().__init__(message)

    @classmethod
    def from_validation_error(cls, error: ValidationError) -> typing.Self:
        return cls(errors=error.errors())


__all__ = ["AuthmoderneException", "InvalidRequestError"]
