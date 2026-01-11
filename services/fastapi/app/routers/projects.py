"""Docstring для services.fastapi.app.routers.projects."""

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")


# http://localhost:1338/fastapi/api/v1/projects
@router.get("/projects")
def get_projects() -> dict:
    """_summary_.

    :return: _description_
    :rtype: dict
    """
    return {"message": "Hello from FastAPI in Docker!"}


# http://localhost:1338/fastapi/api/v1/projects/1
@router.get("/projects/{project_id}")
def get_project(project_id: int) -> dict:
    """_summary_.

    :param user_id: _description_
    :type user_id: int
    :return: _description_
    :rtype: dict
    """
    return {"project_id": project_id}
