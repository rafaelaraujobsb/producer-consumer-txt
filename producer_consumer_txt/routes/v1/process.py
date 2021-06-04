from fastapi import APIRouter, Body, Path

from producer_consumer_txt.models import MODEL_ANSWER_DEFAULT, ReturnMessage
from producer_consumer_txt.models.process import ResultTask
from producer_consumer_txt.modules.utils import parse_openapi
from producer_consumer_txt.modules.process import check_status_task, format_json


route = APIRouter()


MODEL_PROCESS_DEFAULT = {
    406: ReturnMessage(status=406, message="Invalid User Input"),
    **MODEL_ANSWER_DEFAULT
}


@route.post("/", response_model=ResultTask, responses=parse_openapi(MODEL_PROCESS_DEFAULT))
def process_route_post(json: dict = Body(..., description="nested json")):
    """ Send json for validation and storage in output.txt """
    return ResultTask(status=200, message="Success", task_id=format_json(json))


@route.get("/{task_id}", response_model=ReturnMessage, responses=parse_openapi(MODEL_ANSWER_DEFAULT))
def process_check_route_get(task_id: str = Path(..., description="task request id")):
    """ Check json storage status """
    return ReturnMessage(status=200, message=check_status_task(task_id))
