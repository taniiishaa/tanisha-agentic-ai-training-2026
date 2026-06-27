# 🎁 Wrapper Functions in Python

## 📖 What is a Wrapper Function?

A **wrapper function** is a function that **wraps around another function**, allowing you to execute additional code **before**, **after**, or **around** the original function without modifying its implementation.

Wrapper functions are most commonly used with **decorators**.

---

# Why Do We Need Wrapper Functions?

Wrapper functions help us:

- Add logging
- Measure execution time
- Validate input
- Handle exceptions
- Authenticate users
- Modify outputs
- Register tools
- Reuse common functionality

Instead of rewriting the same code in multiple functions, we write it once inside a wrapper.

---

# Basic Structure

```python
def wrapper():
    print("Before")

    # Original function executes here

    print("After")
```

The wrapper surrounds the original function.

---

# Example Without Wrapper

```python
def greet():
    print("Hello!")
```

Output

```
Hello!
```

---

# Example With Wrapper

```python
def wrapper(func):

    def inner():
        print("Before execution")

        func()

        print("After execution")

    return inner
```

Applying it:

```python
def greet():
    print("Hello!")

greet = wrapper(greet)

greet()
```

Output

```
Before execution
Hello!
After execution
```

---

# Wrapper Using Decorators

Instead of manually wrapping functions, Python provides decorators.

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper
```

Usage

```python
@decorator
def greet():
    print("Hello!")

greet()
```

Output

```
Before
Hello!
After
```

---

# Wrapper with Arguments

A wrapper should be able to work with any function, regardless of its parameters.

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper
```

Usage

```python
@decorator
def add(a, b):
    return a + b

print(add(5, 7))
```

Output

```
Before
After
12
```

---

# Understanding `*args` and `**kwargs`

### `*args`

Collects all positional arguments into a tuple.

Example

```python
def func(*args):
    print(args)

func(1, 2, 3)
```

Output

```
(1, 2, 3)
```

---

### `**kwargs`

Collects all keyword arguments into a dictionary.

Example

```python
def func(**kwargs):
    print(kwargs)

func(name="Tanisha", age=20)
```

Output

```
{'name': 'Tanisha', 'age': 20}
```

---

# Why Use `*args` and `**kwargs`?

Without them:

```python
def wrapper():
    func()
```

This only works for functions with **no parameters**.

With them:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

The wrapper can handle **any function**, regardless of the number or type of arguments.

---

# Returning the Result

A wrapper should return the original function's result.

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return wrapper
```

Otherwise, the decorated function may return `None`.

---

# Preserving Function Metadata

Decorators can hide the original function's name and documentation.

Example

```python
def greet():
    """Greets the user."""
    print("Hello!")
```

Without `wraps()`:

```python
print(greet.__name__)
```

Output

```
wrapper
```

The original name is lost.

---

# Using `functools.wraps`

Python provides `wraps()` to preserve metadata.

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper
```

Now,

```python
print(greet.__name__)
```

Output

```
greet
```

---

# Wrapper Flow

```
Function Called
       │
       ▼
Wrapper Starts
       │
       ▼
Code Before Execution
       │
       ▼
Original Function Executes
       │
       ▼
Code After Execution
       │
       ▼
Result Returned
```

---

# Real-Life Example: Logging

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} completed")

        return result

    return wrapper
```

Usage

```python
@logger
def square(n):
    return n * n

print(square(5))
```

Output

```
Calling square
square completed
25
```

---

# Real-Life Example: Timing a Function

```python
import time
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper
```

---

# Advantages of Wrapper Functions

- Reuse common code.
- Avoid code duplication.
- Add functionality without modifying the original function.
- Improve readability.
- Essential for decorators.
- Enable logging, timing, authentication, validation, and caching.

---

# Real-World Applications

Wrapper functions are widely used in:

- Python decorators
- Flask
- FastAPI
- Django
- LangChain
- OpenAI Agents
- CrewAI
- Logging systems
- Authentication systems
- Performance monitoring

---

# Key Points to Remember

- A **wrapper function** surrounds another function.
- It executes code before and/or after the original function.
- Wrappers are the core of Python decorators.
- `*args` and `**kwargs` make wrappers compatible with any function.
- `functools.wraps` preserves the original function's metadata.
- Wrapper functions promote reusable, modular, and maintainable code.

---

# Summary

A **wrapper function** is a function that wraps around another function to extend or modify its behavior without changing the original code. It is the foundation of Python decorators and is commonly used for logging, timing, authentication, validation, and tool registration. By using `*args`, `**kwargs`, and `functools.wraps`, wrapper functions become flexible, reusable, and suitable for real-world Python applications.