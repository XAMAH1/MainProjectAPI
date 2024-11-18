from datetime import datetime
from fastapi import HTTPException
import random

from md5_hash.md5_hash import calculate_md5
from user.register.database import get_mail_user, insert_user
from user.register.model import model_new_user, failed_respounse_model


async def registration_new_user_system(data_user: model_new_user) -> failed_respounse_model :
    if not await get_mail_user(data_user.email):
        raise  HTTPException(status_code=400, detail="Эта почта уже занята")
    get_user_id = calculate_md5(str({'username': {data_user.nickname}, 'datetime': {str(datetime.today())}, 'random_int': random.randint(1, 999999)}))
    get_password_user = calculate_md5(data_user.password)
    if not await insert_user(data_user, get_user_id, get_password_user):
        raise HTTPException(status_code=400, detail="Возникла ошибка при регистрации, попробуйте еще раз")
    print(get_user_id)
    return failed_respounse_model(message="Аккаунт успешно создан")

# if __name__ == '__main__':
#     print(asyncio.run(registration_new_user_system(data_user=model_new_user(user=model_autme(email="wefwe1few@mail.ru", nickname="XAMAH", password="123", device= None), last_name='Качалкин', first_name="Илья", phone="89195659986"))))

