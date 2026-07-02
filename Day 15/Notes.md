# 🚀 Building an AI Chatbot with LangChain, Ollama, FastAPI & Streamlit

This guide explains how to build a complete AI chatbot using:

* **Python**
* **uv** (Package Manager)
* **LangChain**
* **Ollama**
* **FastAPI**
* **Streamlit**
* **Tools**
* **Middleware**

---

# Project Architecture

```text
User
   │
   ▼
Streamlit UI (app.py)
   │
   ▼
FastAPI (main.py)
   │
   ▼
Agent (agent.py)
   │
   ▼
LLM Model (model.py)
   │
   ▼
Ollama (Llama3, Mistral, Gemma, etc.)
```

The agent can also use:

```text
Agent
 │
 ├── Calculator Tool
 ├── Weather Tool
 ├── Search Tool
 └── Middleware
```

---

# Step 1: Initialize the Project

```bash
uv init chatbot
```

## What is `uv`?

`uv` is a modern Python package manager that is significantly faster than `pip`.

It creates a new Python project.

After running the command:

```text
chatbot/
│
├── pyproject.toml
└── .python-version
```

---

# Step 2: Install LangChain

```bash
uv add langchain
```

LangChain helps you build AI applications by connecting:

* LLMs
* Agents
* Tools
* Memory
* Prompts

without writing everything manually.

---

# Step 3: Install Ollama Support

```bash
uv add langchain-ollama
```

This installs LangChain's integration with Ollama.

Ollama allows you to run Large Language Models locally.

Examples:

* Llama 3
* Mistral
* Gemma
* DeepSeek

---

# Step 4: Install FastAPI

```bash
uv add fastapi uvicorn
```

### FastAPI

FastAPI is used to build REST APIs.

Example endpoint:

```text
http://localhost:8000/chat
```

### Uvicorn

Uvicorn runs the FastAPI application.

Without Uvicorn, your API cannot start.

---

# Step 5: Create `model.py`

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "llama3",
    model_provider="ollama",
    temperature=0.5
)
```

## Why create a separate model file?

Instead of creating the model repeatedly, we create it once and import it wherever needed.

Think of it like:

```text
Engine

↓

Used throughout the car
```

---

# Step 6: Create `agent.py`

```python
from langchain.agents import create_agent
from model import model

agent = create_agent(
    model=model,
    tools=[],
    middleware=[],
    system_prompt="You are a helpful assistant."
)
```

## What is an Agent?

A normal LLM simply answers questions.

An Agent can:

* Think
* Decide
* Use Tools
* Call APIs
* Perform Actions

Example:

User asks:

```text
What is 25 × 39?
```

The agent decides to use a calculator tool before responding.

---

## System Prompt

```python
system_prompt="You are a helpful assistant."
```

This tells the AI how it should behave.

Examples:

```text
You are a coding teacher.
```

or

```text
Always answer in Hindi.
```

---

# Step 7: Create `main.py`

```python
from fastapi import FastAPI

app = FastAPI()
```

This creates the web server.

Think of FastAPI as the waiter in a restaurant.

The waiter receives requests and delivers responses.

---

# Step 8: Create an API Endpoint

```python
@app.get("/chat/{message}")
def chat(message):
    return "Hello World"
```

Visiting:

```text
http://localhost:8000/chat/hello
```

returns:

```text
Hello World
```

---

# Step 9: Run the Server

```bash
uv run uvicorn main:app --reload
```

Explanation:

* Run `main.py`
* Find the object named `app`
* Start the server
* Restart automatically whenever code changes

---

# Step 10: Test the API

Open:

```text
http://localhost:8000/chat
```

or

```bash
curl http://localhost:8000/chat
```

Output:

```text
Hello World
```

---

# Step 11: Connect the Agent

Replace

```python
return "Hello World"
```

with

```python
return agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
)["messages"][-1].content
```

## What happens?

```text
User
   │
   ▼
FastAPI
   │
   ▼
Agent
   │
   ▼
Model
   │
   ▼
Response
```

Breaking it down:

### `agent.invoke()`

Runs the AI.

### `messages`

Stores the conversation.

### `"role": "user"`

Indicates the sender.

### `"content"`

Contains the user's message.

The model returns a list of messages.

The final response is:

```python
["messages"][-1].content
```

---

# Step 12: Install Streamlit

```bash
uv add streamlit
```

Create:

```text
app.py
```

Basic example:

```python
import streamlit as st

st.title("My AI Chatbot")
```

Result:

```text
+------------------------+
| My AI Chatbot          |
|                        |
| [Input Box]            |
+------------------------+
```

---

## Replace Random Responses

Instead of:

```python
response = random.choice([
    "Hello",
    "Hi",
    "Good Morning"
])
```

Use:

```python
response = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":prompt
            }
        ]
    }
)["messages"][-1].content
```

Now the chatbot generates AI-powered responses.

---

# Step 13: Create Tools

Create:

```text
tools.py
```

Example:

```python
from langchain.tools import tool

@tool
def calculator(expression: str):
    """Calculate a mathematical expression."""
    return str(eval(expression))
```

## What is `@tool`?

It tells LangChain:

> "This function is a tool the agent can use."

Without `@tool`, the agent treats it as a normal Python function.

Example:

User:

```text
2 + 5
```

Agent:

```text
↓

Uses Calculator Tool

↓

Returns 7
```

---

# Step 14: Register the Tool

Update `agent.py`

```python
from tools import calculator

agent = create_agent(
    model=model,
    tools=[calculator]
)
```

Now the AI can use the calculator whenever necessary.

---

# Step 15: Middleware

Create:

```text
middleware.py
```

Example:

```python
from langchain.agents.middleware import after_agent

@after_agent
def run_after_agent(self, state):
    print("Agent finished.")
```

---

## What is Middleware?

Middleware runs automatically **before** or **after** the agent.

Think of airport security:

```text
Passenger

↓

Security Check (Middleware)

↓

Board Plane (Agent)
```

---

### Before Agent

Runs before the AI.

```python
@before_agent
def check_input(self, state):
    print(state)
```

Use cases:

* Validate input
* Block harmful prompts
* Add context
* Logging

---

### After Agent

Runs after the AI responds.

```python
@after_agent
def run_after_agent(self, state):
    print("Finished")
```

Use cases:

* Save chat history
* Analytics
* Logging
* Modify responses

---

Register middleware:

```python
from middleware import run_after_agent

agent = create_agent(
    model=model,
    tools=[calculator],
    middleware=[run_after_agent]
)
```

---

# Final Project Structure

```text
chatbot/
│
├── model.py          # Initializes the LLM
├── agent.py          # Creates the AI agent
├── tools.py          # Custom tools
├── middleware.py     # Before/After hooks
├── main.py           # FastAPI backend
├── app.py            # Streamlit frontend
├── pyproject.toml
└── README.md
```

---

# Complete Workflow

```text
User
   │
   ▼
Streamlit UI
   │
   ▼
FastAPI
   │
   ▼
Agent
   │
   ├── Before Middleware
   │
   ▼
LLM Model (Ollama)
   │
   ├── Uses Tools (if required)
   │
   ▼
After Middleware
   │
   ▼
FastAPI
   │
   ▼
Streamlit UI
   │
   ▼
User receives the response
```

---

# Summary

This project follows a clean and modular architecture:

| File            | Responsibility                           |
| --------------- | ---------------------------------------- |
| `model.py`      | Initializes the LLM                      |
| `agent.py`      | Creates and manages the AI agent         |
| `tools.py`      | Defines custom tools for the agent       |
| `middleware.py` | Executes logic before or after the agent |
| `main.py`       | Provides FastAPI backend endpoints       |
| `app.py`        | Builds the Streamlit frontend            |

This modular structure is commonly used in production AI applications because it separates concerns, making the project easier to maintain, debug, and scale.
