from loguru import logger

from producer_consumer_txt.exceptions import InvalidUserInput
from producer_consumer_txt.modules.utils import get_request_id
from producer_consumer_txt.services.queue import celery, task_write_json_to_file


def format_json(json: dict) -> str:
    task_id = get_request_id()
    logger.info(f"[+] REQUEST ID: {task_id} - FORMAT JSON")

    if json:
        # TODO: implementação ao vivo
        pass
    else:
        logger.error(f"[+] REQUEST ID: {task_id} - JSON IS EMPTY")
        raise InvalidUserInput()

    logger.info(f"[+] REQUEST ID: {task_id} - SEND TASK TO QUEUE")
    id = task_write_json_to_file.apply_async(kwargs={"json": json}, task_id=task_id)
    logger.info(f"[+] REQUEST ID: {task_id} - RECEIVED ID TASK {task_id}")

    return str(id)


def check_status_task(task_id: str) -> str:
    logger.info(f"[+] REQUEST ID: {get_request_id()} - CHECK TASK ID {task_id}")
    return celery.AsyncResult(task_id).status.title()
