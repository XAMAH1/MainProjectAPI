from datetime import datetime, timezone
import random
from dotenv import load_dotenv
import os

from fastapi import HTTPException
import jwt

from md5_hash.md5_hash import calculate_md5
from user.logIn_user.models import respounse_model, model_autme, model_device
from user.logIn_user.database import select_user, insert_user_new_token

load_dotenv()

async def login_user_system(data_user: model_autme) -> respounse_model:
    hash_password = calculate_md5(
        data_user.password
    )
    result = await select_user(
        data_user
    )
    for current_user in result.scalars():
        if hash_password != current_user.password:
            raise HTTPException(
                status_code=401,
                detail="Не правильный логин или пароль"
            )
        jwt_token = jwt.encode(
            {
                "email": data_user.email,
                "time": str(datetime.now(tz=timezone.utc)),
                'random_int': random.randint(1, 999999)
            },
            os.getenv('JWT_KEY'),
            algorithm='HS256'
        )
        if not await insert_user_new_token(
                data_user=data_user,
                token=jwt_token,
                user_id=current_user.id
        ):
            raise HTTPException(
                status_code=422,
                detail="Ошибка авторизации"
            )
        return respounse_model(token=str(jwt_token))
    raise HTTPException(
        status_code=401,
        detail="Не правильный логин или пароль"
    )


if __name__ == '__main__':
    import asyncio
    print(asyncio.run(login_user_system(model_autme(email="wefwe1few@mail.ru", nickname="XAMAH", password="123", device=model_device(user_ip="192.168.0.1", user_device="SERVER")))))

