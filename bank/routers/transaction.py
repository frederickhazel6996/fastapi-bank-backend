# Body parameters
from fastapi import APIRouter, Depends
from typing import List
from fastapi import status, HTTPException
from fastapi.encoders import jsonable_encoder
from ..schemas import transaction
from ..db.database import db
from ..utils.oauth2 import get_current_user


router = APIRouter(
    prefix="/api/transaction",
    tags=["Transactions"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_transaction(
    request: transaction.CreateTransactionModel,
    current_user=Depends(get_current_user),
):
    try:
        transaction = jsonable_encoder(request)
        await db["transactions"].insert_one(transaction)
        return {"message": "Transaction created"}
    except:
        raise HTTPException(status_code=500, detail=f"Error")


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=transaction.CreateTransactionModel,
)
async def get_transaction(
    id: str,
    current_user=Depends(get_current_user),
):
    if (transaction := await db["transactions"].find_one({"_id": id})) is not None:
        return transaction
    raise HTTPException(status_code=404, detail=f"Transaction {id} not found")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[transaction.CreateTransactionModel],
)
async def get_transactions(
    current_user=Depends(get_current_user),
):
    transaction = await db["transactions"].find().to_list(1000)
    return transaction


@router.put(
    "/update-transaction/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_transaction(
    id: str,
    request: transaction.UpdateTransactionModel,
    current_user=Depends(get_current_user),
):
    transaction = jsonable_encoder(request)
    update_result = await db["transactions"].update_one(
        {"_id": id}, {"$set": transaction}
    )
    if update_result.modified_count != 1:
        raise HTTPException(status_code=404, detail=f"Transaction {id} not found")
    return {"message": "Transaction Updated"}


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_transaction(
    id: str,
    current_user=Depends(get_current_user),
):
    delete_result = await db["transactions"].delete_one({"_id": id})

    if delete_result.deleted_count != 1:
        raise HTTPException(status_code=404, detail=f"Transaction {id} not found")
    return {"message": "Transaction Deleted"}
