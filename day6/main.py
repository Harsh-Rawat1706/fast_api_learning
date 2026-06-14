from fastapi import FastAPI

# Routers
from routers.auth import auth
from routers.students import stud
from routers.teachers import teach
from routers.courses import cours

# Middleware
from middleware.logger import log_request_time

# Create FastAPI application
app = FastAPI(
    title="College Management API",
    description="Backend API built using FastAPI",
    version="1.0.0"
)

# Register Middleware
app.middleware("http")(log_request_time)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to College Management API"
    }

# Register Routers
app.include_router(auth)
app.include_router(stud)
app.include_router(teach)
app.include_router(cours)