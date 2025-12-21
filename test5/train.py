import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('housing.csv').iloc[:,:-1].dropna()
print('reading data')

X = df.drop(columns = 'median_house_value')
y = df.median_house_value.copy()
print('splitting data')

model = LinearRegression().fit(X, y)
print('training model')

joblib.dump(model, 'model.joblib')
print('saving model')
