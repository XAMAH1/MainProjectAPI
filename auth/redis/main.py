from redis import main_redis


async def post_redis(token: str):
    redis = await main_redis()
    await redis.set(key=f"{token}_auth", value="True", timeout=30)
    await redis.close()


async def get_redis(token: str):
    redis = await main_redis()
    result = await redis.get(f"{token}_auth")
    await redis.close()
    return result