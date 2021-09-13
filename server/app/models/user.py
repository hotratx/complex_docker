from sqlalchemy import Column, Integer, String

from app.db.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(30))
    sobrenome: str = Column(String(40), nullable=True)
    email: str = Column(String(40))
    endereco: str = Column(String(40), nullable=True)

    def __repr__(self):
        return f'User(self.name)'


class Values(SqlAlchemyBase):
    __tablename__ = "values"

    index: int = Column(Integer, primary_key=True)

    def __repr__(self):
        return f'Values(self.index)'
