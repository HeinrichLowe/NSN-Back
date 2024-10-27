import uvicorn
from src.main.server.server import app

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
