from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ...storage.sqlalchemy import Base
from ..types import CodeChallengeMethod


class OAuthClient(Base):
    __tablename__ = "oauth_clients"

    client_id: Mapped[str] = mapped_column(
        String(128), primary_key=True, unique=True, nullable=False
    )


class OAuthGrant[SubjectID](Base):
    __tablename__ = "oauth_grants"

    client_id: Mapped[str] = mapped_column(
        ForeignKey("oauth_clients.client_id"), nullable=False, primary_key=True
    )
    subject_id: Mapped[SubjectID] = mapped_column(
        String(128), nullable=False, primary_key=True
    )
    granted_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(UTC), nullable=False
    )
    scope: Mapped[str] = mapped_column(Text(), nullable=False)


class OAuthAuthorizationCode[SubjectID](Base):
    __tablename__ = "oauth_authorization_codes"

    code: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    client_id: Mapped[str] = mapped_column(
        ForeignKey("oauth_clients.client_id"), nullable=False
    )
    subject_id: Mapped[SubjectID] = mapped_column(
        String(128), nullable=False, primary_key=True
    )
    expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    response_type: Mapped[str] = mapped_column(String(128), nullable=False)
    redirect_uri: Mapped[str | None] = mapped_column(Text(), nullable=True)
    scope: Mapped[str] = mapped_column(Text(), nullable=False)
    code_challenge: Mapped[str] = mapped_column(String(128), nullable=False)
    code_challenge_method: Mapped[CodeChallengeMethod] = mapped_column(
        String(128), nullable=False
    )
