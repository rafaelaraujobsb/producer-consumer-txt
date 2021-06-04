import time
import uuid

import urllib3
from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from producer_consumer_txt.config import envs
from producer_consumer_txt.exceptions.error_handler import load_exception_api
from producer_consumer_txt.routes import rota_v1
from producer_consumer_txt.modules.utils import _request_id_ctx_var


urllib3.disable_warnings()

# Versão
__version__ = "0.3.0"

# Logger Requisição
logger.level("REQUEST RECEIVED", no=21, color="<white>")
logger.level("REQUEST FINISHED", no=21, color="<white>")

if envs.SAVE_LOG:
    logger.add("critical.log", level="CRITICAL", retention="60 days")
    logger.add("debug.log", level="DEBUG", retention="60 days")
    logger.add("error.log", level="ERROR", retention="60 days")
    logger.add("info.log", level="INFO", retention="60 days")


app = FastAPI(
    title=envs.PROJECT_NAME,
    description=envs.PROJECT_DESC,
    version=__version__,
    docs_url="/swagger",
    redoc_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Versions Routes
app.include_router(rota_v1, prefix="/v1")

# Exceptions API
load_exception_api(app)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = str(uuid.uuid1())

    logger.log("REQUEST RECEIVED", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path}")

    request_id = _request_id_ctx_var.set(id)

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINISHED", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path} - TIME: {process_time}")

    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Request-ID"] = id

    _request_id_ctx_var.reset(request_id)

    return response
