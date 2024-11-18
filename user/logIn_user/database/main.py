from datetime import datetime


from database.main import *
from ..models import model_autme


async def select_user(
        data_user: model_autme,
        hash_password: str
) -> AutmeBaseModel | None:
    query = select(AutmeBaseModel).filter(AutmeBaseModel.email == data_user.email)
    async with Session() as session:
        result: AutmeBaseModel = await session.execute(query)
        return result


async def insert_user_new_token(
        data_user: model_autme,
        token: str,
        user_id: str
) -> bool:
    async with Session() as session:
        new_device_user = DeviceBaseModel(
            name=data_user.device.user_device,
            ip_device=data_user.device.user_ip,
        )
        session.add(new_device_user)
        await session.commit()
        query = select(DeviceBaseModel).filter(DeviceBaseModel.name == data_user.device.user_device).order_by(DeviceBaseModel.id.desc())
        result = await session.execute(query)
        for current_device in result.scalars():
            new_token_user = TokenBaseModel(
                user_id=user_id,
                token=token,
                create_date=datetime.now(),
                device=current_device.id
            )
            session.add(new_token_user)
            try:
                await session.commit()
            except Exception as e:
                return False
            return True