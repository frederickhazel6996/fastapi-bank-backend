from distutils.log import error
from fastapi import APIRouter
from typing import List
from fastapi import status, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ..schemas import user, token
from ..db.database import db
from fastapi.security import OAuth2PasswordRequestForm
from ..utils.hash import verify_hash, encrypt_password
from ..utils.jwt import create_access_token
from random_username.generate import generate_username
from fastapi.security import OAuth2PasswordRequestForm
import uuid


router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
async def register_user(request: user.UserRequestModel):

    temp_user_id = f"user{uuid.uuid1()}"
    _username = generate_username()
    temp_username = f"${_username[0]}"

    try:
        if (await db["users"].find_one({"email": request.email})) is None:
            new_user = user.AddUserModel(
                password=encrypt_password(request.password),
                email=request.email.lower(),
                user_id=temp_user_id,
                username=temp_username,
            )

            db_user = jsonable_encoder(new_user)
            await db["users"].insert_one(db_user)
            access_token = create_access_token(data={"username": temp_username})
            return {
                "access_token": access_token,
                "token_type": "bearer",
                "id": temp_user_id,
            }

        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "failed",
                "details": f"user with email {request.email} exists",
                "status_code": 409,
            },
        )

    except:
        raise HTTPException(status_code=500, detail=f"Internal Server Error")


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
)
async def login_user(request: OAuth2PasswordRequestForm = Depends()):

    try:
        if (
            user := await db["users"].find_one({"email": request.username.lower()})
        ) is not None:
            if not verify_hash(user["password"], request.password):
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "message": "failed",
                        "details": f"Incorrect Username or Password",
                        "status_code": 404,
                    },
                )
            access_token = create_access_token(data={"username": user["username"]})
            return {
                "access_token": access_token,
                "token_type": "bearer",
                "user_id": user["user_id"],
                "username": user["username"],
            }
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": "failed",
                "details": f"Incorrect Username or Password",
                "status_code": 404,
            },
        )

    except:

        raise HTTPException(status_code=500, detail=f"Internal Server Error")
