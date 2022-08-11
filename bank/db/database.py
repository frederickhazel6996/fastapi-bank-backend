from ..utils.config import settings
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URL)
db = client.bank
