from typing import Generic, Type, TypeVar
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from fastapi.encoders import jsonable_encoder

from app.db.modelbase import SqlAlchemyBase
from app.models.user import User, Values
from app import schemas

#from pydantic import BaseModel


ModelType = TypeVar("ModelType", bound=SqlAlchemyBase)
#CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
#UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase:
   def __init__(self, model: Type[ModelType]):
        self.model = model


class CRUDUser(CRUDBase):
    async def create(self, db: Session, user: schemas.User):
        obj_in_data = jsonable_encoder(user)
        db_user = self.model(**obj_in_data)
        db.add(db_user)
        await db.commit()
        #db.flush(db_user)
        #return {'name': 'sdf', 'email': 'lkj'}
        #return obj_in_data


    async def get_all_user(self, db: Session):
        q = await db.execute(select(self.model).order_by(self.model.email))
        return q.scalars().all()


class CRUDValues(CRUDBase):
    async def create_values(self, db: Session, value: schemas.Values):
        obj_in_data = jsonable_encoder(value)
        db_values = self.model(**obj_in_data)
        db.add(db_values)
        await db.commit()

    async def get(self, db: Session):
        q = await db.execute(select(self.model).order_by(self.model.index))
        return q.scalars().all()
        

user = CRUDUser(User)
values = CRUDValues(Values)
