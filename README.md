# Task Management REST API

A simple REST API built using FastAPI and SQLite that supports CRUD operations for managing tasks.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Installation

1. Clone the repository:

```bash
git clone <your-github-repo-url>
```

2. Navigate to the project folder:

```bash
cd task-api
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks | Create a new task |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a task by ID |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Features

- Create, Read, Update and Delete tasks
- SQLite database integration
- JSON responses
- Input validation using Pydantic
- Error handling
- Automatic Swagger documentation