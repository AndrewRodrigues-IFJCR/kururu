from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jose import jwt
from pwdlib import PasswordHash
from settings import JWTSettings

PasswordHandler = PasswordHash.recommended()


def generate_password_hash(password: str) -> str:
    return PasswordHandler.hash(password)


def verify_password(password_plain: str, password_hash: str):
    if not PasswordHandler.verify(password_plain, password_hash):
        raise Exception()


jwt_settings = JWTSettings()


def minutes_to_datetime(minutes: int):
    return datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes)


def create_access_token(account_id: int):
    return jwt.encode(
        {
            'sub': account_id,
            'exp': minutes_to_datetime(
                jwt_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
            ),
        },
        key=jwt_settings.JWT_ACCESS_TOKEN_SECRET_KEY,
    )


def create_refresh_token(account_id: int):
    return jwt.encode(
        {
            'sub': account_id,
            'exp': minutes_to_datetime(
                jwt_settings.JWT_REFRESH_TOKEN_EXPIRE_MINUTES
            ),
        },
        key=jwt_settings.JWT_REFRESH_TOKEN_SECRET_KEY,
    )
