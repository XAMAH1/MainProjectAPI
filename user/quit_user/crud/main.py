from fastapi.params import Depends

from auth import auth
from user.quit_user.database import delete_current_token


async def quit_user(
        token: str = Depends(auth)
):
    return await delete_current_token(token)
