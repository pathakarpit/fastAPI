from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic
    prediction = data.feature1 + data.feature2
    return {"prediction": prediction}