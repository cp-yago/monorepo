from app.repositories.base import BaseRepository
from app.models.todo import Todo


class TodoRepository(BaseRepository[Todo]):
    def __init__(self, session):
        super().__init__(Todo, session)
