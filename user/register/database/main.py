from datetime import datetime, timedelta

from database.main import *
from user.register.model.pd_new_user import model_new_user


async def get_mail_user(mail):
    async with Session() as session:

        query: UserBaseModel = await session.execute(select(UserBaseModel).filter(UserBaseModel.email == mail))
        if query.scalar():
            return False
        return True



async def insert_user(user: model_new_user, user_id, password):
    async with Session() as session:
        new_user = UserBaseModel(
            nickname= user.nickname,
            last_name= user.last_name,
            first_name= user.first_name,
            email= user.email,
            phone= user.phone,
            subscription= "Базовая",
            role="user",
            subscription_start_time= datetime.now(),
            subscription_end_time= datetime.now() + timedelta(days=31),
        )
        new_autme = AutmeBaseModel(
            email= user.email,
            password=password,
            id=str(user_id),
            create_date=datetime.now(),
        )
        session.add_all([new_user, new_autme])
        try:
            await session.commit()
        except Exception as e:
            print(e)
            return False
        return True