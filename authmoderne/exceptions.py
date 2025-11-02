"""Base exceptions for the authmoderne package."""


class AuthmoderneException(Exception):
    """Base exception for all authmoderne exceptions."""

    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
