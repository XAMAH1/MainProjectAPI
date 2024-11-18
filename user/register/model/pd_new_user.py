from pydantic import BaseModel, EmailStr


class model_new_user(BaseModel):
    email: EmailStr
    nickname: str
    password: str
    phone: str
    first_name: str
    last_name: str