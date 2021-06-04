from contextvars import ContextVar


_request_id_ctx_var: ContextVar[str] = ContextVar("request_id", default=None)


def get_request_id() -> str:
    return _request_id_ctx_var.get()


def parse_openapi(answers: dict) -> dict:
    return {status: {"content": {"application/json": {"example": answer.dict()}}, "model": answer.__class__}
            for status, answer in answers.items()}
