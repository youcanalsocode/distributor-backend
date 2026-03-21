from datetime import datetime, timedelta
from typing import Optional
import bcrypt
import jwt

SECRET_KEY = "distributor-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 1 week

def verify_password(plain_password: str, hashed_password: str):
    # Truncate to 72 bytes max to handle bcrypt limitations
    if isinstance(plain_password, str):
        plain_bytes = plain_password.encode('utf-8')[:72]
    else:
        plain_bytes = plain_password[:72]
        
    if isinstance(hashed_password, str):
        hash_bytes = hashed_password.encode('utf-8')
    else:
        hash_bytes = hashed_password

    try:
        return bcrypt.checkpw(plain_bytes, hash_bytes)
    except ValueError:
        return False

def get_password_hash(password: str):
    if isinstance(password, str):
        pwd_bytes = password.encode('utf-8')[:72]
    else:
        pwd_bytes = password[:72]
    
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
