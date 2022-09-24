from fastapi import status, Response, APIRouter, Depends
from enum import Enum
from typing import Optional

from routers.blog_post import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get(
    "/all",
    summary="Gets all blogs",
    description="This API call simulates fetching all blogs",
    response_description="Returns the list of available blogs"
)
def get_blogs(page=1,
              page_size: Optional[int] = None,
              req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All {page_size} blogs on page {page}", 'req': req_parameter}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"Blog Type is {type}", 'req': req_parameter}


@router.get("/{id}")
def getBlog(id: int, response: Response, req_parameter: dict = Depends(required_functionality)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Invlid Blog Id"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with ID {id}", 'req': req_parameter}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
def get_blog_comments(
        id: int, comment_id: int, valid: bool = True, username: Optional[str] = None,
        req_parameter: dict = Depends(required_functionality)):
    """
    Simulates retrieving comments for a blog
    - **id** mandatory, id of the blog
    - **comment_id** mandatory, id of the comment
    - **valid** mandatory query string
    - **username** optional, name of the user
    """
    return {
        "message": f"Blog ID {id} and Comment ID {comment_id} valid is {valid} and username is {username}", 'req': required_functionality
    }
