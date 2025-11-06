import typing

import pytest

from authmoderne.storage import DoesNotExist, StorageProtocol


class MockStorage(StorageProtocol):
    def __init__(self) -> None:
        self._data: dict[typing.Any, list[typing.Any]] = {}

    async def get_one_by[Model](
        self, model: type[Model], **filters: typing.Any
    ) -> Model:
        objects = self._get_model_objects(model)
        for obj in objects:
            if all(getattr(obj, key) == value for key, value in filters.items()):
                return obj
        raise DoesNotExist()

    async def create[Model](self, model: type[Model], **data: typing.Any) -> Model:
        objects = self._get_model_objects(model)
        obj = model(**data)
        objects.append(obj)
        return obj

    def _get_model_objects[Model](self, model: type[Model]) -> list[Model]:
        if model not in self._data:
            self._data[model] = []
        return self._data[model]


@pytest.fixture
def mock_storage() -> MockStorage:
    return MockStorage()
