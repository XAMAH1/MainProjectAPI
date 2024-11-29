from redis import main_redis


async def post_redis(mass: list, token: str):
    redis = await main_redis()
    await redis.set(key=token, value=mass, timeout=30)
    await redis.close()


async def get_redis(token: str):
    redis = await main_redis()
    result = await redis.get(token)
    await redis.close()
    if result:
        return result
    return False