#from typing import Callable, Optional, Any

#import sqlalchemy as sa
#import sqlalchemy.orm as orm
from sqlalchemy.orm import sessionmaker
#import redis

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

#from app.db.modelbase import SqlAlchemyBase
from app.core.config import settings



#__redis: redis.Redis = None
#cache = redis.Redis("redis")

DATABASE_URL = settings.PGDATABASE
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
AsyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


#async def start_redis():
#    global __redis 
#    __redis = await aioredis.create_redis_pool(host='redis', port=6379, db=0)
#    await __redis.set('key', 'string-value')
#
#def cache():
#    return __redis
    

#__async_engine: Optional[AsyncEngine] = None
#
#
#def global_init():
#    global __async_engine
#
#    # Verifica se já foi criada a session
#    if __async_engine:
#        return
#
#    DATABASE_URL = settings.DATABASE_URL
#    print(f'Conect ao database URL: {DATABASE_URL}')
#
#    __async_engine = create_async_engine(DATABASE_URL, future=True, echo=True)
#
#    import app.db.__all_models
#
#    with __async_engine.begin() as conn:
#        conn.run_sync(SqlAlchemyBase.metadata.drop_all)
#        conn.run_sync(SqlAlchemyBase.metadata.create_all)
#
#    #SqlAlchemyBase.metadata.create_all(__async_engine)
#
#def create_async_session() -> AsyncSession:
#    global __async_engine
#
#    if not __async_engine:
#        raise Exception("You must call global_inti() before using this method.")
#
#    session: AsyncSession = sessionmaker(__async_engine, expire_on_commit=False, class_=AsyncSession)
#    session.sync_session.expire_on_commit = False
#
#    return session
        
