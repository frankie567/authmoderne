import dataclasses

import pytest

from authmoderne.core import Authmoderne
from tests.conftest import MockModel, MockStorage, MockStorageProvider


@pytest.mark.anyio
class TestAuthmoderneGetStorage:
    async def test_single_storage(self) -> None:
        authmoderne = Authmoderne(MockStorageProvider({}))
        async with authmoderne() as authmoderne_request:
            storage = await authmoderne_request.get_storage(MockModel)
            assert isinstance(storage, MockStorage)

    async def test_multiple_storages(self) -> None:
        class FirstMockStorage[Model](MockStorage[Model]):
            pass

        @dataclasses.dataclass
        class FirstMockModel: ...

        class SecondMockStorage[Model](MockStorage[Model]):
            pass

        @dataclasses.dataclass
        class SecondMockModel: ...

        authmoderne = Authmoderne(
            (
                MockStorageProvider(
                    {}, models=[FirstMockModel], storage_class=FirstMockStorage
                ),
                MockStorageProvider(
                    {}, models=[SecondMockModel], storage_class=SecondMockStorage
                ),
            )
        )
        async with authmoderne() as authmoderne_request:
            first_storage = await authmoderne_request.get_storage(FirstMockModel)
            assert isinstance(first_storage, FirstMockStorage)

            second_storage = await authmoderne_request.get_storage(SecondMockModel)
            assert isinstance(second_storage, SecondMockStorage)
