from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, Union
from datetime import datetime
from ..utils.pyObject import PyObjectId


class AccountModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    balance: float = Field(...)
    user_id: str = Field(...)
    pin: str = Field(...)
    account_id: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Test Account",
                "balance": 3000,
                "user_id": "USR1",
                "pin": "1234",
            }
        }


class UpdateAccountModel(BaseModel):
    name: Optional[str]
    balance: Optional[float]
    course: Optional[str]
    pin: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Test Account",
                "balance": 3000,
                "user_id": "USR1",
                "pin": "1234",
            }
        }
