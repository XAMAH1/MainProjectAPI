from pydantic import BaseModel, EmailStr
from .pd_user_device import model_device


class model_autme(BaseModel):
    email: EmailStr
    password: str
    device: model_device