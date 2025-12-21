import joblib
import numpy as np
from typing import List, Dict

saved_model = joblib.load('model.joblib')
print('model loaded')

def make_prediction(data: dict) -> float:
    features = np.array([
    [
        data['longitude'],
        data['latitude'],
        data['housing_median_age'],
        data['total_rooms'],
        data['total_bedrooms'],
        data['population'],
        data['households'],
        data['median_income']
    ]])
    prediction = saved_model.predict(features)
    return float(prediction[0])

def make_batch_prediction(data_list: List[Dict]) -> np.array:
    features = np.array([[
        x['longitude'],
        x['latitude'],
        x['housing_median_age'],
        x['total_rooms'],
        x['total_bedrooms'],
        x['population'],
        x['households'],
        x['median_income']
    ]
    for x in data_list
    ])
    predictions = saved_model.predict(features)
    return predictions