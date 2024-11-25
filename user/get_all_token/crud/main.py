import json

import jwt
from fastapi.params import Depends

from auth import auth
from database import TokenBaseModel
from user.get_all_token.database import select_all_token_user, select_token_user
from user.get_all_token.model import device_model, token_model, respounse_model
from user.get_all_token.redis import get_redis, post_redis


async def get_all_user_token_system(
        token: str = Depends(auth)
) -> respounse_model:
    redis_result = await get_redis(token)
    if redis_result:
        return json.loads(redis_result)
    result: list[TokenBaseModel] = await select_token_user(token)
    for current_token in result.scalars():
        result_all  = await select_all_token_user(current_token.user_id)
        mass = []
        for row in result_all:
            all_token, device = row
            mass.append(token_model(token=all_token.token, datetime=str(all_token.create_date), device=device_model(user_ip=device.ip_device, user_device=device.name)))
        await post_redis(respounse_model(tokens=mass).model_dump_json(), token)
        return respounse_model(tokens=mass)