import uvicorn
from fastapi import FastAPI

from apis.base import api_router
from core.config import settings
from db.session import engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
create_tables()
include_router(app)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
