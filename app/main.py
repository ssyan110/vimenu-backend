from fastapi import FastAPI
import os, time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from ViMenu (dev)!"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "vimenu-backend",
        "version": os.getenv("APP_VERSION", "dev"),
        "ts": int(time.time())
    }
