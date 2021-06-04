from pydantic import BaseModel, Field


class ReturnMessage(BaseModel):
    status: int = Field(..., description="request status_code")
    message: str = Field(..., description="request message")


MODEL_ANSWER_DEFAULT = {
    422: ReturnMessage(status=422, message="Invalid Parameters"),
    500: ReturnMessage(status=500, message="Internal Error"),
}
