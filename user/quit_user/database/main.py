from starlette.exceptions import HTTPException

from database.main import *
from sqlalchemy import delete

from user.quit_user.redis import delete_redis
from user.register.model import failed_respounse_model as pd_respounse_model


async def delete_current_token(
    token: str
) -> pd_respounse_model:
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.token == token)
        result: list[TokenBaseModel] = await session.execute(query)
        for current_user in result.scalars():
            query = delete(TokenBaseModel).where(TokenBaseModel.token == token)
            await session.execute(query)
            query = delete(DeviceBaseModel).where(DeviceBaseModel.id == current_user.device)
            await session.execute(query)
            await session.commit()
            await delete_redis(token)
            return pd_respounse_model(message="Вы успешно вышли с аккаунта")
    raise HTTPException(status_code=422, detail="Возникла ошибка при выходе из аккаунта, похоже ваш токен не действителен")
