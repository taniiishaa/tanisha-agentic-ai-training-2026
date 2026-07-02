# 🚀 FastMCP Guide


# What is MCP?

**MCP** stands for **Model Context Protocol**.

It is an open standard that allows AI models to communicate with external applications in a structured way.

Instead of every AI application creating its own custom API, MCP provides one common protocol.

Think of MCP like:

```text
USB for AI Applications
```

Just as USB allows different devices to connect to a computer,

MCP allows different AI applications to connect to tools and services.

---

# Why was MCP Created?

Imagine you have:

* Calculator
* Database
* Weather API
* Email Service
* File System

Without MCP:

```text
ChatGPT  ---- Custom API ---- Calculator

Claude ---- Another API ---- Calculator

Gemini ---- Another API ---- Calculator
```

Every AI needs a different integration.

This creates lots of duplicate work.

---

With MCP:

```text
ChatGPT
       │
Claude │
       │
Gemini │
       ▼
   MCP Server
       │
 ┌─────┼─────┐
 │     │     │
 ▼     ▼     ▼
Calculator Database Weather
```

One protocol.

Multiple AI clients.

---

# What is FastMCP?

FastMCP is a Python framework for building MCP servers easily.

Think of it as:

```text
FastAPI

↓

For Web APIs

-------------------

FastMCP

↓

For MCP Servers
```

It hides all the complex MCP protocol details.

You only write Python functions.

---

# Install FastMCP

Using uv:

```bash
uv add fastmcp
```

Or using pip:

```bash
pip install fastmcp
```

---

# Create Your First Server

Create:

```text
server.py
```

Example:

```python
from fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")
```

## What happened?

You created an MCP server named:

```text
My First MCP Server
```

Think of it like:

```text
app = FastAPI()
```

But instead:

```text
mcp = FastMCP()
```

---

# Running the Server

```python
mcp.run()
```

Complete file:

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo Server")

mcp.run()
```

Run:

```bash
python server.py
```

The MCP server is now ready for clients to connect.

---

# What are Tools?

A Tool is something the AI can execute.

Examples:

* Calculator
* Weather
* Search
* Database Query
* File Reader

User:

```text
What is 45 × 89?
```

Instead of guessing,

the AI calls a calculator tool.

---

# Creating a Tool

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b
```

---

## What does `@mcp.tool()` do?

It tells FastMCP:

> "This function is available for AI models."

Without it,

the function is just a normal Python function.

---

Example:

User asks:

```text
Add 15 and 25
```

AI

↓

Calls

```python
add(15,25)
```

↓

Returns

```text
40
```

---

# Multiple Tools

```python
@mcp.tool()
def subtract(a: int, b: int):
    return a - b

@mcp.tool()
def multiply(a: int, b: int):
    return a * b

@mcp.tool()
def divide(a: int, b: int):
    return a / b
```

Now the AI has four tools.

---

# What are Resources?

Resources are information that AI can read.

Unlike tools,

resources do **not** perform actions.

They simply provide data.

Examples:

* Company Policy
* Employee Handbook
* README
* Product Catalog
* FAQ

---

Creating a Resource

```python
@mcp.resource("company://policy")
def company_policy():
    return """
Employees must wear ID cards.
Office timing: 9 AM - 6 PM.
"""
```

When AI needs company rules,

it reads this resource.

---

Think of it like:

```text
Book

↓

AI opens it

↓

Reads information
```

---

# What are Prompts?

Prompts are reusable instructions.

Instead of writing long prompts repeatedly,

create them once.

Example:

```python
@mcp.prompt()
def coding_helper():
    return "You are an expert Python developer."
```

Whenever used,

the AI receives this instruction.

---

Example

Without Prompt:

```text
You are an expert Python developer...
Explain recursion...
```

With Prompt:

```text
Use coding_helper prompt

↓

Explain recursion
```

Cleaner and reusable.

---

# Complete Example

```python
from fastmcp import FastMCP

mcp = FastMCP("Calculator Server")

@mcp.tool()
def add(a: int, b: int):
    """Add two numbers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b

@mcp.resource("company://policy")
def policy():
    return "Office timing is 9 AM to 6 PM."

@mcp.prompt()
def helper():
    return "You are a helpful assistant."

mcp.run()
```

---

# How Everything Works

```text
User
   │
   ▼
AI Client
(ChatGPT / Claude Desktop / Cursor)
   │
   ▼
MCP Protocol
   │
   ▼
FastMCP Server
   │
   ├──────────────┐
   │              │
   ▼              ▼
Tools         Resources
   │              │
   └──────┬───────┘
          ▼
      AI Response
```

---

# Difference Between Tools, Resources and Prompts

| Feature             | Tool | Resource | Prompt |
| ------------------- | ---- | -------- | ------ |
| Performs actions    | ✅    | ❌        | ❌      |
| Returns information | ✅    | ✅        | ✅      |
| Can modify data     | ✅    | ❌        | ❌      |
| Reusable            | ✅    | ✅        | ✅      |
| Used by AI          | ✅    | ✅        | ✅      |

---

# Typical Workflow

```text
User

↓

AI receives request

↓

AI decides

↓

Need information?

↓

Read Resource

OR

Need to perform an action?

↓

Call Tool

↓

Receive result

↓

Generate final response

↓

Return answer to user
```

---


FastMCP makes it easy to build MCP servers by allowing you to expose Python functions as tools, share information through resources, and define reusable prompts. It hides the complexity of the Model Context Protocol, enabling you to focus on building useful AI capabilities instead of implementing the protocol itself.

As AI applications increasingly adopt MCP, FastMCP provides a clean, modular, and scalable way to create services that can be used by multiple AI clients such as Claude Desktop, Cursor, and other MCP-compatible applications.
