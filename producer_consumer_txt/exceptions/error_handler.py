import traceback

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from producer_consumer_txt.exceptions import ApiProducerConsumerText
from producer_consumer_txt.modules.utils import get_request_id


def load_exception_api(app: FastAPI):
    """ API exception handling """

    @app.exception_handler(RequestValidationError)
    def exception_handler_validation(request: Request, exc: RequestValidationError):
        logger.error(f"[-] REQUEST ID: {get_request_id()} - {exc}")
        return JSONResponse(status_code=422, content={"status": 422, "message": "Invalid Parameters"})

    @app.exception_handler(404)
    def exception_handler_404(request: Request, exc: RequestValidationError):
        logger.error(f"[-] REQUEST ID: {get_request_id()} - Not Found")

        message = exc.message if hasattr(exc, "message") else "Not Found"

        return JSONResponse(status_code=404, content={"status": 404, "message": message})

    @app.exception_handler(500)
    def exception_handler_500(request: Request, exc: HTTPException):
        logger.critical(f"[-] REQUEST ID: {get_request_id()}"
                        f" {''.join(traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__))}")

        return JSONResponse(status_code=500, content={"status": 500, "message": "Internal Error"})

    @app.exception_handler(ApiProducerConsumerText)
    def exception_handler_api_producer_consumer_txt(request: Request, exc: ApiProducerConsumerText):
        logger.error(f"[-] REQUEST ID: {get_request_id()} - {exc}")

        return JSONResponse(status_code=exc.status_code, content={"status": exc.status_code, "message": exc.message})
