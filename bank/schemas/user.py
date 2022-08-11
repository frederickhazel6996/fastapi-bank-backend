from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, Union
from datetime import datetime
from ..utils.pyObject import PyObjectId


class UserModel(BaseModel):
    class Config:
        orm_mode = True


class UserRequestModel(UserModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "Jack@gmail.com",
                "password": "1234",
            }
        }


class AddUserModel(UserModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
    user_id: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username": "JackSparrow",
                "email": "Jack@gmail.com",
                "password": "1234",
            }
        }


class LoginUserModel(UserModel):

    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "Jack@gmail.com",
                "password": "1234",
            }
        }


class UpdateAccountModel(UserModel):
    email: Optional[EmailStr]
    password: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "Jack@gmail.com",
                "password": "1234",
            }
        }
