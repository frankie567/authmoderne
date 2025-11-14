import dataclasses
import typing
from collections.abc import Callable, Coroutine, Iterable

from authmoderne.storage import DoesNotExist, StorageProtocol, StorageProvider


@dataclasses.dataclass
class MockModel:
    id: str


class MockStorage[Model](StorageProtocol[Model]):
    def __init__(self, model: type[Model], data: list[Model]) -> None:
        self.model = model
        self._data = data

    async def get_one_by(self, **filters: typing.Any) -> Model:
        for obj in self._data:
            if all(getattr(obj, key) == value for key, value in filters.items()):
                return obj
        raise DoesNotExist()

    async def create(self, **data: typing.Any) -> Model:
        obj = self.model(**data)
        self._data.append(obj)
        return obj

    async def update(self, obj: Model, **data: typing.Any) -> Model:
        for key, value in data.items():
            setattr(obj, key, value)
        return obj


class MockStorageProvider(StorageProvider):
    def __init__[Model](
        self,
        data: dict[typing.Any, list[typing.Any]],
        models: Iterable[type[Model]] | None = None,
        storage_class: type[MockStorage[typing.Any]] = MockStorage,
    ) -> None:
        super().__init__(models=models)
        self.data = data
        self.storage_class = storage_class

    def _get_storage_factory(
        self,
    ) -> Callable[..., Coroutine[None, None, StorageProtocol[typing.Any]]]:
        async def _get_storage[Model](model: type[Model]) -> StorageProtocol[Model]:
            return self.storage_class(model, self.data.get(model, []))

        return _get_storage
