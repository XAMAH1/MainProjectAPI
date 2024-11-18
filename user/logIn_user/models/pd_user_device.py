from pydantic import BaseModel


class model_device(BaseModel):
    user_ip: str
    user_device: str