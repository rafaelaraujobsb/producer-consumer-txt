import time
import uuid

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
import urllib3

from .config import envs
from .exceptions.error_handler import carregar_exception_api
from .rotas import rota_v1


urllib3.disable_warnings()

# Versão
__version__ = "0.0.1"

# Logger Requisição
logger.level("REQUEST RECEBIDA", no=21, color="<white>")
logger.level("REQUEST FINALIZADA", no=21, color="<white>")

logger.add("critico.log", level="CRITICAL", retention="60 days")
logger.add("debug.log", level="DEBUG", retention="60 days")
logger.add("error.log", level="ERROR", retention="60 days")
logger.add("info.log", level="INFO", retention="60 days")

app = FastAPI(
    title=envs.PROJETO_NOME,
    description=envs.PROJETO_DESC,
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

# Versões Rotas
app.include_router(rota_v1, prefix="/v1")

# Exceções API
carregar_exception_api(app)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = uuid.uuid1()

    logger.log("REQUEST RECEBIDA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINALIZADA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path} - TEMPO: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)

    return response
