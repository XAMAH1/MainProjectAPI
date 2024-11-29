from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from dotenv import load_dotenv

from auth.database import select_token_user
from auth.redis import get_redis

http_bearer = HTTPBearer()
load_dotenv()


async def auth(user_token: str = Depends(http_bearer)):
    try:
        token = user_token.credentials
        if await get_redis(token):
            return token
        return await select_token_user(token)
    except Exception as e:
        raise HTTPException(status_code=422, detail="Ошибка проверки токена!")

