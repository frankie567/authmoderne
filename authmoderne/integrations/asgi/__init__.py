from asgiref.typing import (
    ASGI3Application,
    ASGIReceiveCallable,
    ASGIReceiveEvent,
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
        if scope["type"] == "lifespan":

            async def receive_lifespan() -> ASGIReceiveEvent:
                message = await receive()
                if message["type"] == "lifespan.shutdown":
                    await self.authmoderne.close()
                return message

            return await self.app(scope, receive_lifespan, send)

        async with self.authmoderne() as authmoderne_request:
            state = scope.get("state", {})
            state["authmoderne_request"] = authmoderne_request
            scope["state"] = state

            return await self.app(scope, receive, send)
