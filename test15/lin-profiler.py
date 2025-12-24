import time 
from fastapi import FastAPI, Request

app = FastAPI()

def computation(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    time.sleep(1)  # Simulate a time-consuming task
    return total

@profile
def process_data(x: int) -> int:
    return computation(x)

@app.get('/profiling')
def profiling(a: int):
    result = process_data(a)
    return {"result": result}