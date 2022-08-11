from fastapi import Depends, HTTPException, status
from blog import models, schemas, database
from sqlalchemy.orm import Session
from blog.hashing import Hash


def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id: {id} is not available")
    return user