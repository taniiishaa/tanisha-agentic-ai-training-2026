# CodeNoids Full-Stack AI Chat Assistant

A modern, full-stack AI conversational platform featuring a decoupled architecture: a **Vite React** frontend, a scalable **FastAPI** backend middleware routing layer, and locally managed LLMs running via **Ollama**.

---

## 🏗️ Project Architecture

The platform separates user interaction, API routing, and AI processing into three distinct layers:

```text
[ React Frontend ]            [ FastAPI Backend ]            [ Local AI Engine ]
(http://localhost:5173)  -->  (http://127.0.0.1:8000)  -->  (Ollama via Port 11434)
```

### Architecture Overview

1. **Frontend (`my-app`)**

   * Built using React + Vite.
   * Handles user interactions and UI rendering.
   * Maintains chat history and state management.
   * Sends API requests to FastAPI backend.

2. **Backend (`my-backend`)**

   * Built using FastAPI.
   * Acts as a middleware between frontend and AI models.
   * Handles CORS policies.
   * Processes incoming chat requests and forwards them to Ollama.

3. **AI Engine (`Ollama`)**

   * Runs locally on the system.
   * Hosts open-source LLMs.
   * Generates responses based on user prompts.
   * Supports multiple models and easy switching.

---

## 🛠️ Installation & Setup Blueprint

### Prerequisites

Before starting, ensure the following are installed:

* Python 3.10+
* Node.js 18+
* npm
* Git
* Ollama
* uv package manager

---

## 1️⃣ Frontend Setup

Create and run the React application:

```bash
npm create vite@latest my-app
cd my-app

npm install
npm run dev
```

Default frontend URL:

```text
http://localhost:5173
```

---

## 2️⃣ Backend Setup

Navigate out of your frontend workspace to create a standalone backend layer:

```bash
cd ~
mkdir my-backend
cd my-backend
```

Install required dependencies:

```bash
uv pip install fastapi uvicorn langchain langchain-community requests
```
---

## 3️⃣ Running the Backend

Start the FastAPI server:

```bash
cd ~/my-backend

uv run uvicorn main:app --reload
```

Backend endpoint:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Ollama Setup

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify installation:

```bash
ollama --version
```

Pull a model:

```bash
ollama pull llama3.2
```

Run the model:

```bash
ollama run llama3.2
```

Ollama default port:

```text
http://127.0.0.1:11434
```

---

# 🚧 Challenges Faced & Resolutions (Error Diary)

## 1. The FastAPI "Could Not Import Module" Crash

### Error

```text
ERROR: Error loading ASGI app. Could not import module "main.py".
```

### Cause

Uvicorn expects module names, not file names.

### Wrong

```bash
uvicorn main.py:app
```

### Correct

```bash
uv run uvicorn main:app --reload
```

---

## 2. The FastAPI "Attribute app Not Found" Bug

### Error

```text
ERROR: Error loading ASGI app.
Attribute "app" not found in module "main"
```

### Cause

Running the command from the wrong directory.

### Solution

```bash
cd ~/my-backend

uv run uvicorn main:app --reload
```

---

## 3. The Local LLM Connection Interruption (EOF)

### Error

```text
Error: Post "http://127.0.0.1:11434/api/generate": EOF
```

### Cause

Large models exhausted available resources.

### Solution

Use lightweight models:

```bash
ollama pull llama3.2
```

or

```bash
ollama pull qwen2.5:0.5b
```

---

## 4. The Real-Time Chat Disappearing Act

### Error

User messages disappeared after clearing the input box.

### Cause

Messages were directly linked to the current input state.

### Solution

Store messages in a dedicated chat history array:

```javascript
const [messages, setMessages] = useState([]);
```

This keeps conversations persistent even when inputs are cleared.

---

## 5. The Browser CORS Block

### Error

```text
Access to fetch at 'http://127.0.0.1:8000/chat'
from origin 'http://localhost:5173'
has been blocked by CORS policy
```

### Cause

Frontend and backend operate on different ports.

### Solution

Configure CORSMiddleware:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# 🔄 Request Flow

The following sequence occurs whenever a user sends a message:

```text
User
 ↓
React Frontend
 ↓
POST /chat
 ↓
FastAPI Backend
 ↓
Ollama API
 ↓
LLM Response
 ↓
FastAPI
 ↓
React UI
 ↓
Displayed to User
```

---

# 🧰 Technology Stack

| Layer         | Technology   |
| ------------- | ------------ |
| Frontend      | React        |
| Build Tool    | Vite         |
| Styling       | Tailwind CSS |
| Backend       | FastAPI      |
| Server        | Uvicorn      |
| AI Runtime    | Ollama       |
| Language      | Python       |
| API Format    | REST         |
| Data Exchange | JSON         |

---

# 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* Full-Stack Development
* REST API Design
* FastAPI Fundamentals
* React State Management
* Cross-Origin Communication (CORS)
* Local LLM Deployment
* Prompt Engineering Basics
* Frontend-Backend Integration
* Debugging Production Errors
* Modern AI Application Architecture

---

# 📜 Conclusion

CodeNoids Full-Stack AI Chat Assistant demonstrates how modern AI applications can be built using a modular architecture. By combining React, FastAPI, and Ollama, the project achieves a scalable, locally hosted conversational platform that remains lightweight, secure, and extensible for future AI-powered enhancements.

This project serves as an excellent foundation for advanced AI systems involving memory, agents, vector databases, Retrieval-Augmented Generation (RAG), and multi-model orchestration.
