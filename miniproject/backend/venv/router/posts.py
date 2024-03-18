from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import sys
sys.path.append('/Users/elif/Desktop/dolunay/miniproject/backend/venv')
import models
import schemas
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/', response_model=List[schemas.CreatePost])
def get_all_posts(db: Session = Depends(get_db)):

    post = db.query(models.Events).all()


    return  post

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreatePost])
def post_a_post(post_post:schemas.CreatePost, db:Session = Depends(get_db)):

    new_post = models.Events(**post_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]


@router.get('/{id}', response_model=schemas.CreatePost, status_code=status.HTTP_200_OK)
def get_one_post(id:int ,db:Session = Depends(get_db)):

    idv_post = db.query(models.Events).filter(models.Events.id == id).first()

    if idv_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_post

@router.delete('/{event_name}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(event_name:str, db:Session = Depends(get_db)):

    deleted_post = db.query(models.Events).filter(models.Events.event_name == event_name)


    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The event '{event_name}' you requested for does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()


@router.put('/{id}', response_model=schemas.CreatePost)
def update_post(id:int, update_post:schemas.PostBase, db:Session = Depends(get_db)):

    updated_post =  db.query(models.Events).filter(models.Events.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return  updated_post.first()
