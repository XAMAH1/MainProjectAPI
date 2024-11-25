from fastapi import APIRouter, Depends

from user.get_all_token import get_all_user_token_system
from user.logIn_user import login_user_system
from user.logIn_user.models import respounse_model as login_respounse_model
from user.quit_user.crud import quit_user_system
from user.quit_user.model import model_respounse as quit_user_respounse_model
from user.get_all_token.model import respounse_model as all_token_respounse_model
from user.register import registration_new_user_system
from user.register.model.pd_respounse_model import failed_respounse_model as register_respounse_model

autohorizen = APIRouter()


@autohorizen.post("/register", response_model=register_respounse_model, responses={
  422: {
    "description": "Bad Request",
    "content": {
      "application/json": {
        "example": {"detail": "Name is required"}
      }
    }
  }
})
async def register(
        result: str = Depends(registration_new_user_system)
):
    """
    Регистрация нового пользователя в сстеме, уникальная почта, nickname можно использовать неограничено!
    Пароль желатенльно отправлять в виде hash!
    """
    return result



@autohorizen.post("/login", response_model=login_respounse_model, responses={
  422: {
    "description": "Bad Request",
    "content": {
      "application/json": {
        "example": {"detail": "Сообщение ошибки"}
      }
    }
  },
  401: {
    "description": "Bad Request",
    "content": {
      "application/json": {
        "example": {"detail": "Ошибка авторизации"}
      }
    }
  }
})
async def login_user(
        result: str = Depends(login_user_system)
):
  """
  Авторизация пользователя в системе, можно авторизоваться только по почте!
  Пароль отправлять только в том виде, котором отправляли при регистрации!
  Девайс обязателен
  В резульате успешной авторизации ответ будет стостоять из токена, который будет обязателен в дальнейшем
  """
  return result


@autohorizen.post("/quit", response_model=quit_user_respounse_model, responses={
  422: {
    "description": "Bad Request",
    "content": {
      "application/json": {
        "example": {"detail": "Сообщение ошибки"}
      }
    }
  }
})
async def quit_user(
        result: str = Depends(quit_user_system)
):
  """
  Выход авторизованного устройства (НЕ ТОГО, С КОТОРОГО ПРОИЗВОДИТСЯ ВЫХОД)
  """
  return result



@autohorizen.get("/token/all", response_model=all_token_respounse_model, responses={
  422: {
    "description": "Bad Request",
    "content": {
      "application/json": {
        "example": {"detail": "Сообщение ошибки"}
      }
    }
  }
})
async def all_token_user(
        result: str = Depends(get_all_user_token_system)
):
  """
  Получение всех авторизованных устройств. Выводятся только последние 50 устройств
  """
  return result