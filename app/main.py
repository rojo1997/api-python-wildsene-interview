"""Main module"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config

from routers import hello_name, model

from events.event_handlers import start_app_handler, stop_app_handler

with open("README.md", mode="r", encoding="utf-8") as f:
    description = f.read()

app = FastAPI(title="api-wildsene-interview", description=description)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(hello_name.router)
app.include_router(model.router)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=config("FASTAPI_PORT", cast=int, default=8080),
        log_level=config("FASTAPI_LOG_LEVEL", cast=str, default="debug"),
        workers=config("FASTAPI_WORKERS", cast=int, default=1),
    )
