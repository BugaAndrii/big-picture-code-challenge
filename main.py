import uvicorn
from fastapi import FastAPI
from api.apps.routers import apps_router
from api.components.models import Base
from api.core.data_base import engine


def include_router(server):
    """
    Include the application routers in the FastAPI server instance.

    :param server: FastAPI server instance.
    """
    server.include_router(apps_router)


def create_tables():
    """
    Create all database tables defined in the models.

    This function binds the metadata to the database engine and creates the tables.
    """
    Base.metadata.create_all(bind=engine)


def start_application():
    """
    Initialize and configure the FastAPI application.

    This function creates an instance of FastAPI, includes routers, creates tables, and returns the application instance.

    :return: Configured FastAPI application instance.
    """
    server = FastAPI(title="Big Picture Coding Challenge - Backend - Book Library", version="0.1")
    include_router(server)
    create_tables()
    return server


# Create the FastAPI application instance
app = start_application()

if __name__ == "__main__":
    # Run the FastAPI application using Uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=6060,
        log_level="info",
        reload=True
    )
