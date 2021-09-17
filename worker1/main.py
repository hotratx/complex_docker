import redis
import time

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str

    class config:
        case_sensitive = True

settings = Settings()

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


def run():
    while True:
        try:
            valor = r.get("values")
            r.set("values", int(valor*2))
        except:
            print("erro leitura worker")
        time.sleep(2)


if __name__ == "__main__":
    run()
