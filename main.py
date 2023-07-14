from fastapi import FastAPI
from routers import instagram

app = FastAPI()

app.include_router(instagram.router)


@app.get("/")
def index():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)