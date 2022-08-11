from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt_password(password: str):
    hashedPassword = pwd_context.hash(password)
    return hashedPassword


def verify_hash(hashed_password, plain_password):
    return pwd_context.verify(plain_password, hashed_password)
