from base64 import b64encode
from datetime import datetime, timedelta
from secrets import token_bytes

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.repo import UsersRepo as users_repo

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await users_repo.find_one_or_none(email=email)
    if user and verify_password(password, user.hashed_password):
        return user


# TODO: add refresh token

def get_secret_key() -> str:
    return b64encode(token_bytes(32)).decode()


if __name__ == '__main__':
    print(get_secret_key())
