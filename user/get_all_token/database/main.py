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
) -> list[TokenBaseModel]:
    async with Session() as session:
        query = select(TokenBaseModel).filter(TokenBaseModel.user_id == user_id)
        result: list[TokenBaseModel] = await session.execute(query)
        return result
