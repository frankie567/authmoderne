import httpx
import pytest
from asgi_lifespan import LifespanManager
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from authmoderne.core import Authmoderne, AuthmoderneRequest
from authmoderne.integrations.asgi import AuthmoderneMiddleware
from tests.conftest import MockStorageProvider


async def endpoint(request: Request) -> Response:
    authmoderne_request: AuthmoderneRequest = request.scope["state"][
        "authmoderne_request"
    ]
    assert isinstance(authmoderne_request, AuthmoderneRequest)
    return Response("OK")


authmoderne = Authmoderne(MockStorageProvider({}))


app = Starlette(
    routes=[Route("/", endpoint=endpoint)],
    middleware=[Middleware(AuthmoderneMiddleware, authmoderne=authmoderne)],
)


@pytest.mark.anyio
async def test_middleware() -> None:
    async with LifespanManager(app):
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app), base_url="http://testserver"
        ) as client:
            response = await client.get("/")
            assert response.status_code == 200
            assert response.text == "OK"
