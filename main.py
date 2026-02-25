from fastapi import FastAPI,Request
import logging
import time

from database import Base, engine
from routers import users, products


app = FastAPI()
logging.basicConfig(level=logging.INFO)


# Create table in DB
Base.metadata.create_all(bind=engine)


#middleware->LOGGING  
@app.middleware("http")
async def middleware(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()
    process_time = end - start

    logging.info(f"{request.url.path} took {process_time} seconds")

    response.headers["X-Process-Time"] = str(process_time)

    return response


# Include routers
app.include_router(users.routers)
app.include_router(products.routers)                               
