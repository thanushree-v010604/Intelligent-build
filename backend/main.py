from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .build_manager import run_pipeline

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for project demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/run")
def run_build():
    return run_pipeline()
