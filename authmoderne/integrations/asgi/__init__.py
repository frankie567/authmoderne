from asgiref.typing import (
    ASGI3Application,
    ASGIReceiveCallable,
    ASGISendCallable,
    Scope,
)

from authmoderne.core import Authmoderne


class AuthmoderneMiddleware:
    def __init__(self, app: ASGI3Application, *, authmoderne: Authmoderne) -> None:
        self.app = app
        self.authmoderne = authmoderne

    async def __call__(
        self, scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable
    ) -> None:
        if scope["type"] not in {"http", "websocket"}:
            await self.app(scope, receive, send)
            return

        async with self.authmoderne() as authmoderne_request:
            state = scope.get("state", {})
            state["authmoderne_request"] = authmoderne_request
            scope["state"] = state

            return await self.app(scope, receive, send)
