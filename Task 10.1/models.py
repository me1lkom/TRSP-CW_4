from pydantic import BaseModel

class CustomExceptionModel(BaseModel):
    status_code: int
    er_message: str
    er_details: str

class Items(BaseModel):
    item_id: int

class Users(BaseModel):
    username: str
    age: int