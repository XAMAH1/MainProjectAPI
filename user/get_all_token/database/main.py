from database.main import *


async def select_token_user(
       token: str
) -> list[TokenBaseModel]:
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.token == token)
        result: list[TokenBaseModel] = await session.execute(query)
        return result


async def select_all_token_user(
        user_id: str
):
    async with (Session() as session):
        query = (
            select(TokenBaseModel, DeviceBaseModel)
            .filter(TokenBaseModel.user_id == user_id)
            .join(DeviceBaseModel, TokenBaseModel.device == DeviceBaseModel.id)
            .limit(15)
            .order_by(TokenBaseModel.id.desc())
            )
        result = await session.execute(query)
        return result
