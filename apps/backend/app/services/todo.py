from app.repositories.todo import TodoRepository
from app.schemas.todo import TodoResponse, TodoBase
from typing import List


class TodoService:
    def __init__(self, session):
        self.repository = TodoRepository(session)

    def create_todo(self, todo_create: TodoBase) -> TodoResponse:
        print("chegou aqui")
        todo = todo_create.model_dump()
        return self.repository.create(todo)

    def list_todos(self) -> List[TodoResponse]:
        return self.repository.list()
