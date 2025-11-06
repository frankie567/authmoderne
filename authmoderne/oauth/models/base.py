import typing
from datetime import datetime

from ..types import CodeChallengeMethod


class OAuthClientProtocol(typing.Protocol):
    """Protocol for OAuth client implementations."""

    client_id: str


class OAuthGrantProtocol[SubjectID](typing.Protocol):
    """Protocol for OAuth grant implementations."""

    client_id: str
    subject_id: SubjectID
    granted_at: datetime
    scope: str


class OAuthAuthorizationCodeProtocol[SubjectID](typing.Protocol):
    """Protocol for OAuth authorization code implementations."""

    code: str
    client_id: str
    subject_id: SubjectID
    expires_at: datetime
    response_type: str
    redirect_uri: str | None
    scope: str
    code_challenge: str
    code_challenge_method: CodeChallengeMethod
