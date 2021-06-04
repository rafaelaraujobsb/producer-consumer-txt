from json import dump, load

from celery import Celery
from loguru import logger

from producer_consumer_txt import celeryconfig


celery = Celery("producer_consumer_txt")
celery.config_from_object(celeryconfig)


@celery.task(acks_late=False)
def task_write_json_to_file(json: dict):
    logger.info(f"[+] ID: {task_write_json_to_file.request.id} - PROCESSING")

    with open("/deploy/files/output.txt", "r+") as file:
        if file.read(1):
            file.seek(0)
            output = load(file)
            output.append(json)
        else:
            output = [json]

        file.seek(0)
        dump(output, file, indent=4)

    logger.info(f"[+] ID: {task_write_json_to_file.request.id} - PROCESSED")
