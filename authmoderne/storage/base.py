import typing

from ..exceptions import AuthmoderneException


class StorageError(AuthmoderneException):
    """Base exception for all storage-related errors."""


class DoesNotExist(StorageError):
    """Error raised when a requested object does not exist in storage."""

    def __init__(self) -> None:
        message = "The requested object does not exist in storage."
        super().__init__(message)


class StorageProtocol(typing.Protocol):
    """Protocol for storage backends."""

    async def get_one_by_id[Model](self, model: type[Model], id: typing.Any) -> Model:
        """Retrieve an object by its ID.

        Args:
            model: The model class to query.
            id: The ID of the object to retrieve.

        Raises:
            DoesNotExist: If the object does not exist in storage.

        Returns:
            The retrieved object.
        """
        ...

    async def get_one_by[Model](
        self, model: type[Model], **filters: typing.Any
    ) -> Model:
        """Retrieve an object by arbitrary filters.

        Args:
            model: The model class to query.
            **filters: A set of key-value pairs to filter the query.

        Raises:
            DoesNotExist: If the object does not exist in storage.

        Returns:
            The retrieved object.
        """
        ...

    async def create[Model](self, model: type[Model], object: typing.Any) -> Model:
        """Create a new object in storage.

        Args:
            model: The model class to create.
            object: The object data to create.

        Returns:
            The created object.
        """
        ...
