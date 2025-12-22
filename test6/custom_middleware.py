from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        import time
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f'Request URL: {request.url.path}')
        print(f"Request processed in {process_time} seconds")
        response.headers["X-Process-Time"] = str(process_time)
        return response

app.add_middleware(TimerMiddleware)

@app.get("/hello")
async def hello():
    for _ in range(1000000):
        pass  # Simulate some processing
    return {"message": "Hello, World!"}