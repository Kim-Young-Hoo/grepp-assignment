from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from starlette import status

from schemas.user import UserCreate, UserRead
from db.session import get_db
from db.repository.user import create_new_user

router = APIRouter()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
