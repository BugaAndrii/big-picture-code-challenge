from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.core.configurations import db_settings

# Create a new SQLAlchemy engine instance
# The pool_recycle argument is set to 3600 seconds (1 hour) to prevent database timeout issues
engine = create_engine(db_settings.database_url, pool_recycle=3600)

# Create a configured "Session" class
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Create a base class for our models to inherit from
Base = declarative_base()


def get_db():
    """
    Dependency function that provides a database session.
    This function is used with FastAPI's dependency injection system.

    It yields a database session and ensures it is closed after the request is completed.

    :yield: SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        print(f"Database connected")
        yield db
    finally:
        print(f"Database disconnected")
        db.close()
