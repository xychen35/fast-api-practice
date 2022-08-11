from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(plain_password: str, hash_password: str):
        return pwd_cxt.verify(plain_password, hash_password)