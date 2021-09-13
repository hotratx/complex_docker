from typing import Optional
from pydantic import BaseModel


class UserOut(BaseModel):
    name: str
    email: str
    endereco: Optional[str] = None


class User(BaseModel):
    name: str
    sobrenome: Optional[str] = None
    email: str
    endereco: Optional[str] = None


class Values(BaseModel):
    index: int
