from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

from app.config import settings
from app.users.exceptions import TokenExpiredException, AbsentTokenException, InvalidTokenException, \
    UserIsNotPresentException
from app.users.repo import UsersRepo as users_repo


def get_token(request: Request):
    if not (token := request.cookies.get("booking_access_token")):
        raise AbsentTokenException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        raise InvalidTokenException

    expire = payload.get("exp")
    if not expire or int(expire) < int(datetime.utcnow().timestamp()):
        raise TokenExpiredException

    user_id = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await users_repo.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user

# todo: add roles
# async def get_current_admin_user(user=Depends(get_current_user)):
#     if not user.role == "admin":
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
#     return user
