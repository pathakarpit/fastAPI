from fastapi import FastAPI, Depends, HTTPException
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str

    class Config:
        env_file = "key.env"

settings = Settings()
app = FastAPI()

def get_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return x_api_key