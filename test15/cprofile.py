import os
import time
import cProfile
from fastapi import FastAPI, Request
import datetime
from fastapi.responses import JSONResponse

PROFILES_DIR = "profiles"
os.makedirs(PROFILES_DIR, exist_ok=True)

app = FastAPI()


@app.middleware("http")
async def create_profile(request: Request, call_next):
    time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = request.url.path.strip("/") or "root"
    profile_name = os.path.join(PROFILES_DIR, f"profile_{path}_{time_stamp}.prof")

    profiler = cProfile.Profile()
    profiler.enable()

    response = await call_next(request)

    profiler.disable()
    profiler.dump_stats(profile_name)

    print(f"Profile saved to {profile_name}")
    return response

@app.get('/')
def home():
    return {"message": "Hello, World!"}

@app.get('/compute')
def compute():
    total = sum(range(1000000))
    return {"total": total}