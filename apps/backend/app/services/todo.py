from app.repositories.todo import TodoRepository
from app.schemas.todo import TodoResponse, TodoBase, TodoUpdate
from typing import List
from app.models.todo import Todo


class TodoService:
    def __init__(self, session):
        self.repository = TodoRepository(session)

    def create_todo(self, todo_create: TodoBase) -> TodoResponse:
        todo = todo_create.model_dump()
        return self.repository.create(todo)
    
    def update_todo(self, todo_id: str, todo_update: TodoUpdate) -> TodoResponse:
        update_data = todo_update.model_dump()
        todo = self.repository.get(todo_id)
        return self.repository.update(todo, update_data)

    def list_todos(self) -> List[TodoResponse]:
        return self.repository.list()
