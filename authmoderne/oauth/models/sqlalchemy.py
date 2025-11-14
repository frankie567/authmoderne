import typing
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...storage.sqlalchemy import Base
from ..types import CodeChallengeMethod
from .base import (
    OAuthAuthorizationCodeModel,
    OAuthClientModel,
    OAuthGrantModel,
)


class OAuthClient(OAuthClientModel, Base):
    __tablename__ = "oauth_clients"

    _client_id: Mapped[str] = mapped_column(
        "client_id", String(128), primary_key=True, unique=True, nullable=False
    )

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self._client_id = value


class OAuthGrant(OAuthGrantModel, Base):
    __tablename__ = "oauth_grants"

    _client_id: Mapped[str] = mapped_column(
        "client_id",
        ForeignKey("oauth_clients.client_id"),
        nullable=False,
        primary_key=True,
    )
    _subject_id: Mapped[typing.Any] = mapped_column(
        "subject_id", String(128), nullable=False, primary_key=True
    )
    _granted_at: Mapped[datetime] = mapped_column(
        "granted_at", DateTime(), default=datetime.now(UTC), nullable=False
    )
    _scope: Mapped[str] = mapped_column("scope", Text(), nullable=False)

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self._client_id = value

    @property
    def subject_id(self) -> typing.Any:
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value: typing.Any) -> None:
        self._subject_id = value

    @property
    def granted_at(self) -> datetime:
        return self._granted_at

    @granted_at.setter
    def granted_at(self, value: datetime) -> None:
        self._granted_at = value

    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, value: str) -> None:
        self._scope = value


class OAuthAuthorizationCode(
    OAuthAuthorizationCodeModel,
):
    __tablename__ = "oauth_authorization_codes"

    _code: Mapped[str] = mapped_column(
        "code", String(64), primary_key=True, nullable=False
    )
    _client_id: Mapped[str] = mapped_column(
        "client_id", ForeignKey("oauth_clients.client_id"), nullable=False
    )
    _subject_id: Mapped[typing.Any] = mapped_column(
        "subject_id", String(128), nullable=False, primary_key=True
    )
    _expires_at: Mapped[datetime] = mapped_column(
        "expires_at", DateTime(), nullable=False
    )
    _response_type: Mapped[str] = mapped_column(
        "response_type", String(128), nullable=False
    )
    _redirect_uri: Mapped[str | None] = mapped_column(
        "redirect_uri", Text(), nullable=True
    )
    _scope: Mapped[str] = mapped_column("scope", Text(), nullable=False)
    _code_challenge: Mapped[str] = mapped_column(
        "code_challenge", String(128), nullable=False
    )
    _code_challenge_method: Mapped[CodeChallengeMethod] = mapped_column(
        "code_challenge_method", String(128), nullable=False
    )

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        self._code = value

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self._client_id = value

    @property
    def subject_id(self) -> typing.Any:
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value: typing.Any) -> None:
        self._subject_id = value

    @property
    def expires_at(self) -> datetime:
        return self._expires_at

    @expires_at.setter
    def expires_at(self, value: datetime) -> None:
        self._expires_at = value

    @property
    def response_type(self) -> str:
        return self._response_type

    @response_type.setter
    def response_type(self, value: str) -> None:
        self._response_type = value

    @property
    def redirect_uri(self) -> str | None:
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value: str | None) -> None:
        self._redirect_uri = value

    @property
    def scope(self) -> str:
        return self._scope

    @scope.setter
    def scope(self, value: str) -> None:
        self._scope = value

    @property
    def code_challenge(self) -> str:
        return self._code_challenge

    @code_challenge.setter
    def code_challenge(self, value: str) -> None:
        self._code_challenge = value

    @property
    def code_challenge_method(self) -> CodeChallengeMethod:
        return self._code_challenge_method

    @code_challenge_method.setter
    def code_challenge_method(self, value: CodeChallengeMethod) -> None:
        self._code_challenge_method = value


__all__ = [
    "OAuthClient",
    "OAuthGrant",
    "OAuthAuthorizationCode",
]
