from fastapi import Header, HTTPException, status
from datetime import datetime
from typing import Annotated
from decouple import config
import jwt

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

async def verify_token(authorization: Annotated[str, Header()]):
    try:
        payload = jwt.decode(authorization, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not validated"
        )