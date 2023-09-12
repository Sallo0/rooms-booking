from fastapi import APIRouter, Depends, Response

from app.users.exceptions import UserAlreadyExistsException, InvalidCredentialsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.repo import UsersRepo as users_repo
from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await users_repo.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await users_repo.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserRegister):
    if not (user := await authenticate_user(user_data.email, user_data.password)):
        raise InvalidCredentialsException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token",
                        access_token,
                        httponly=True,
                        )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return {"message": "Successfully logged out"}


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    return user
