import os
from dotenv import load_dotenv
from pathlib import Path

# Define the path to the .env file
env_path = Path(".") / ".env"

# Load environment variables from the .env file
load_dotenv(dotenv_path=env_path)


class DBSettings:
    """
    Database settings class to load and manage database configuration from environment variables.

    Attributes:
        DB_CONNECTION (str): Database connection type (e.g., mysql, postgresql).
        MYSQL_USER (str): MySQL database user.
        MYSQL_PASSWORD (str): MySQL database password.
        MYSQL_SERVER (str): MySQL database server address.
        MYSQL_PORT (int): MySQL database port.
        MYSQL_DB (str): MySQL database name.
        database_url (str): Constructed database URL for SQLAlchemy.
    """
    DB_CONNECTION: str = os.environ.get("DB_CONNECTION")
    MYSQL_USER: str = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.environ.get("MYSQL_SERVER", "localhost")
    MYSQL_PORT: str = os.environ.get("MYSQL_PORT", 3306)

    # Convert MYSQL_PORT to integer if it is a string
    if type(MYSQL_PORT) is str:
        MYSQL_PORT = int(MYSQL_PORT)

    MYSQL_DB: str = os.environ.get("MYSQL_DB")
    # Construct the database URL
    database_url = f"{DB_CONNECTION}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"


db_settings = DBSettings()
