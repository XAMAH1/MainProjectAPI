from pydantic import BaseModel

from user.get_all_token.model import device_model


class token_model(BaseModel):
    token: str
    datetime: str
    device: device_model