# 🛠️ Python Decorators for Tools

## 📖 What is a Decorator?

A **decorator** is a special function in Python that allows you to **modify or extend the behavior of another function without changing its original code**.

Decorators are commonly used for:
- Logging
- Authentication
- Timing functions
- Validation
- Registering functions as tools (used in AI agents)

A decorator is applied using the **@** symbol.

---

# Basic Syntax

```python
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
```

Applying the decorator:

```python
@decorator
def greet():
    print("Hello!")

greet()
```

### Output

```
Before function execution
Hello!
After function execution
```

---

# How Decorators Work

When Python sees:

```python
@decorator
def greet():
    print("Hello")
```

Python actually converts it into:

```python
def greet():
    print("Hello")

greet = decorator(greet)
```

So the original function is replaced with the decorated version.

---

# Why Use Decorators for Tools?

In AI applications, we often have many functions such as:

- Search
- Calculator
- Weather
- GitHub Search
- File Reader

Instead of manually storing every function, decorators can automatically register them.

Example:

```python
@tool
def search():
    ...
```

The function is automatically added to a registry.

---

# Creating a Basic Tool Decorator

```python
tool_registry = {}

def tool(func):
    tool_registry[func.__name__] = func
    return func
```

---

# Using the Decorator

```python
@tool
def add(a, b):
    return a + b

@tool
def greet(name):
    return f"Hello {name}"
```

---

# Registry Contents

```python
print(tool_registry)
```

Output:

```python
{
    "add": <function add>,
    "greet": <function greet>
}
```

---

# Calling a Tool Dynamically

```python
result = tool_registry["add"](10, 20)
print(result)
```

Output

```
30
```

---

# Tool Decorator with Description

A better approach is to store metadata.

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

---

# Using Metadata

```python
@tool(description="Adds two numbers")
def add(a, b):
    return a + b

@tool(description="Greets a user")
def greet(name):
    return f"Hello {name}"
```

---

# Registry Output

```python
{
    "add": {
        "function": <function add>,
        "description": "Adds two numbers"
    },

    "greet": {
        "function": <function greet>,
        "description": "Greets a user"
    }
}
```

---

# Executing a Tool

```python
tool_registry["add"]["function"](5, 7)
```

Output

```
12
```

---

# Decorator Using Wrapper Function

Sometimes we want to perform an action before and after a function executes.

Example:

```python
from functools import wraps

tool_registry = {}

def tool(description=""):
    def decorator(func):

        tool_registry[func.__name__] = {
            "function": func,
            "description": description
        }

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running {func.__name__}")

            result = func(*args, **kwargs)

            print(f"Result = {result}")

            return result

        return wrapper

    return decorator
```

---

# Example

```python
@tool("Multiply two numbers")
def multiply(a, b):
    return a * b

multiply(4, 6)
```

Output

```
Running multiply
Result = 24
```

---

# Decorator with Custom Name

```python
tool_registry = {}

def tool(name=None, description=""):

    def decorator(func):

        tool_name = name or func.__name__

        tool_registry[tool_name] = {
            "name": tool_name,
            "description": description,
            "function": func
        }

        return func

    return decorator
```

---

# Example

```python
@tool(
    name="calculator",
    description="Adds two numbers"
)
def add(a, b):
    return a + b
```

Registry

```python
{
    "calculator": {
        "name": "calculator",
        "description": "Adds two numbers",
        "function": <function add>
    }
}
```

---

# Understanding the Flow

```
Function Created
        │
        ▼
Decorator Applied (@tool)
        │
        ▼
Function Added to Registry
        │
        ▼
Optional Wrapper Executes
        │
        ▼
Original Function Runs
        │
        ▼
Result Returned
```

---

# Advantages of Tool Decorators

- Automatic tool registration
- Cleaner and more readable code
- Eliminates manual registration
- Stores metadata (name, description)
- Easily scalable for large projects
- Commonly used in AI frameworks

---

# Real-World Applications

Tool decorators are widely used in:

- LangChain
- OpenAI Agents
- AutoGen
- CrewAI
- FastAPI
- Flask
- Django
- Pytest

---

# Key Points to Remember

- A decorator is a function that takes another function as input.
- Decorators are applied using the **@** symbol.
- They allow extending functionality without modifying the original function.
- Tool decorators automatically register functions for later use.
- Wrappers allow adding extra behavior before and after function execution.
- `functools.wraps` preserves the original function's metadata.
- Decorators make code cleaner, modular, and reusable.

---

# Summary

Python decorators are a powerful feature that helps modify function behavior without changing the original implementation. In AI and automation projects, tool decorators are especially useful because they automatically register functions, store metadata, and make tools easy to discover and execute dynamically. This pattern is widely used in modern Python frameworks and agent-based systems.