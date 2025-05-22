from fastapi import FastAPI, Request
from prometheus_client import Histogram, generate_latest
from starlette.responses import Response
import time

app = FastAPI()

REQUEST_TIME = Histogram('request_processing_seconds', 'Time spent processing request')

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    REQUEST_TIME.observe(process_time)
    return response

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")