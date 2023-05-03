import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.spa.static import SPAStaticFiles
from src.router import health, state

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(state.router, prefix="/tf")
app.include_router(health.router, prefix="/health")
app.mount("/", SPAStaticFiles(directory="./ui/build", html=True), name="ui")


if __name__ == '__main__':
    uvicorn.run(app)
