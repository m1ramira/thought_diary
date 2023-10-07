# Cognitive Behavior Therapy Thought Diary Service

This is a Python FastAPI application that serves as a Cognitive Behavior Therapy (CBT) Thought Diary. The application allows users to track and manage their thoughts, emotions, and behaviors as part of CBT therapy. It utilizes a PostgreSQL database to store user data securely.

## Features
* **User Authentication**:Users can create accounts, log in, and securely manage their thought diary entries.

* **Thought Diary Entries**: Users can create, read, update, and delete thought diary entries. Each entry typically includes details about the thought, associated emotions, behaviors, and cognitive distortions.

* **Emotion Tracking**: Users can track their emotions associated with each thought diary entry. Emotions can be categorized and rated.

* **(In Process) Cognitive Distortions**: The application provides predefined cognitive distortions that users can associate with their thought diary entries to help identify thought patterns.

* **(In Process) Data Visualization**: Users can view graphs and charts that summarize their thought diary data over time, helping them gain insights into their thought patterns and progress in therapy. 

## Prerequisites
Before you begin, ensure you have the following installed:

- Python (3.9+)
- PostgreSQL (9.5+)
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic

## Setup
1. Clone this repository:
```
https://github.com/m1ramira/thought_diary.git
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required Python packages:
```
pip install -r requirements.txt
```

4. Configure the database connection by modifying the config.py file. Update the PostgreSQL database URL with your credentials.
5. Create .env file in root of project. Example:
```
MODE=DEV

DB_HOST=localhost
DB_PORT=port
DB_USER=user
DB_PASS=password
DB_NAME=db_name

TEST_DB_HOST=localhost
TEST_DB_PORT=port
TEST_DB_USER=user
TEST_DB_PASS=password
TEST_DB_NAME=test_db_name

PROD_DB_HOST=localhost
PROD_DB_PORT=port
PROD_DB_USER=user
PROD_DB_PASS=password
PROD_DB_NAME=prod_db_name

SECRET_KEY=secret_key
ALGORITHM=algorith

```

6. Apply database migrations using Alembic:
```
alembic upgrade head
```

7. Start the FastAPI application:
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

8. Access the application by visiting http://localhost:8000 in your web browser.

## API Documentation
The API documentation is generated automatically and can be accessed at http://localhost:8000/docs.

## Tests
To run the test suite, use the following command:
```
pytest
```

## Acknowledgments
This project was inspired by the principles of Cognitive Behavior Therapy (CBT).
Special thanks to the FastAPI and PostgreSQL communities for their excellent tools and documentation.