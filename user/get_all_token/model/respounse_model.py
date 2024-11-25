from pydantic import BaseModel

from user.get_all_token.model import token_model


class respounse_model(BaseModel):
    tokens: list[token_model]