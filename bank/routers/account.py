# Body parameters
from fastapi import APIRouter
from typing import List, Optional
from fastapi import Depends, status, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from ..db import database
from ..schemas import account
from ..db.database import db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/account",
    tags=["Accounts"],
)


@router.post(
    "/account",
    status_code=status.HTTP_201_CREATED,
)
async def create_account(request: account.AccountModel):
    account = jsonable_encoder(request)
    await db["accounts"].insert_one(account)
    return {"message": "Account created"}


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[account.AccountModel]
)
async def get_accounts():
    accounts = await db["accounts"].find().to_list(1000)
    return accounts
