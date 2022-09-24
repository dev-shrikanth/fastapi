from pydantic import BaseModel
from typing import List


# Base Article schema

class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        orm_mode = True

# Base user schema


class UserBase(BaseModel):
    username: str
    email: str
    password: str

# return values for user with articles


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []

    class Config():
        orm_mode = True


# sent to create an article

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

# user schema to go with articles


class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True

# displays articles with user details


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config():
        orm_mode = True
