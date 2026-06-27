# 🛠️ Parameters Used with LangChain `@tool` Decorator

The `@tool` decorator in LangChain converts a normal Python function into a tool that an AI agent can call.

Basic syntax:

```python
from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    return a + b
```

---

# 1. `name`

Specifies a custom name for the tool.

Default:
The function name is used.

Example

```python
@tool("calculator")
def add(a: int, b: int):
    return a + b
```

or

```python
@tool(name="calculator")
def add(a: int, b: int):
    return a + b
```

The tool will be registered as:

```
calculator
```

instead of

```
add
```

---

# 2. `description`

Provides a description of what the tool does.

LLMs use this description to decide when to call the tool.

Example

```python
@tool(
    description="Adds two numbers together."
)
def add(a: int, b: int):
    return a + b
```

---

# 3. `return_direct`

Type

```python
bool
```

Default

```python
False
```

Purpose

If `True`, the tool's output is returned directly to the user without letting the agent continue reasoning.

Example

```python
@tool(return_direct=True)
def get_time():
    return "10:30 AM"
```

Useful for:

- Final answers
- API responses
- Database lookups

---

# 4. `args_schema`

Allows you to define structured input using a Pydantic model.

Example

```python
from pydantic import BaseModel

class AddInput(BaseModel):
    a: int
    b: int

@tool(args_schema=AddInput)
def add(a: int, b: int):
    return a + b
```

Benefits

- Input validation
- Better documentation
- Cleaner JSON inputs

---

# 5. `infer_schema`

Type

```python
bool
```

Default

```python
True
```

Automatically creates the input schema from type hints.

Example

```python
@tool(infer_schema=True)
def multiply(a: int, b: int):
    return a * b
```

Without manually writing a Pydantic model.

---

# 6. `parse_docstring`

Type

```python
bool
```

Default

```python
False
```

If enabled, LangChain reads the function's docstring and extracts:

- Description
- Parameter descriptions

Example

```python
@tool(parse_docstring=True)
def add(a: int, b: int):
    """
    Adds two integers.

    Args:
        a: First number
        b: Second number
    """
    return a + b
```

---

# 7. `error_on_invalid_docstring`

Type

```python
bool
```

Default

```python
True
```

Used together with:

```python
parse_docstring=True
```

If the docstring format is incorrect:

- True → raises an error
- False → ignores the invalid docstring

---

# Complete Example

```python
from langchain_core.tools import tool
from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str

@tool(
    name="weather",
    description="Returns the current weather for a city.",
    args_schema=WeatherInput,
    return_direct=False,
    infer_schema=True,
    parse_docstring=False
)
def get_weather(city: str):
    return f"The weather in {city} is Sunny."
```

---

# Parameter Summary

| Parameter | Type | Default | Purpose |
|-----------|------|---------|---------|
| `name` | str | Function name | Custom tool name |
| `description` | str | Function docstring | Explains the tool to the LLM |
| `return_direct` | bool | False | Return output immediately |
| `args_schema` | BaseModel | None | Structured input validation |
| `infer_schema` | bool | True | Auto-generate schema from type hints |
| `parse_docstring` | bool | False | Parse Google-style docstrings |
| `error_on_invalid_docstring` | bool | True | Raise error for invalid docstrings |

---

# Best Practices

- Always use **type hints** for function parameters.
- Write clear and descriptive tool descriptions.
- Use **`args_schema`** for tools with multiple or complex inputs.
- Enable **`parse_docstring=True`** if your project follows Google-style docstrings.
- Use **`return_direct=True`** only when the tool's response should be the final answer.
- Keep tool names short, descriptive, and unique.

---

# Example of a Well-Defined Tool

```python
from langchain_core.tools import tool

@tool(
    description="Searches GitHub repositories by keyword."
)
def github_search(query: str) -> str:
    """
    Search GitHub repositories.

    Args:
        query: Search keyword.
    """
    return "Repository list..."
```

This tool is easy for both developers and AI agents to understand and use.