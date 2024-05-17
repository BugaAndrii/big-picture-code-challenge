# Big Picture Coding Challenge - Backend - Book Library API

## Installation

*Please follow these steps to get the code running on your local machine.*

### Prerequisites

- Python 3.7+

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/BugaAndrii/big-picture-code-challenge.git
    cd big-picture-code-challenge
    ```

2. **Set Up Virtual Environment and Install Dependencies**:
    Using `requirements.txt`:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Create and Configure the `.env` File**:
    Create a file named `.env` in the root directory of your project and add the following configuration:
    ```
    DB_CONNECTION=mysql+pymysql
    MYSQL_USER=your_mysql_user
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_SERVER=localhost
    MYSQL_PORT=3306
    MYSQL_DB=your_database_name
    ```

4. **Run Database Migrations**:
    Make sure your MySQL server is running and the database specified in `MYSQL_DB` exists.
    ```bash
    python -m api.core.data_base
    ```

5. **Start the FastAPI Application**:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 6060 --reload
    ```

6. **Access the API**:
    Open your browser and go to `http://localhost:6060/docs` to see the automatically generated API documentation.

