from fastapi import FastAPI

from app.routers.department import router as department_router

app = FastAPI(
    title="College Management API",
    version="1.0.0",
)

app.include_router(department_router)