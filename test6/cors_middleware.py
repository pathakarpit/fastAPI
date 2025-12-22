from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins_list = [
    "http://localhost",
    "http://localhost:8000",
    "http://example.com",
]

methods_list = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list,
    allow_credentials=True,
    allow_methods=methods_list,
    allow_headers=["*"],
)