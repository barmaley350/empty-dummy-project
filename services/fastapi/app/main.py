"""Docstring для services.fastapi.app.main."""

from fastapi import FastAPI

app = FastAPI(title="My FastAPI App", version="1.0.0")


@app.get("/")
def read_root() -> None:
    """_summary_.

    :return: _description_
    :rtype: _type_
    """
    return {"message": "Hello from FastAPI in Docker!"}


@app.get("/health")
def health_check() -> dict:
    """_summary_.

    :return: _description_
    :rtype: dict
    """
    return {"status": "healthy"}
