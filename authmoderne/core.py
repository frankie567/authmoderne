import contextlib
from collections.abc import Iterable

import dishka

from .storage import StorageProtocol, StorageProvider


class Authmoderne:
    def __init__(
        self,
        storage: StorageProvider | Iterable[StorageProvider],
        plugins: Iterable[dishka.Provider] | None = None,
    ) -> None:
        storages = [storage] if isinstance(storage, StorageProvider) else storage
        self._container = dishka.make_async_container(*storages, *(plugins or ()))

    def __call__(self) -> "AuthmoderneRequest":
        return AuthmoderneRequest(self._container)

    async def close(self) -> None:
        await self._container.close()


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

    async def get[C](self, cls: type[C]) -> C:
        return await self.request_container.get(cls)

    async def get_storage[Model](self, model: type[Model]) -> StorageProtocol[Model]:
        return await self.request_container.get(StorageProtocol[model])  # type: ignore[valid-type]

    @property
    def request_container(self) -> dishka.AsyncContainer:
        if self._request_container is None:
            raise RuntimeError("Request container is not initialized.")  # noqa: TRY003
        return self._request_container
