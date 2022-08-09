from fastapi import FastAPI
from .routers import account

app = FastAPI()
app.include_router(account.router)


@app.get(
    "/",
)
def index():

    return {"message": "lmaoo"}
