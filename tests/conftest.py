import typing

import pytest

from authmoderne.storage import DoesNotExist, StorageProtocol


class MockStorage(StorageProtocol):
    def __init__(self) -> None:
        self._data: dict[typing.Any, dict[str, typing.Any]] = {}

    async def get_by_id[Model](self, model: type[Model], id: typing.Any) -> Model:
        try:
            return self._get_model_mapping(model)[id]
        except KeyError as e:
            raise DoesNotExist() from e

    async def create[Model](self, model: type[Model], object: Model) -> Model:
        model_mapping = self._get_model_mapping(model)
        object_id = getattr(object, "id")
        model_mapping[object_id] = object
        return object

    def _get_model_mapping[Model](self, model: type[Model]) -> dict[str, Model]:
        if model not in self._data:
            self._data[model] = {}
        return self._data[model]


@pytest.fixture
def mock_storage() -> MockStorage:
    return MockStorage()
