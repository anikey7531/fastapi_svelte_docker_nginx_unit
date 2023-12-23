from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    """
    A simple Hello\qwda World GET request
    """
    return {"message": "Helloo, World!"}

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)