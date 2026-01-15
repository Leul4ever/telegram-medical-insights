from fastapi import FastAPI

app = FastAPI(title="Telegram Medical Insights API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Telegram Medical Insights API"}
