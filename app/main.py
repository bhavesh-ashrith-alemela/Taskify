from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models.task import Task
from .routers import tasks

# Create database tables
Task.metadata.create_all(bind=engine)

app = FastAPI(
    title="Taskify API",
    description="A simple Task Management REST API built with FastAPI",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Taskify API! Visit /docs for interactive documentation."}