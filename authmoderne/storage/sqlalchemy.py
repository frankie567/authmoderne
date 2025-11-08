import typing
from collections.abc import AsyncIterable

import dishka
from sqlalchemy import URL, select
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from .base import DoesNotExist, StorageProtocol, StorageProvider


class Base(DeclarativeBase):
    pass


class SQLAlchemyStorage(StorageProtocol):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_one_by[Model](
        self, model: type[Model], **filters: typing.Any
    ) -> Model:
        statement = select(model).filter_by(**filters)
        result = await self.session.execute(statement)
        object = result.scalar_one_or_none()
        if object is None:
            raise DoesNotExist()
        return object

    async def create[Model](self, model: type[Model], **data: typing.Any) -> Model:
        object = model(**data)
        self.session.add(object)
        await self.session.flush()
        return object


class SQLAlchemyEngineProvider(StorageProvider):
    def __init__(self, url: str | URL) -> None:
        super().__init__()
        self.url = url

    @dishka.provide(scope=dishka.Scope.APP)
    async def get_engine(self) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(self.url)
        yield engine
        await engine.dispose()

    @dishka.provide(scope=dishka.Scope.APP)
    async def get_sessionmaker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @dishka.provide(scope=dishka.Scope.REQUEST)
    async def get_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            try:
                yield session
            except:
                await session.rollback()
                raise
            else:
                await session.commit()

    @dishka.provide(scope=dishka.Scope.REQUEST)
    async def get_storage(self, session: AsyncSession) -> SQLAlchemyStorage:
        return SQLAlchemyStorage(session)


__all__ = [
    "Base",
    "SQLAlchemyStorage",
    "SQLAlchemyEngineProvider",
]
