from app.repositories.base import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(User, session)

    def get_by_email(self, email: str) -> User | None:
        return self.get_by_field("email", email)
