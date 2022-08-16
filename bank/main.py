from sys import prefix
from fastapi import FastAPI
from .routers import account, auth, transaction
from .utils.config import settings

app = FastAPI()
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(transaction.router)


@app.get(
    "/",
)
def index():

    return {"message": f"Welcome to the {settings.APP_NAME} API"}
