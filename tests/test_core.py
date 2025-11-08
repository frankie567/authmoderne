import pytest

from authmoderne.core import Authmoderne
from tests.conftest import MockStorage, MockStorageProvider


@pytest.mark.anyio
async def test_authmoderne() -> None:
    authmoderne = Authmoderne(MockStorageProvider())
    async with authmoderne() as authmoderne_request:
        storage = await authmoderne_request.get_storage()
        assert isinstance(storage, MockStorage)
