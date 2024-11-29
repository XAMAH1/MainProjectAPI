from redis import main_redis


async def delete_redis(token: str):
    try:
        redis = await main_redis()
        await redis.delete(token)
        await redis.close()
    except:
        ...
