import typing

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from .base import DoesNotExist, StorageProtocol


class Base(DeclarativeBase):
    pass


class SQLAlchemyStorage(StorageProtocol):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_one_by_id[Model](self, model: type[Model], id: typing.Any) -> Model:
        object = await self.session.get(model, id)
        if object is None:
            raise DoesNotExist()
        return object

    async def get_one_by[Model](
        self, model: type[Model], **filters: typing.Any
    ) -> Model:
        statement = select(model).filter_by(**filters)
        result = await self.session.execute(statement)
        object = result.scalar_one_or_none()
        if object is None:
            raise DoesNotExist()
        return object

    async def create[Model](self, model: type[Model], object: Model) -> Model:
        self.session.add(object)
        await self.session.flush()
        return object
