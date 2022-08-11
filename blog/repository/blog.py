from fastapi import Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas, database

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id: {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id: {id} is not available"}
    return blog

def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id: {id} is not available")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return "Updated"

def destroy(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id: {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)