from fastapi import FastAPI
from loguru import logger
import os

app = FastAPI(title="demo-api", version=os.getenv("APP_VERSION", "0.1.0"))

@app.get("/")
def root():
    logger.info("root hit")
    return {"app": "demo-api", "message": "Hello from FastAPI", "version": app.version}

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": app.version}
