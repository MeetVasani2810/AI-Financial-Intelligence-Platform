from fastapi import FastAPI
from api.routes import router
app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"AI Financial Copilot API Running"
    }
app.include_router(router)