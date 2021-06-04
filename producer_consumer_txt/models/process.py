from pydantic import Field

from producer_consumer_txt.models import ReturnMessage


class ResultTask(ReturnMessage):
    task_id: str = Field(..., description="task id to check progress")

    class Config:
        schema_extra = {
            "example": {
                "status": 200,
                "message": "Success",
                "task_id": "2a688cb6-c491-11eb-9e2a-88d7f67fb67f"
            }
        }
