from sqlmodel import SQLModel, Field
from typing import Optional


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    done: bool = Field(default=False)
