import typing
from collections.abc import Callable, Coroutine, Iterable

import dishka

from ..exceptions import AuthmoderneException


class StorageError(AuthmoderneException):
    """Base exception for all storage-related errors."""


class DoesNotExist(StorageError):
    """Error raised when a requested object does not exist in storage."""

    def __init__(self) -> None:
        message = "The requested object does not exist in storage."
        super().__init__(message)


class StorageProtocol[Model](typing.Protocol):
    """Protocol for storage backends."""

    model: type[Model]

    async def get_one_by(self, **filters: typing.Any) -> Model:
        """Retrieve an object by arbitrary filters.

        Args:
            **filters: A set of key-value pairs to filter the query.

        Raises:
            DoesNotExist: If the object does not exist in storage.

        Returns:
            The retrieved object.
        """
        ...

    async def create(self, **data: typing.Any) -> Model:
        """Create a new object in storage.

        Args:
            object: The object data to create.

        Returns:
            The created object.
        """
        ...


class StorageProvider(dishka.Provider):
    """Base class for storage providers."""

    def __init__[Model](
        self, *args: typing.Any, models: Iterable[type[Model]], **kwargs: typing.Any
    ) -> None:
        super().__init__()
        for model in models:
            self.provide(
                self._get_storage_factory(model),
                scope=dishka.Scope.REQUEST,
                provides=StorageProtocol[model],  # type: ignore[valid-type]
            )

    def _get_storage_factory[Model](
        self, model: type[Model]
    ) -> Callable[..., Coroutine[None, None, StorageProtocol[Model]]]:
        raise NotImplementedError()
