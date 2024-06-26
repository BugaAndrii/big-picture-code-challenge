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
    DB_CONNECTION=sql_driver
    SQL_USER=your_sql_user
    SQL_PASSWORD=sql_password
    SQL_SERVER=localhost
    SQL_PORT=3306
    SQL_DB=your_database_name
    ```


4. **Start the FastAPI Application**:
    ```bash 
   uvicorn main:app --host 0.0.0.0 --port 6060 --reload
    ```

5. **Access the API**:
   Open your browser and go to `http://localhost:6060/docs` to see the automatically generated API documentation.

