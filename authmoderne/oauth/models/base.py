import typing


class OAuthClientProtocol(typing.Protocol):
    """Protocol for OAuth client implementations."""

    client_id: str
