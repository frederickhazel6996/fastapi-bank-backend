# Body parameters
from fastapi import APIRouter
from typing import List, Optional
from fastapi import Depends, status, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ..db import database
from ..schemas import account
from ..db.database import db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/account",
    tags=["Accounts"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_account(request: account.AccountModel):
    try:
        account = jsonable_encoder(request)
        await db["accounts"].insert_one(account)
        return {"message": "Account created"}
    except:
        raise HTTPException(status_code=500, detail=f"Error")


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=account.AccountModel
)
async def get_account(id: str):
    if (account := await db["accounts"].find_one({"account_id": id})) is not None:
        return account
    raise HTTPException(status_code=404, detail=f"Account {id} not found")


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[account.AccountModel]
)
async def get_accounts():
    accounts = await db["accounts"].find().to_list(1000)
    return accounts


@router.put(
    "/update-account/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_account(id: str, request: account.UpdateAccountModel):
    account = jsonable_encoder(request)
    update_result = await db["accounts"].update_one(
        {"account_id": id}, {"$set": account}
    )
    if update_result.modified_count != 1:
        raise HTTPException(status_code=404, detail=f"Account {id} not found")
    return {"message": "Account Updated"}


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_account(id: str):
    delete_result = await db["accounts"].delete_one({"account_id": id})

    if delete_result.deleted_count != 1:
        raise HTTPException(status_code=404, detail=f"Student {id} not found")
    return {"message": "Account Deleted"}
