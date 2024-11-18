import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

from database.main import  *
from fastapi.responses import JSONResponse
http_bearer = HTTPBearer()
from config import SECRET_KEY


def auth(user_token: str = Depends(http_bearer)):
    try:
        token = user_token.credentials
        result = session.query(token_autme).filter(token_autme.token == token)
        for i in result:
            if not i.autme_realt.user_realt.isRemove:
                return token
            raise HTTPException(
                status_code=401,
                detail="Аккаунт удален!"
            )
        users = jwt.decode(user_token, SECRET_KEY, algorithms=['HS256'])
        user_ban = session.query(ban_user).filter(ban_user.mail == users['mail'])
        for j in user_ban:
            day_code = str(j.date_ban).split(" ")
            date = datetime.datetime(int(day_code[0].split("-")[0]), int(day_code[0].split("-")[1]),
                                     int(day_code[0].split("-")[2]),
                                     int(day_code[1].split(":")[0]), int(day_code[1].split(":")[1]),
                                     int(day_code[1].split(":")[2]))
            if date + datetime.timedelta(hours=int(str(j.ban_realt.time).split(":")[0]),
                                         minutes=int(str(j.ban_realt.time).split(":")[1])) > datetime.datetime.today():
                raise HTTPException(
                    status_code=401,
                    detail="Аккаунт заблокирован за нарушение пункта правил: {j.ban_realt.rules}. Дата разблокировки: {date + datetime.timedelta(hours=int(str(j.ban_realt.time).split(':')[0]), minutes=int(str(j.ban_realt.time).split(':')[1]))}"
                )

        raise HTTPException(
            status_code=401,
            detail="Ваш токен для авторизации не действителен"
        )
    except Exception as e:
        try:
            session.rollback()
        except:
            pass
        raise HTTPException(
            status_code=401,
            detail="Ваш токен для авторизации не действителен"
        )

