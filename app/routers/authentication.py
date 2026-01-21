from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, JWTtoken
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials",
        )
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect password",
        )

    access_token = JWTtoken.create_access_token(data={"sub": user.email})

    return schemas.Token(access_token=access_token, token_type="bearer")
