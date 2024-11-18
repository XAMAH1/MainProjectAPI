from fastapi import HTTPException

from sqlalchemy import delete

from database.main import *
from user.quit_user.model import model_token, model_respounse


async def delete_token(data_user: model_token) -> model_respounse:
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.token == data_user.token)
        result: list[TokenBaseModel] = await session.execute(query)
        for current_user in result.scalars():
            query = delete(TokenBaseModel).where(TokenBaseModel.token == data_user.token)
            await session.execute(query)
            query = delete(DeviceBaseModel).where(DeviceBaseModel.id == current_user.device)
            await session.execute(query)
            await session.commit()
            return model_respounse(message="Вы успешно вышли с аккаунта")
        raise HTTPException(status_code=422, detail="Возникла ошибка при выходе из аккаунта, похоже ваш токен не действителен")