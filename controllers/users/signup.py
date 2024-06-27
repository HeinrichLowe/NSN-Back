import datetime
from repositories.user import UserCommand
from models.migrations import User
from passlib.hash import pbkdf2_sha256
import jwt
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
Sha = pbkdf2_sha256

async def signup(db_session, input, expires_in = 60):
    await UserCommand.register(db_session, User(
        email=input.email,
        username=input.username.lower(),
        password=Sha.hash(input.password),
        full_name=input.full_name,
        birthday=input.birthday

    ))
    exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=expires_in)

    payload = {
        'sub': input.username,
        'exp': exp
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        'token': access_token,
        'exp': exp.isoformat()
    } 