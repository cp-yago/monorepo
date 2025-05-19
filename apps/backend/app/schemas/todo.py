from pydantic import BaseModel


class TodoBase(BaseModel):
    description: str


class TodoResponse(TodoBase):
    id: int
    description: str
    done: bool


class TodoUpdate(BaseModel):
    id: int
    description: str
    done: bool
