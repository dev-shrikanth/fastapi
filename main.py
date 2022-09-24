from fastapi import FastAPI, Request, HTTPException
from routers import blog_get
from routers import blog_post
from routers import user
from routers import article
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get("/")
def index():
    return {"message": "Hello World 1"}


app.exception_handler(StoryException)


def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


app.exception_handler(HTTPException)


# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)
