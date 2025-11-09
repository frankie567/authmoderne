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


class MockStorageProvider(StorageProvider):
    def __init__[Model](
        self, models: Iterable[type[Model]], data: dict[typing.Any, list[typing.Any]]
    ) -> None:
        super().__init__(models=models)
        self.data = data

    def _get_storage_factory[Model](
        self, model: type[Model]
    ) -> Callable[..., Coroutine[None, None, StorageProtocol[Model]]]:
        async def _get_storage() -> StorageProtocol[Model]:
            return MockStorage[Model](model, self.data.get(model, []))

        return _get_storage
