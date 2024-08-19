from repositories.user import UserCommand
from models.migrations import User
from passlib.hash import pbkdf2_sha256
from decouple import config
import datetime
import jwt

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

async def signin(db_session, input):
    try:
        user_on_db = await UserCommand.search_by_username(db_session, User(
            username=input.username.lower()
        ))
    except Exception:
        return None

    if not Sha.verify(input.password, user_on_db.password):
        return False

    access_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=int(ACCESS_TOKEN_EXPIRATION))

    payload = {
        'sub': {
            "username": input.username,
            "user_id": user_on_db.id.hex
        },
        'exp': access_exp
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    refresh_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=int(REFRESH_TOKEN_EXPIRATION))

    payload = {
        'sub': {
            "user_id": user_on_db.id.hex
        },
        'exp': refresh_exp
    }

    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        'access_token': access_token,
        'access_exp': access_exp.isoformat(),
        'refresh_token': refresh_token,
        'refresh_exp': refresh_exp.isoformat()
    }