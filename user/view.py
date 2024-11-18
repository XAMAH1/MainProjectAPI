from fastapi import APIRouter, Depends

from user.logIn_user import login_user_system
from user.register import registration_new_user_system
from user.register.model.pd_respounse_model import failed_respounse_model

autohorizen = APIRouter()


@autohorizen.post("/register", response_model=failed_respounse_model, responses={
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
    return result



@autohorizen.post("/login", response_model=failed_respounse_model, responses={
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
async def register(
        result: str = Depends(login_user_system)
):
    return result