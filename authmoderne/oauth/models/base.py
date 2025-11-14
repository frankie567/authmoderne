import typing
from datetime import datetime

from authmoderne.models import AuthmoderneModel

from ..types import CodeChallengeMethod


class OAuthClientModel(AuthmoderneModel):
    """Base model for OAuth client implementations."""

    client_id: str


class OAuthGrantModel(AuthmoderneModel):
    """Base model for OAuth grant implementations."""

    client_id: str
    subject_id: typing.Any
    granted_at: datetime
    scope: str


class OAuthAuthorizationCodeModel(AuthmoderneModel):
    """Base model for OAuth authorization code implementations."""

    code: str
    client_id: str
    subject_id: typing.Any
    expires_at: datetime
    response_type: str
    redirect_uri: str | None
    scope: str
    code_challenge: str
    code_challenge_method: CodeChallengeMethod


__all__ = [
    "OAuthClientModel",
    "OAuthGrantModel",
    "OAuthAuthorizationCodeModel",
]
