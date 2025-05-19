from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session):
        self.model = model
        self.session = session

    def get(self, id: int) -> Optional[ModelType]:
        return self.session.get(self.model, id)

    def get_by_field(self, field: str, value: any) -> Optional[ModelType]:
        statement = select(self.model).where(getattr(self.model, field) == value)
        return self.session.exec(statement).first()

    def list(self, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        return self.session.exec(statement).all()

    def create(self, data: dict) -> ModelType:
        db_obj = self.model(**data)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def update(self, db_obj: ModelType, data: dict) -> ModelType:
        for field, value in data.items():
            setattr(db_obj, field, value)
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> Optional[ModelType]:
        db_obj = self.get(id)
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
        return db_obj

    def exists(self, id: int) -> bool:
        statement = select(self.model).where(self.model.id == id)
        return self.session.exec(statement).first() is not None
