from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(
    *, session: Session = Depends(get_session), user_create: UserCreate
) -> UserResponse:
    try:
        user_service = UserService(session)
        user = user_service.create_user(user_create)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
