from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..oauth2 import get_current_user
from ..repository import user


router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=List[schemas.User], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.get_all(db=db)


@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.create(request=request, db=db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db),current_user:schemas.User= Depends(get_current_user)):
    return user.get_user(id=id, db=db)
