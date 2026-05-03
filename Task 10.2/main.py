from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from models import  User

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Ошибка валидации",
            "details": [
                {
                    "field": err["loc"][-1], 
                    "message": err["msg"]
                }
                for err in exc.errors()
            ]
        }    
    )


@app.post("/user/")
async def create_item(user: User):
    return {"message" : "User created", "user": user}