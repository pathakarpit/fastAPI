from fastapi import FastAPI

test_app = FastAPI()

@test_app.get("/")
def index():
    return {"message": "Hello, World!"}
