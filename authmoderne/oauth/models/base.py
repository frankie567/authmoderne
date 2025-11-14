import typing
from datetime import datetime

from authmoderne.models import model_protocol

from ..types import CodeChallengeMethod


@model_protocol
class OAuthClientProtocol(typing.Protocol):
    """Protocol for OAuth client implementations."""

    @property
    def client_id(self) -> str: ...

    @client_id.setter
    def client_id(self, value: str) -> None: ...


@model_protocol
class OAuthGrantProtocol(typing.Protocol):
    """Protocol for OAuth grant implementations."""

    @property
    def client_id(self) -> str: ...

    @client_id.setter
    def client_id(self, value: str) -> None: ...

    @property
    def subject_id(self) -> typing.Any: ...

    @subject_id.setter
    def subject_id(self, value: typing.Any) -> None: ...

    @property
    def granted_at(self) -> datetime: ...

    @granted_at.setter
    def granted_at(self, value: datetime) -> None: ...

    @property
    def scope(self) -> str: ...

    @scope.setter
    def scope(self, value: str) -> None: ...


@model_protocol
class OAuthAuthorizationCodeProtocol(typing.Protocol):
    """Protocol for OAuth authorization code implementations."""

    @property
    def code(self) -> str: ...

    @code.setter
    def code(self, value: str) -> None: ...

    @property
    def client_id(self) -> str: ...

    @client_id.setter
    def client_id(self, value: str) -> None: ...

    @property
    def subject_id(self) -> typing.Any: ...

    @subject_id.setter
    def subject_id(self, value: typing.Any) -> None: ...

    @property
    def expires_at(self) -> datetime: ...

    @expires_at.setter
    def expires_at(self, value: datetime) -> None: ...

    @property
    def response_type(self) -> str: ...

    @response_type.setter
    def response_type(self, value: str) -> None: ...

    @property
    def redirect_uri(self) -> str | None: ...

    @redirect_uri.setter
    def redirect_uri(self, value: str | None) -> None: ...

    @property
    def scope(self) -> str: ...

    @scope.setter
    def scope(self, value: str) -> None: ...

    @property
    def code_challenge(self) -> str: ...

    @code_challenge.setter
    def code_challenge(self, value: str) -> None: ...

    @property
    def code_challenge_method(self) -> CodeChallengeMethod: ...

    @code_challenge_method.setter
    def code_challenge_method(self, value: CodeChallengeMethod) -> None: ...


__all__ = [
    "OAuthClientProtocol",
    "OAuthGrantProtocol",
    "OAuthAuthorizationCodeProtocol",
]
