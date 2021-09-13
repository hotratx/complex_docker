from typing import Generic, Type, TypeVar

from pydantic import BaseModel

from app.db.modelbase import SqlAlchemyBase

ModelType = TypeVar("ModelType", bound=SqlAlchemyBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self):
        return 'oi'
