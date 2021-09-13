from fastapi import FastAPI
from typing import Any, Optional, Generator
import uvicorn

from app.api.api import api_router
from app.db.modelbase import SqlAlchemyBase
from app.db.db_session import engine

app = FastAPI(title='FastAPI, postree and docker')

#def main():
#    uvicorn.run(app, host="127.0.0.1", port=8000)
app.include_router(api_router)

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.drop_all)
        await conn.run_sync(SqlAlchemyBase.metadata.create_all)
#
#@app.get("/")
#def read_root():
#    return {"hello": "World"}
#
#@app.post("/user", response_model=schemas.User)
#async def banco(
#        *,
#        user_in: schemas.User,
#        ) -> Any:
#    async with AsyncSession() as session:
#        async with session.begin():
#            usuario = crud.user.create(session, user=user_in)
#            return usuario

#@app.post("/redis", response_model=Item)
#async def redis_set(item: Item) -> str:
#    async with AsyncSession() as session:
#        async with session.begin():
#            book_dal = User(session)
#            return book_dal.put_redis(item)
#
#@app.get("/getredis/{name}")
#async def get_redis(name: str):
#    async with AsyncSession() as session:
#        async with session.begin():
#            var = User(session)
#            return var.get_red(name)


#@app.get("/users")
#async def get_user():
#    async with AsyncSession() as session:
#        async with session.begin():
#            users = await crud.user.get_all_user(db=session)
#            return users 


#if __name__ == "__main__":
#    main()
if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, debug=True)
