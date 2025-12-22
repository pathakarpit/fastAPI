from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JWTError, JoseError
from fastapi import HTTPException

#constant variables
SECRET_KEY = 'my_secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#funtions
def create_access_token(data: dict):
    header = {"alg": ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = data.copy()
    payload.update({"exp": expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')

def verify_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        username = claims.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Token does not contain username",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"username": username}
    except (JWTError, JoseError):
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )