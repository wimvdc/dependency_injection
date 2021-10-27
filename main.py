"""Application module."""

from fastapi import FastAPI

from data.container import Container
import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()
