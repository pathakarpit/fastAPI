from time import logging
from fastapi import FastAPI, Request

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app = FastAPI()

@app.middleware("http")
async def add_timing(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    time_taken = time.time() - start_time
    logger.info(f"Request to {request.url.path} took {time_taken:.4f} seconds")
    return response

@app.get('/')
def home():
    return {"message": "Hello, World!"}

@app.get('/slow')
async def slow_endpoint():
    time.sleep(2)
    return {"message": "Slow endpoint executed"}

@app.get('/fast')
def fast_endpoint():
    return {"message": "Fast endpoint executed"}

