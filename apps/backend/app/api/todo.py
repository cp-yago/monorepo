from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.todo import TodoResponse, TodoBase
from app.core.database import get_session
from app.services.todo import TodoService
from typing import List

router = APIRouter()


@router.post("/todos", response_model=TodoResponse)
def create_todo(
    *, session: Session = Depends(get_session), todo_create: TodoBase
) -> TodoResponse:
    try:
        todo_service = TodoService(session)
        todo = todo_service.create_todo(todo_create)
        return todo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/todos", response_model=List[TodoResponse])
def list_todos(*,  session: Session = Depends(get_session)) -> List[TodoResponse]:
    try:
        todo_service = TodoService(session)
        todos = todo_service.list_todos()
        return todos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))