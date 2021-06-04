from fastapi import HTTPException


class ApiProducerConsumerText(HTTPException):
    """ Classe Base """

    def __init__(self, status_code: int, message: str, stacktrace: str = ""):
        self.message = message
        self.stacktrace = stacktrace
        self.status_code = status_code

    def __repr__(self):
        return f"\n---> Status: {self.status}\n---> Message: {self.message}\n---> Stacktrace: {self.stacktrace}"

    def __str__(self):
        return self.message


class InvalidUserInput(ApiProducerConsumerText):
    def __init__(self, message: str = "Invalid User Input", stacktrace: str = ""):
        super().__init__(status_code=406, message=message, stacktrace=stacktrace)
