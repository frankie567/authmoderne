from collections.abc import AsyncGenerator

import dishka
import pytest
from sqlalchemy import String
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Mapped, mapped_column

from authmoderne.storage import DoesNotExist, StorageProtocol
from authmoderne.storage.sqlalchemy import (
    Base,
    SQLAlchemyEngineProvider,
    SQLAlchemyStorage,
)


class Model(Base):
    __tablename__ = "models"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)


@pytest.fixture
async def sqlalchemy_session() -> AsyncGenerator[AsyncSession]:
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    async with sessionmaker() as async_session:
        yield async_session

    await engine.dispose()


@pytest.fixture
async def sqlalchemy_storage(
    sqlalchemy_session: AsyncSession,
) -> SQLAlchemyStorage[Model]:
    return SQLAlchemyStorage[Model](Model, sqlalchemy_session)


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_sqlalchemy_storage(
    anyio_backend: str, sqlalchemy_storage: SQLAlchemyStorage[Model]
) -> None:
    # Create a new model instance
    model_instance = await sqlalchemy_storage.create(name="Test Model")
    assert model_instance.id is not None
    assert model_instance.name == "Test Model"

    # Retrieve the model instance by its name
    retrieved_instance = await sqlalchemy_storage.get_one_by(name="Test Model")
    assert retrieved_instance.id == model_instance.id
    assert retrieved_instance.name == "Test Model"

    # Attempt to retrieve a non-existent model instance
    with pytest.raises(DoesNotExist):
        await sqlalchemy_storage.get_one_by(name="Non-Existent Model")


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_engine_provider(anyio_backend: str) -> None:
    container = dishka.make_async_container(
        SQLAlchemyEngineProvider("sqlite+aiosqlite:///:memory:", {Model})
    )

    engine = await container.get(AsyncEngine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with container() as request_container:
        sqlalchemy_storage = await request_container.get(StorageProtocol[Model])
        assert isinstance(sqlalchemy_storage, SQLAlchemyStorage)

        model_instance = await sqlalchemy_storage.create(name="Test Model")
        assert model_instance.id is not None
        assert model_instance.name == "Test Model"

    await container.close()
