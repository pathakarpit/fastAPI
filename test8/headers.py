from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()

API_KEY = "my_secure_api_key"

def get_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return x_api_key

@app.get("get-data/")
async def get_data(api_key: str = Depends(get_api_key)):
    return {"data": "Here is your secured data"}