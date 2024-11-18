from fastapi import Depends

from user.quit_user.database import delete_token
from user.quit_user.model import model_respounse


async def quit_user_system(result: model_respounse = Depends(delete_token)) -> model_respounse:
    return result
