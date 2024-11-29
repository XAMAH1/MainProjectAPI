from database.main import *
from sqlalchemy import delete
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
            return pd_respounse_model(message="Вы успешно вышли с аккаунта")
