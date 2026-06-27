# Codenoids 2026 Industrial Training – Agentic AI

Welcome to my Industrial Training repository for the Codenoids 2026 Agentic AI Program.This repository documents my learning journey during the Codenoids 2026 Industrial Training Program in Agentic AI.

### Day 1

#### Work Done
- Solved LeetCode #1: Two Sum
- Solved LeetCode #2: Add Two Numbers
  
### Day 2

#### Work Done
- Solved LeetCode #3: Longest Substring Without Repeating Characters
- Solved LeetCode #4: Roman to Integer

### Day 3

#### Work Done
- Solved LeetCode #5: Longest Palindromic Substring

### Day 4

#### Topics Covered
- Synchronous Programming
- Asynchronous Programming
- Event Loop
- Coroutines
- async / await
- asyncio.gather()
- Concurrent Execution

#### Work Done
- Solved LeetCode #6: Container With Most Water
- Solved LeetCode #7:Longest Common Prefix
- Asyncio Examples
- Concurrent File Processing
- Async Programming Notes

### Day 5

#### Topics Covered
- Asyncio Task Orchestration
- Failure Handling Strategies
- Concurrent Task Execution
- Business Rule-Based Result Validation

#### Implemented
- Single Task Failure Scenario
- Fail-Fast Strategy
- Multiple Failure Handling
- Success Threshold Validation
- Async Task Monitoring

### Day 6

#### Topics Covered
- Breadth-First Search (BFS)
- Queue Data Structure
- Grid Traversal
- Stack Data Structure
- Parentheses Validation Logic

#### Work Done
- Solved LeetCode #20: Valid Parentheses
- Solved LeetCode #994: Rotting Oranges
- Implemented BFS-based Solution
- Implemented Stack-based Solution
- Practiced Async and Non-Async Implementations

### Day 7

#### Topics Covered

- Python 2 vs Python 3
- Python Virtual Environments (venv)
- PIP Package Manager
- UV Package Manager
- LangChain Framework
- Ollama Local LLMs

### Day 8

#### Topics Covered

- Linked Lists
- Two-Pointer Technique
- Merging Sorted Data
- Dummy Nodes in Linked Lists
- Backtracking
- Recursion

#### Work Done 

- Solved LeetCode #21: Merge Two Sorted Lists
- Solved LeetCode #17: Letter Combinations of a Phone Number
- Implemented Linked List Merging Algorithm
- Implemented Backtracking-Based Solution

### Day 9

#### Topics Covered

- ReactJS Fundamentals
- Vite Project Setup
- Tailwind CSS Integration
- Component-Based Architecture
- Multi-Page Website Development
- Navigation and Routing
- Responsive UI Design

#### Work Done 

- React Application Setup using Vite
- Tailwind CSS Configuration
- React Router Integration
- Navigation Bar Component
- Home Page Development
- Agentic AI Page
- Marketplace Page
- Settings Page
- Chat Interface Layout
- Component-Based Folder Structure
- Responsive Layout Design

#### Technologies Used

- ReactJS
- JavaScript
- Tailwind CSS
- HTML
- CSS

### Day 10

#### Topics Covered
- FastAPI Fundamentals
- Uvicorn Fundamentals
- Portfolio Page Design

#### Implemented

- FastAPI Installation and Setup
- Uvicorn Installation and Setup
- About Me Page Development
- Professional Summary Section
- Technical Skills Section
- Education Section
- Social Links Integration
- Resume Download Button Placeholder

#### Technologies Used

- Python
- FastAPI
- Uvicorn
- ReactJS
- Tailwind CSS

 ### Day 11

#### Topics Covered

- HTTP Status Codes
- Cookies in Web Development
- Local Storage vs Session Storage
- Python Decorators
- Website Performance Optimization with Lighthouse

#### Work Done

- Studied Common HTTP Status Codes
- Learned Cookie Creation, Storage, and Usage
- Compared Local Storage and Session Storage
- Implemented Basic Python Decorators
- Explored Function Wrapping using Decorators
- Learned Lighthouse Metrics

### Day 12

#### Topics Covered

- Streamlit Fundamentals
- Streamlit UI Development
- Ollama Fundamentals
- LangChain Integration
- ChatOllama Model Configuration
- Tool Calling in LLMs
- Asynchronous Programming in Python
- AsyncIO Fundamentals
- HTTPX for Async API Requests
- GitHub API Integration
- Agentic AI Workflow
- Modular Project Architecture

#### Work Done

- Installed and Configured Streamlit
- Built Interactive Streamlit User Interface
- Set Up Ollama for Local LLM Execution
- Integrated LangChain with ChatOllama
- Developed a GitHub Assistant Project
- Created Modular Project Structure (`app.py`, `model.py`, `tools.py`)
- Implemented 20 GitHub API Tools
- Connected GitHub APIs using HTTPX
- Developed Asynchronous API Request Handling
- Implemented Tool Binding using LangChain
- Built Agent Workflow for Tool Execution
- Implemented Dynamic Tool Routing
- Created LLM-to-Tool Communication Pipeline
- Integrated Real-Time GitHub Data Fetching
- Developed Response Generation Workflow
- Tested End-to-End Assistant Functionality
- Created Project Documentation

#### Project Developed

**GitHub Assistant (Agentic AI Project)**

Features:
- Natural Language GitHub Queries
- Real-Time GitHub Data Retrieval
- Automatic Tool Selection
- Asynchronous API Calls
- Local LLM Execution using Ollama
- Streamlit-Based User Interface
- LangChain Tool Calling
- Modular and Scalable Architecture

#### Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- ChatOllama
- HTTPX
- AsyncIO
- GitHub REST API
- Markdown

### Day 13

#### Topics Covered

* LangChain Agents
* LangChain Tools
* Tool Decorators (`@tool`)
* Pydantic (`BaseModel` & `Field`)
* `args_schema` for Tool Input Validation
* Ollama Local LLM Integration
* Agent Creation with `create_agent()`
* HumanMessage and Message Passing
* Agent Invocation using `invoke()`
* Streamlit Integration
* Tool Response Metadata
* Error Handling in Tools

#### Work Done

* Built a simple AI Calculator Agent using LangChain and Streamlit.
* Created a custom **Addition Tool** using the `@tool` decorator.
* Defined structured tool inputs using **Pydantic** (`BaseModel` and `Field`).
* Implemented `args_schema` for automatic input validation.
* Connected the agent to a local **Qwen 2.5 (0.5B)** model through **Ollama**.
* Configured the agent using `create_agent()` with a custom system prompt.
* Passed user queries to the agent using `HumanMessage`.
* Executed the agent with `agent.invoke()` and session configuration (`thread_id`).
* Displayed the agent's final response in a Streamlit interface.
* Inspected and displayed response metadata, including tool calls, message type, and message ID.
* Added basic exception handling to improve tool reliability.
* Organized the project into separate modules (`app.py`, `model.py`, and `tools.py`) following a clean project structure.

```text
Codenoids-2026-Agentic-AI/
│
├── Day 1/
│   ├── TwoSum.py
│   ├── AddTwoNumbers.py
│
├── Day 2/
│   ├── LongestSubstringWithoutRepeatingCharacters.py
│   ├── RomanToInteger.py
│
├── Day 3/
│   ├── LongestPalindromicSubstring.py
│
├── Day 4/
│   ├── Asyncio.md
│   ├── async_greeting.py
│   ├── async_tasks.py
│   ├── concurrent_file_read.py
│   ├── async_results.py
│   ├── longestCommonPrefix.py
│
├── Day 5/
│   ├── 10PracticeQuestions
│       ├── 1.py
│       ├── 2.py
│       ├── 3.py
│       ├── 4.py
│       ├── 5.py
│       ├── 6.py
│       ├── 7.py
│       ├── 8.py
│       ├── 9.py
│       └── 10.py
│
│   ├── task_case_1.py
│   ├── task_case_2.py
│   ├── task_case_3.py
│   ├── task_case_4.py
│   ├── task_case_5.py
│   └── day5.md
│
├── Day 6/
│   ├── ValidParentheses.py
│   └── RottingOranges.py
│
├── Day 7/
│   ├── Python2_vs_Python3.md
│   ├── venv.md
│   ├── pip.md
│   ├── uv.md
│   ├── langchain.md
│   ├── app.py
│   ├── main.py
│   ├── quiz.py
│   └── summarizer.py
│
├── Day 8/
│   ├── letter.py
│   └── merge.py
│
├── Day 9/
│   ├── components
│       └── Header.jsx
│   ├── features
│       ├── App.css
│       ├── App.jsx
│       ├── index.css
│       └── main.jsx
│
├── Day 10/
│   ├── AboutMe.jsx
│   ├── FastAPI.md
│   ├── Uvicorn.md
│   └── main.py
│
├── Day 11/
│   ├── Cookies.md
│   ├── Decorators.md
│   ├── Lighthouse.md
│   ├── Local_Storage_vs_Session_Storage.md
│   ├── StatusCode.md
│   └── decorator.py
│
├── Day 12/
│   ├── Github Assistant
│       ├── app.py
│       ├── model.py
│       ├── tools.py
│       └── Readme.md
│   ├── Project.md
│   ├── Streamlit.md
│   ├── main.py
│   └── model.py
│
├── Day 13/
│   ├── tools
│       ├── app.py
│       ├── model.py
│       └── tools.py
│   ├── Parameters Used with LangChain.md
│   ├── Prompt Engineering.md
│   ├── decorators in python.md
│   ├── tools in python.md
│   └── wrapper.md
│
└── README.md

## Technologies Used

- Python
- Asyncio
- Data Structures & Algorithms
- LangChain
- Ollama
- Llama 3.2
- Git & GitHub
- Ubuntu (WSL)
- ReactJS
- JavaScript
- Tailwind CSS
- HTML
- CSS
- FastAPI
- Uvicorn
- Streamlit
- ChatOllama
- HTTPX
- GitHub REST API
- Markdown

```
---

*Industrial Training 2026 – Agentic AI Learning Journey*
