import pytest

from authmoderne.core import Authmoderne
from tests.conftest import MockModel, MockStorage, MockStorageProvider


@pytest.mark.anyio
async def test_authmoderne() -> None:
    authmoderne = Authmoderne(MockStorageProvider({MockModel}, {}))
    async with authmoderne() as authmoderne_request:
        storage = await authmoderne_request.get_storage(MockModel)
        assert isinstance(storage, MockStorage)
