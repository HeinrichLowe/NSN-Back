from pydantic import BaseModel, Field, field_validator
from sqlalchemy import TIMESTAMP
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List

class SignupRequest(BaseModel):
    email: Optional[str] = Field(description="email do usuario")
    username: Optional[str] = Field(min_length=3, max_length=32, description="nome do usuario para realizar o login")
    password: str = Field(min_length=6, max_length=64, description="password do usuario para realizar o login")
    full_name: str = Field(max_length=128, description="nome completo (ou não) do usário")
    birthday: str = Field(description="data de nascimento do usário. Ex: 01-01-1999")

    @field_validator("birthday")
    @classmethod
    def valid_bithday(cls, raw):
        date = datetime.strptime(raw, "%Y-%m-%d")
        return date

    def check_email_or_username(self, values):
        email, username = values.get('email'), values.get('username')
        if not email and not username:
            raise ValueError("Email ou username deve ser fornecido.")
        return values

class SignupResponse(BaseModel):
    id: UUID = Field(description="id do usuario no portal")


class SigninRequest(BaseModel):
    username: str = Field(description="username do usuairo")
    password: str = Field(description="senha do usuario")

class SigninResponse(BaseModel):
    access_token: str = Field(description="Generated access token")
    exp: str = Field(description="Token expiration time")

class UserResponse(BaseModel):
    username: str = Field(description="User username")
    name: str = Field(description="User full name")
    avatar: str = Field(description="User Avatar")
    email: str = Field(description="User email")
    birthday: str = Field(description="User birthday")

"""class SigninResponse(BaseModel):
    access_token: str = Field(description="token de accesso gerado")
    refresh_token: str = Field(description="token para refresh da autenticacao")
    expires_in: int = Field(description="tempo de duração do token")"""

class AttributesSchema(BaseModel):
    id: UUID
    email: str | None
    username: str | None
    password: str
    full_name: str
    avatar: str | None

class BodySchema(BaseModel):
    type: str
    count: int
    attributes: List[AttributesSchema]
