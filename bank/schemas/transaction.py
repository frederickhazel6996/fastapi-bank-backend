from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, Union
from datetime import datetime
from ..utils.pyObject import PyObjectId


class CreateTransactionModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    to_account: str
    from_account: str
    to_account_type: str
    from_account_type: str
    account_id: str
    timestamp: datetime
    amount: float
    status: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "to_account": "$Bluebunny78263",
                "from_account": "$MonkeyDLuffy",
                "to_account_type": "fast-bank",
                "from_account_type": "fast-bank",
                "amount": 3000,
                "account_id": "ACC1",
                "timestamp": "2002-12-25 00:00:00-06:39",
                "status": "complete",
            }
        }


class UpdateTransactionModel(BaseModel):

    timestamp: datetime
    status: float

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "timestamp": "2002-12-25 00:00:00-06:39",
                "status": "complete",
            }
        }
