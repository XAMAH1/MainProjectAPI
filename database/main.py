import asyncio

from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from database.base import Base
from database.models import UserBaseModel, TokenBaseModel, DeviceBaseModel, AutmeBaseModel, SubscriptionBaseModel as Subscription, AccessBaseModel as Access, RoleBaseModel
from database.settings import get_settings_connect
from logger import logger

engine = create_async_engine(
    url=get_settings_connect(),
    echo=False,
    pool_size=10,
    max_overflow=100,
)





Session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def create_table():
    async with engine.begin() as connection:
        logger.info("Началось создание базы данных")
        await connection.run_sync(Base.metadata.drop_all)
        logger.info("Старая база данных была удалена")
        await connection.run_sync(Base.metadata.create_all)
        logger.info("Новая база данных успешно создана")
#
#
async def check_static_data():
    try:
        async with Session() as session:
            query = (
                select(Subscription)
                .select_from(Subscription)
                .where(Subscription.price >= 0)
            )
            res = await session.execute(query)
            if len(res.scalars().all()) == 0:
                session.add(Subscription(name="Базовая", price=0, isHide=False))
                await session.commit()

            query = (
                select(Subscription)
                .select_from(Subscription)
                .where(Subscription.price >= 0)
            )
            res = await session.execute(query)
            for i in res.scalars().all():
                logger.info(i)

            query = (
                select(Access)
                .select_from(Access)
                .where(Access.id >= 0)
            )
            res = await session.execute(query)
            if len(res.scalars().all()) == 0:
                session.add(Access(description="Административные права", subscription_name="Базовая"))
            logger.debug("Проверка завершена")
            await session.commit()
    except Exception as e:
        print(e)

# asyncio.run(create_table())
# asyncio.run(check_static_data())


# class accessModelDTO(BaseModel):
#     id: int
#     description: str
#     subscription_name: str
#
#
#
# def get_connection():
#     with engine.connect() as connection:
#         print(connection)
#
# def insert_user():
#     with Session() as session:
#         user = UserBaseModel(
#             nickname="ХАМАН",
#             last_name="Качалкин",
#             first_name="Илья",
#             email="cuperopen@mail.ru",
#             phone="89195659986",
#             role="user",
#             subscription="Базовая"
#         )
#         autme = AutmeBaseModel(
#             email="cuperopen@mail.ru",
#             password="123",
#
#         )
#         session.add_all([user, autme])
#         session.commit()
#
#
# def get_colums():
#     with Session() as session:
#         query = (
#             select(
#                 UserBaseModel,
#                 )
#             .select_from(UserBaseModel)
#             .order_by(UserBaseModel.email.desc())
#         )
#         # print(sqr)
#         # query = (
#         #     select(
#         #         sqr
#         #     ).order_by(AutmeModel.create_date.desc())
#         # )
#         print(query)
#         res = session.execute(query)
#         for i in res.scalars().all():
#             print(i)
#
#
# async def select_user():
#     # while True:
#         async with Session() as session:
#             query = (
#                 select(AutmeBaseModel)
#                 .select_from(AutmeBaseModel)
#             )
#             res = await session.execute(query)
#             res = res.scalars().all()
#             result: list[AutmeModelDTO] = [AutmeModelDTO.model_validate(row, from_attributes=True) for row in res]
#             for ress in result:
#                 logger.warning(ress)
# #
# from datetime import datetime
#
# class AutmeModelDTO(BaseModel):
#     email: str
#     id: str
#
#
# class UserModelDTO(BaseModel):
#     email: str
#     nickname: str
#     first_name: str
#     last_name: str
#     phone: str
#     role: str
#     subscription: str
#     subscription_start_time: datetime
#     subscription_end_time: datetime
# #
# #
#
# asyncio.run(select_user())
# create_table()
# check_static_data()
# insert_user()
# get_connection()
# insert_colums()
# print(get_colums())
# num_error = 0
# print("в цикл")
# while True:
#     try:
#         get_colums()
#     except KeyboardInterrupt:
#         print("Buy")
#     except AttributeError as e:
#         print(f"{num_error}. Error {e.name} -> {e}")
#         num_error += 1
#     except Exception as e:
#         print(f"{num_error}. Error Exception -> {e}")
#         num_error += 1

