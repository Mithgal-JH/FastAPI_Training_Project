from fastapi import HTTPException , status
from sqlalchemy.orm import Session
from .. import schemas, models
from ..hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=Hash.hash_password(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    users= db.query(models.User ).all()
    if not users:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"no users is available",
            
        )
    return users

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} is not available",
        )
    return user