from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.get_blog(id, db)


@router.post("/", response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request=request, db=db)


@router.put(
    "/{id}", response_model=schemas.ShowBlog, status_code=status.HTTP_202_ACCEPTED
)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id=id, request=request, db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    return blog.delete(id=id, db=db)
