"""Application module."""

from fastapi import FastAPI

import endpoints


def create_app() -> FastAPI:

    app = FastAPI()
    app.include_router(endpoints.router)
    return app


app = create_app()
