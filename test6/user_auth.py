from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login (username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        return {"access_token": "secrettoken", "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )   

def decode_token(token: str):
    if token == "secrettoken":
        return {"username": "admin"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)

@app.get('/profile')
def get_profile(current_user: dict = Depends(get_current_user)):
    return {"username": current_user['username'], "role": "admin"}