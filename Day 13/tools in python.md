# 🛠️ Tools in Python

## 📖 What are Tools?

A **tool** is simply a Python function that performs a specific task and can be called by another program, user, or AI agent.

Think of a tool as a **specialized function** designed to accomplish one job.

For example:

- Add two numbers
- Search the web
- Read a file
- Get the current weather
- Send an email
- Query a database

In AI systems, tools allow the language model to perform actions beyond generating text.

---

# Why Do We Need Tools?

Large Language Models (LLMs) can generate text, but they cannot directly:

- Access the internet
- Read local files
- Perform calculations accurately
- Call APIs
- Control applications

To perform these tasks, they use **tools**.

The AI decides:

1. Which tool to use.
2. What inputs to provide.
3. Executes the tool.
4. Uses the returned result to generate a final response.

---

# Tool = A Python Function

A normal Python function can act as a tool.

Example:

```python
def add(a, b):
    return a + b
```

Calling it:

```python
print(add(5, 7))
```

Output

```
12
```

---

# Example: Weather Tool

```python
def get_weather(city):
    return f"The weather in {city} is Sunny."
```

Usage

```python
print(get_weather("Delhi"))
```

Output

```
The weather in Delhi is Sunny.
```

---

# Example: Search Tool

```python
def search(query):
    return f"Searching for '{query}'..."
```

Usage

```python
search("Python decorators")
```

Output

```
Searching for 'Python decorators'...
```

---

# Example: Calculator Tool

```python
def calculator(a, b, operation):

    if operation == "+":
        return a + b

    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b
```

Usage

```python
calculator(10, 5, "*")
```

Output

```
50
```

---

# Registering Tools

Instead of remembering every function manually, tools are often stored in a registry.

Example

```python
tool_registry = {}

tool_registry["add"] = add
tool_registry["search"] = search
tool_registry["weather"] = get_weather
```

Now tools can be accessed dynamically.

```python
tool_registry["add"](5, 10)
```

Output

```
15
```

---

# Registering Tools Automatically

Instead of manually adding functions to the registry, we can use decorators.

Example

```python
tool_registry = {}

def tool(func):
    tool_registry[func.__name__] = func
    return func
```

Usage

```python
@tool
def add(a, b):
    return a + b

@tool
def search(query):
    return f"Searching for {query}"
```

The functions are automatically registered.

---

# Tool with Metadata

Sometimes we also store information about each tool.

Example

```python
tool_registry = {}

def tool(description=""):

    def decorator(func):

        tool_registry[func.__name__] = {
            "function": func,
            "description": description
        }

        return func

    return decorator
```

Usage

```python
@tool(description="Adds two numbers")
def add(a, b):
    return a + b
```

Registry

```python
{
    "add": {
        "function": <function add>,
        "description": "Adds two numbers"
    }
}
```

---

# How AI Uses Tools

```
User Question
      │
      ▼
Language Model
      │
      ▼
Chooses Appropriate Tool
      │
      ▼
Executes Tool
      │
      ▼
Receives Result
      │
      ▼
Generates Final Response
```

---

# Real-Life Example

User asks:

> "What is 357 × 894?"

Instead of guessing,

AI calls:

```python
calculator(357, 894, "*")
```

The calculator returns:

```
319158
```

The AI then replies:

> The answer is **319,158**.

---

# Tools in AI Frameworks

Modern AI frameworks use tools extensively.

Examples include:

- **LangChain** – Wraps Python functions as tools for AI agents.
- **OpenAI Agents SDK** – Lets AI models call developer-defined tools.
- **CrewAI** – Allows multiple AI agents to collaborate using shared tools.
- **AutoGen** – Supports tool use for multi-agent workflows.
- **LlamaIndex** – Integrates tools for querying data and external systems.

---

# Common Types of Tools

| Tool Type | Example |
|-----------|---------|
| Calculator | Addition, subtraction |
| Search Tool | Search the web |
| File Tool | Read/write files |
| Weather Tool | Get weather information |
| Database Tool | Execute SQL queries |
| GitHub Tool | Search repositories |
| Email Tool | Send emails |
| Translation Tool | Translate text |
| Image Tool | Generate images |
| API Tool | Fetch data from external services |

---

# Advantages of Using Tools

- Extend AI capabilities beyond text generation.
- Enable interaction with external systems.
- Promote modular and reusable code.
- Simplify maintenance and scalability.
- Allow dynamic function selection.
- Improve accuracy for tasks like calculations and data retrieval.

---

# Key Points to Remember

- A **tool** is a Python function designed to perform a specific task.
- AI models use tools to interact with the outside world.
- Tools can access APIs, files, databases, and perform calculations.
- Tools are often registered in a **tool registry**.
- Decorators make tool registration automatic and cleaner.
- Most modern AI frameworks rely on tools to build intelligent agents.

---

# Summary

A **tool** in Python is a reusable function that performs a specific action. In AI systems, tools enable language models to go beyond text generation by interacting with external resources, performing calculations, accessing databases, calling APIs, or reading files. By organizing tools into a registry and using decorators for automatic registration, developers can build scalable, modular, and efficient AI applications.