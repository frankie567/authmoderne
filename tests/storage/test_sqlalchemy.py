from collections.abc import AsyncGenerator

import pytest
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column

from authmoderne.storage.base import DoesNotExist
from authmoderne.storage.sqlalchemy import Base, SQLAlchemyStorage


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
async def sqlalchemy_storage(sqlalchemy_session: AsyncSession) -> SQLAlchemyStorage:
    return SQLAlchemyStorage(sqlalchemy_session)


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_sqlalchemy_storage(
    anyio_backend: str, sqlalchemy_storage: SQLAlchemyStorage
) -> None:
    # Create a new model instance
    model_instance = await sqlalchemy_storage.create(Model, name="Test Model")
    assert model_instance.id is not None
    assert model_instance.name == "Test Model"

    # Retrieve the model instance by its name
    retrieved_instance = await sqlalchemy_storage.get_one_by(Model, name="Test Model")
    assert retrieved_instance.id == model_instance.id
    assert retrieved_instance.name == "Test Model"

    # Attempt to retrieve a non-existent model instance
    with pytest.raises(DoesNotExist):
        await sqlalchemy_storage.get_one_by(Model, name="Non-Existent Model")
