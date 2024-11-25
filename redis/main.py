import asyncredis as redis
from dotenv import load_dotenv

import os
load_dotenv()


async def main_redis():
    redis_container = await redis.connect(f"redis://{os.getenv('REDIS_HOST')}:6379")
    return redis_container