from fastapi import HTTPException

from database.main import *


async def select_token_user(token: str):
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.token == token)
        result: list[TokenBaseModel] = await session.execute(query)
        for i in result.scalars():
            return i.token
        raise HTTPException(status_code=422, detail="Ваш токен не действителен")
