import redis

from app.config.settings import settings


def get_redis():
    try:
        connection = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            username=settings.REDIS_USER,
            password=settings.REDIS_PASSWORD,
            decode_responses=True,
            db=settings.REDIS_DB
        )
        if connection.ping() is True:
            return connection
    except redis.RedisError as e:
        raise ValueError(f"Error connecting to Redis: {e}")