from pydantic import BaseModel


class device_model(BaseModel):
    user_ip: str
    user_device: str