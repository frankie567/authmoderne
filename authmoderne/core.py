import contextlib

import dishka

from .storage import StorageProtocol, StorageProvider


class Authmoderne:
    def __init__(self, storage_provider: StorageProvider) -> None:
        self._container = dishka.make_async_container(storage_provider)

    def __call__(self) -> "AuthmoderneRequest":
        return AuthmoderneRequest(self._container)


class AuthmoderneRequest:
    def __init__(self, container: dishka.AsyncContainer) -> None:
        self._container = container
        self._request_container: dishka.AsyncContainer | None = None
        self._exit_stack = contextlib.AsyncExitStack()

    async def __aenter__(self) -> "AuthmoderneRequest":
        self._request_container = await self._exit_stack.enter_async_context(
            self._container()
        )
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object,
    ) -> None:
        await self._exit_stack.aclose()

    async def get_storage(self) -> StorageProtocol:
        return await self.request_container.get(StorageProtocol)

    @property
    def request_container(self) -> dishka.AsyncContainer:
        if self._request_container is None:
            raise RuntimeError("Request container is not initialized.")  # noqa: TRY003
        return self._request_container
