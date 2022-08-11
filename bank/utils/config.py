from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    SECRET_KEY: str
    MONGO_URL: str

    # specify .env file location as Config attribute
    class Config:
        env_file = ".env"


settings = Settings()
