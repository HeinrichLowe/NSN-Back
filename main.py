import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.http.routes import UserRoute, PostRoute

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router=UserRoute)
app.include_router(router=PostRoute)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
