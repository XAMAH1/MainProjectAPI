from fastapi import HTTPException
from fastapi.params import Depends

from sqlalchemy import delete

from auth import auth
from database.main import *
from user.quit_current_user.model import model_token, model_respounse
from user.quit_current_user.redis import delete_redis


async def delete_token(
        data_user: model_token,
        token: str = Depends(auth)
) -> model_respounse:
    print(token)
    print(data_user.token)
    if data_user.token == token:
        raise HTTPException(status_code=422, detail="Это ваше устройство")
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.token == data_user.token)
        result: list[TokenBaseModel] = await session.execute(query)
        for current_user in result.scalars():
            query = delete(TokenBaseModel).where(TokenBaseModel.token == data_user.token)
            await session.execute(query)
            query = delete(DeviceBaseModel).where(DeviceBaseModel.id == current_user.device)
            await session.execute(query)
            await session.commit()
            await delete_redis(token)
            return model_respounse(message="Вы успешно вышли с аккаунта")
        raise HTTPException(status_code=422, detail="Возникла ошибка при выходе из аккаунта, похоже ваш токен не действителен")