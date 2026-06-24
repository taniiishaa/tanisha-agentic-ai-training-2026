# GitHub Assistant

An intelligent **Asynchronous GitHub Assistant** built using **Streamlit**, **LangChain**, **Ollama**, and **GitHub APIs**. The system leverages Large Language Models (LLMs) with tool-calling capabilities to fetch real-time GitHub information and provide conversational responses to user queries.

---

# 🚀 Project Overview

GitHub Assistant is an AI-powered application that enables users to interact with GitHub repositories, profiles, and related information using natural language.

Instead of manually navigating GitHub, users can ask questions such as:

* "Show details of a GitHub user."
* "Get repository information."
* "Fetch contributor details."
* "Display repository statistics."
* "Show recent activity."

The assistant automatically determines which GitHub API endpoint is required, executes the appropriate tool, and returns a human-friendly response.

---

# 🏗️ System Architecture

The application follows a modular architecture that separates the user interface, AI model logic, and API tools.

```text
                  ┌────────────────────────┐
                  │   app.py (Streamlit)   │
                  │ Frontend & Workflow    │
                  └───────────┬────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │    model.py (LLM)      │
                  │ ChatOllama + LangChain │
                  └───────────┬────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │   tools.py (HTTPX)     │
                  │ GitHub API Tool Layer  │
                  └────────────────────────┘
```

---

# 📂 Project Structure

```text
GitHub-Assistant/
│
├── app.py
├── model.py
├── tools.py
└── README.md
```

---

# 📄 Module Description

## 1. app.py

### Purpose

Acts as the frontend and orchestration layer.

### Responsibilities

* Creates the Streamlit user interface
* Accepts user queries
* Sends prompts to the LLM
* Detects tool calls
* Executes tools asynchronously
* Returns final responses

### Workflow

```text
User Query
    ↓
LLM Analysis
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
GitHub API Response
    ↓
LLM Response Generation
    ↓
User Output
```

---

## 2. model.py

### Purpose

Acts as the AI brain of the application.

### Technologies

* LangChain
* ChatOllama
* Ollama

### Responsibilities

* Initializes the local LLM
* Binds GitHub tools
* Handles tool-calling functionality
* Generates conversational responses

### Model Used

```python
qwen2.5:0.5b
```

### Tool Binding

```python
llm.bind_tools(all_github_tools)
```

This enables the model to understand which tools are available and when to use them.

---

## 3. tools.py

### Purpose

Provides GitHub-related functionality through asynchronous API calls.

### Technologies

* HTTPX
* AsyncIO
* LangChain Tools

### Responsibilities

* Fetch GitHub profile information
* Retrieve repository details
* Get contributors
* Access repository statistics
* Fetch GitHub activity data
* Process API responses

---

# ⚡ Why Asynchronous Programming?

Traditional API requests are blocking.

```python
requests.get(...)
```

The program waits until the response arrives before doing anything else.

With asynchronous programming:

```python
async def function():
    await client.get(...)
```

The application can perform other operations while waiting for GitHub's response.

---

# Benefits of Async Architecture

* Faster execution
* Better scalability
* Improved user experience
* Efficient network operations
* Reduced waiting time

---

# 🔧 Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| Streamlit  | Frontend UI               |
| LangChain  | Agent Framework           |
| Ollama     | Local LLM Runtime         |
| ChatOllama | LLM Integration           |
| HTTPX      | Async API Requests        |
| AsyncIO    | Concurrency Management    |
| GitHub API | Real-Time GitHub Data     |

---

# 🤖 Agent Workflow

The application follows a complete Agentic AI workflow.

## Step 1

User submits a question.

```text
Show details of user octocat
```

## Step 2

The LLM analyzes the request.

## Step 3

The model selects the most relevant GitHub tool.

## Step 4

The selected tool is executed asynchronously.

## Step 5

GitHub API returns live data.

## Step 6

The retrieved information is sent back to the model.

## Step 7

The model generates a natural language response.

---

# 🔄 Tool Execution Loop

A custom workflow function manages the interaction between the model and tools.

```text
User Input
    ↓
Model Invocation
    ↓
Tool Call Detection
    ↓
Tool Execution
    ↓
Data Collection
    ↓
Final Model Response
```

This ensures the LLM not only selects tools but also receives their output before generating an answer.

---

# 🌟 Key Features

### Natural Language Queries

Users can interact using plain English.

### Intelligent Tool Selection

The LLM automatically chooses the appropriate GitHub tool.

### Real-Time GitHub Data

Information is fetched directly from GitHub APIs.

### Local LLM Deployment

Runs entirely on the local machine using Ollama.

### Asynchronous Processing

Supports efficient and scalable API communication.

### Modular Architecture

Easy to maintain and extend.

---

# 🎯 Project Highlights

## Advanced Tool Routing

The model understands user intent and dynamically selects the correct tool from multiple available tools.

## Asynchronous Backend

Uses AsyncIO and HTTPX for non-blocking API communication.

## Fully Local AI System

No paid API keys required.

Everything runs locally using:

* Ollama
* LangChain
* Streamlit
* Open-source LLMs

## Agentic AI Workflow

Implements a complete reasoning → tool execution → response generation cycle.

---

# 📈 Future Enhancements

* GitHub Repository Analysis
* Pull Request Insights
* Commit History Summarization
* Code Review Assistance
* Multi-Repository Search
* GitHub Issue Tracking
* Repository Recommendation System
* Vector Database Integration
* Memory-Enabled Conversations

---

# 🎓 Learning Outcomes

Through this project, the following concepts were explored:

* Agentic AI Systems
* LangChain Tool Calling
* Local LLM Deployment
* Asynchronous Programming
* Streamlit Application Development
* API Integration
* Workflow Orchestration
* Software Architecture Design
* GitHub API Usage

---

# ✅ Conclusion

GitHub Assistant demonstrates how Large Language Models can be enhanced with external tools to perform real-world tasks. By combining Streamlit, LangChain, Ollama, AsyncIO, and GitHub APIs, the project creates a powerful AI assistant capable of retrieving live GitHub information and presenting it in a conversational format.

The project showcases modern AI engineering practices including tool calling, asynchronous workflows, local LLM deployment, and modular software architecture.
