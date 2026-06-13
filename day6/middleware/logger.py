from fastapi import FastAPI, Request
import time

async def log_request_time(request: Request, call_next):
    start_time = time.time()
    print("Incoming Request")
    print(f"Method : {request.method}")
    print(f"URL    : {request.url}")
    
    response = await call_next(request)
    
    print(f"Status : {response.status_code}")
    print("Request Completed")
    end_time = time.time()
    duration = end_time - start_time
    print(f"Request took {duration:.4f} seconds")
    return response
    