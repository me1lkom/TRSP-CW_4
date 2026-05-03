from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models import CustomExceptionModel, Items, Users

app = FastAPI()

class NotFound(HTTPException):
    def __init__ (self, message: str, detail: str = "Не найдено"):
        super().__init__(status_code = 404, detail = detail)
        self.message = message

class BadRequest(HTTPException):
    def __init__ (self, message: str, detail: str = "Неверный запрос"):
        super().__init__(status_code = 400, detail = detail)
        self.message = message

@app.exception_handler(NotFound)
async def not_found_handler(request: Request, exc: NotFound) -> JSONResponse:
    error = jsonable_encoder(CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)

@app.exception_handler(BadRequest)
async def bad_request_handler(request: Request, exc: BadRequest) -> JSONResponse:
    error = jsonable_encoder(CustomExceptionModel(status_code=exc.status_code, er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)



@app.get("/items/{item_id}", response_model=Items)
async def read_item(item_id: int):
    if item_id == 3:
        raise NotFound(message="Объект не найден", detail="Не найдено");
    return Items(item_id=item_id)


@app.get("/users/{user_id}", response_model=Users)
async def read_user(user_id: int):
    if user_id < 3:
        raise BadRequest(message="ID пользователя должен быть положительный", detail="Неверный запрос");
    return Users(user_id=user_id)