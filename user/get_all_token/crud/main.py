from fastapi.params import Depends

from auth import auth
from database import TokenBaseModel
from user.get_all_token.database import select_all_token_user, select_token_user
from user.get_all_token.model import device_model, token_model, respounse_model


async def get_all_user_token_system(
        token: str = Depends(auth)
) -> respounse_model:
    result: list[TokenBaseModel] = await select_token_user(token)
    for current_token in result.scalars():
        result_all: list[TokenBaseModel] = await select_all_token_user(current_token.user_id)
        mass = []
        for all_token in result_all.scalars():
            print(all_token)
            mass.append(token_model(token=all_token.token, datetime=str(all_token.create_date), device=device_model(user_ip=all_token.device_real.ip_device, user_device=all_token.device_real.name)))
        return mass