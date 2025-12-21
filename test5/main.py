from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_prediction
from typing import List

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Welcome to the Housing Price Prediction API!'}

@app.post('/prediction', response_model=OutputSchema)
def predict(input_data: InputSchema):
    prediction = make_prediction(input_data.model_dump())
    return OutputSchema(predicted_price=prediction)

@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(input_data: List[InputSchema]):
    predictions = make_batch_prediction([data.model_dump() for data in input_data])
    return [OutputSchema(predicted_price=pred) for pred in predictions]
    