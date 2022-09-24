
from fastapi import APIRouter, Depends
from exceptions import StoryException
from schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# create an article


@router.post('/new', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    if request.content.startswith('Once upon a time'):
        raise StoryException('No stories please')
    return db_article.create_article(db, request)


# get an article

@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
