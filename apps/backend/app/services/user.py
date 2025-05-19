from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user import UserRepository
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, session):
        self.repository = UserRepository(session)

    def get_user_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)

    def create_user(self, user_create: UserCreate) -> User:
        # Check if user exists
        if self.get_user_by_email(user_create.email):
            raise ValueError("Email already registered")

        # Create user data
        user_data = user_create.model_dump()
        password = user_data.pop("password")
        user_data["password_hash"] = self._get_password_hash(password)

        # Create user
        return self.repository.create(user_data)

    def update_user(self, user: User, user_update: UserUpdate) -> User:
        update_data = user_update.model_dump(exclude_unset=True)

        if "password" in update_data:
            password = update_data.pop("password")
            update_data["password_hash"] = self._get_password_hash(password)

        update_data["updated_at"] = datetime.utcnow()
        return self.repository.update(user, update_data)

    @staticmethod
    def _get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
