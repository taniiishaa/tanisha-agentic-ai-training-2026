# Uvicorn

Uvicorn is a lightning-fast ASGI server used to run Python web applications built with frameworks like FastAPI and Starlette.

## Features

- High performance
- Supports asynchronous applications
- Lightweight and fast
- Easy to use
- Ideal for FastAPI projects

## Installation

```bash
pip install uvicorn
```

## Basic Usage

Run a FastAPI application:

```bash
uvicorn main:app --reload
```

### Explanation

- `main` → Python file name (`main.py`)
- `app` → FastAPI application object
- `--reload` → Automatically reloads the server when code changes

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

Run:

```bash
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000
```

## Common Commands

Run with a custom port:

```bash
uvicorn main:app --port 5000
```

Run on all network interfaces:

```bash
uvicorn main:app --host 0.0.0.0
```

## Why Use Uvicorn?

- Runs FastAPI applications
- Handles incoming HTTP requests
- Supports async operations
- Provides fast performance

## Technologies Used With Uvicorn

- Python
- FastAPI
- Starlette

