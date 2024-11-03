from uuid import UUID
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, field_validator, model_validator
from src.errors.types import HttpBadRequestError

# ----------------------- Signup Schemas -----------------------
class SignupRequest(BaseModel):
    email: str | None = Field(description="email do usuario")
    username: str | None = Field(description="nome do usuario para realizar o login")
    password: str = Field(description="password do usuario para realizar o login")
    full_name: str = Field(description="nome completo (ou não) do usário")
    birth_date: datetime = Field(description="data de nascimento do usário. Ex: 01-01-1999")

    @field_validator("birth_date")
    @classmethod
    def valid_bithday(cls, raw: str | datetime) -> datetime:
        if isinstance(raw, datetime):
            return raw

        try:
            return datetime.strptime(raw, "%Y-%m-%d")
        except ValueError as exc:
            raise HttpBadRequestError("Formato de data inválido. Use YYYY-MM-DD") from exc

    @model_validator(mode='after')
    def validate_login_method(self) -> 'SignupRequest':
        if not self.email and not self.username:
            raise HttpBadRequestError("Email or username is required")

        if not self.password:
            raise HttpBadRequestError("Password is required")

        if not self.full_name:
            raise HttpBadRequestError("Name is required")

        if len(self.username) > 32:
            raise HttpBadRequestError("Username too long")

        if len(self.username) < 3:
            raise HttpBadRequestError("Username too short")

        if len(self.password) > 64:
            raise HttpBadRequestError("Password too long")

        if len(self.password) < 6:
            raise HttpBadRequestError("Password too short")

        if len(self.full_name) > 128:
            raise HttpBadRequestError("Name too long")

        return self

class SignupAttributes(BaseModel):
    id: UUID | str = Field(description="ID único do usuário")

class SignupResponse(BaseModel):
    type: str = Field(description="Tipo do objeto")
    count: int = Field(description="Quantidade de itens")
    attributes: SignupAttributes = Field(description="Atriburto de retorno do signup")


# ----------------------- Signin Schemas -----------------------
class SigninRequest(BaseModel):
    email: str | None = Field(default=None, description="User Email")
    username: str | None = Field(default=None, description="User Username")
    password: str | None = Field(description="User password")

    @model_validator(mode='after')
    def validate_login_method(self) -> 'SigninRequest':
        if not self.email and not self.username:
            raise HttpBadRequestError("Email or username is required")

        if not self.password:
            raise HttpBadRequestError("Password is required")

        return self

class SigninResponse(BaseModel):
    access_token: str = Field(description="Token de acesso")
    access_exp: str = Field(description="Tempo de duração do token de acesso")
    refresh_token: str = Field(description="Token para refresh da autenticacao")
    refresh_exp: str = Field(description="Tempo de duração do token de refresh")


# ----------------------- Get basic user info Schemas -----------------------
#class GetBasicUserInfoResponse(BaseModel):
#    token: str = Field(description="Token de autenticação")

class UserResponse(BaseModel):
    name: str = Field(description="User full name")
    avatar: str = Field(description="User Avatar")


# ----------------------- Search by name Schemas -----------------------
class SearchByNameRequest(BaseModel):
    name: str = Field(description="Nome do usuário para busca")

class SearchByNameAttributes(BaseModel):
    id: UUID | str = Field(description="ID único do usuário")
    full_name: str = Field(default=None, description="Nome completo do usuário")
    avatar: str | None = Field(default=None, description="Avatar do usuário")

class SearchByNameResponse(BaseModel):
    type: str = Field(description="Tipo do objeto")
    count: int = Field(description="Quantidade de itens")
    attributes: List[SearchByNameAttributes] = Field(description="Lista de atributos do usuário")
