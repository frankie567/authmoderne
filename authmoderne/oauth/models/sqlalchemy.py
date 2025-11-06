import typing
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...storage.sqlalchemy import Base
from ..types import CodeChallengeMethod


class OAuthClient(Base):
    __tablename__ = "oauth_clients"

    _client_id: Mapped[str] = mapped_column(
        String(128), primary_key=True, unique=True, nullable=False
    )

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str) -> None:
        self._client_id = value


class OAuthGrant(Base):
    __tablename__ = "oauth_grants"

    _client_id: Mapped[str] = mapped_column(
        ForeignKey("oauth_clients.client_id"), nullable=False, primary_key=True
    )
    _subject_id: Mapped[typing.Any] = mapped_column(
        String(128), nullable=False, primary_key=True
    )
    _granted_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(UTC), nullable=False
    )
    _scope: Mapped[str] = mapped_column(Text(), nullable=False)

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def subject_id(self) -> typing.Any:
        return self._subject_id

    @property
    def granted_at(self) -> datetime:
        return self._granted_at

    @property
    def scope(self) -> str:
        return self._scope


class OAuthAuthorizationCode[SubjectID](Base):
    __tablename__ = "oauth_authorization_codes"

    _code: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    _client_id: Mapped[str] = mapped_column(
        ForeignKey("oauth_clients.client_id"), nullable=False
    )
    _subject_id: Mapped[SubjectID] = mapped_column(
        String(128), nullable=False, primary_key=True
    )
    _expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    _response_type: Mapped[str] = mapped_column(String(128), nullable=False)
    _redirect_uri: Mapped[str | None] = mapped_column(Text(), nullable=True)
    _scope: Mapped[str] = mapped_column(Text(), nullable=False)
    _code_challenge: Mapped[str] = mapped_column(String(128), nullable=False)
    _code_challenge_method: Mapped[CodeChallengeMethod] = mapped_column(
        String(128), nullable=False
    )

    @property
    def code(self) -> str:
        return self._code

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def subject_id(self) -> SubjectID:
        return self._subject_id

    @property
    def expires_at(self) -> datetime:
        return self._expires_at

    @property
    def response_type(self) -> str:
        return self._response_type

    @property
    def redirect_uri(self) -> str | None:
        return self._redirect_uri

    @property
    def scope(self) -> str:
        return self._scope

    @property
    def code_challenge(self) -> str:
        return self._code_challenge

    @property
    def code_challenge_method(self) -> CodeChallengeMethod:
        return self._code_challenge_method


__all__ = [
    "OAuthClient",
    "OAuthGrant",
    "OAuthAuthorizationCode",
]
