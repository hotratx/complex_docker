import aioredis
from typing import Any, Optional, Generator

from fastapi import APIRouter, Depends, Path, Body, Header, Cookie

from app.core import config
from app import schemas
from app.api.deps import get_db
from app import crud
#from app.redis import redis
from sqlalchemy.orm import Session


router = APIRouter()

redis = aioredis.from_url(config.settings.REDIS_HOST +"://"+ config.settings.REDIS_HOST+":"+config.settings.REDIS_PORT)


@router.post("/values")
async def banco(
        *,
        db: Session = Depends(get_db),
        user_in: schemas.Values
        ) -> Any:
    await redis.set('values', user_in.index)
    await crud.values.create_values(db=db, value=user_in)
    return {"working": "True"}


@router.get("/values/all")
async def get_user(
        *,
        db: Session = Depends(get_db),
        ) -> Any:
    values = await crud.values.get(db)
    return values 


@router.get("/values/current")
async def read_items():
    chave = await redis.get("values")
    return chave
