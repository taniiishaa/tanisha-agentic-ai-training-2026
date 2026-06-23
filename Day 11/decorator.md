# Decorators in Python

## Introduction

A decorator is a special function in Python that allows us to modify or extend the behavior of another function without changing its original code.

Decorators are commonly used for:

- Logging
- Authentication and authorization
- Performance monitoring
- Input validation
- Code reusability

## What is a Decorator?

In Python, functions are treated as first-class objects, which means they can be:

- Assigned to variables
- Passed as arguments
- Returned from other functions

A decorator takes a function as input, adds some functionality, and returns a new function.

## Basic Syntax

```python
def decorator_function(original_function):
    def wrapper():
        print("Something is happening before the function is called.")
        original_function()
        print("Something is happening after the function is called.")
    return wrapper
```

## Using a Decorator

```python
def decorator_function(original_function):
    def wrapper():
        print("Before function execution")
        original_function()
        print("After function execution")
    return wrapper

@decorator_function
def greet():
    print("Hello!")

greet()
```

### Output

```text
Before function execution
Hello!
After function execution
```

## How Decorators Work

The statement:

```python
@decorator_function
def greet():
    print("Hello!")
```

is equivalent to:

```python
def greet():
    print("Hello!")

greet = decorator_function(greet)
```

## Decorator with Arguments

```python
def decorator_function(original_function):
    def wrapper(name):
        print("Before function execution")
        original_function(name)
        print("After function execution")
    return wrapper

@decorator_function
def greet(name):
    print("Hello", name)

greet("Tanisha")
```

### Output

```text
Before function execution
Hello Tanisha
After function execution
```

## Decorator with Multiple Arguments

```python
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = original_function(*args, **kwargs)
        print("Function Ended")
        return result
    return wrapper

@decorator_function
def add(a, b):
    return a + b

print(add(5, 3))
```

### Output

```text
Function Started
Function Ended
8
```

## Real-Life Example: Execution Time

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("Execution Time:", end - start)

        return result
    return wrapper

@timer
def display():
    time.sleep(2)
    print("Task Completed")

display()
```

## Advantages of Decorators

- Promotes code reusability
- Reduces code duplication
- Improves readability
- Separates core logic from additional functionality
- Easy to apply and maintain

## Common Uses of Decorators

### Logging

```python
def log(func):
    def wrapper():
        print("Function called")
        func()
    return wrapper
```

### Authentication

```python
def authenticate(func):
    def wrapper():
        print("User Verified")
        func()
    return wrapper
```

### Performance Monitoring

```python
def timer(func):
    def wrapper():
        print("Timing Function")
        func()
    return wrapper
```

## Built-in Decorators in Python

### @staticmethod

Used to define a static method inside a class.

```python
class Demo:
    @staticmethod
    def show():
        print("Static Method")
```

### @classmethod

Used to define a class method.

```python
class Demo:
    count = 0

    @classmethod
    def display(cls):
        print(cls.count)
```

### @property

Used to create getter methods.

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

## Decorator vs Function

| Feature | Function | Decorator |
|----------|----------|-----------|
| Purpose | Performs a task | Modifies another function |
| Reusability | Limited | High |
| Code Duplication | More likely | Reduced |
| Flexibility | Normal | Can extend behavior |

## Limitations

- Can make debugging more difficult.
- Nested decorators may reduce readability.
- Improper use can make code complex.

## Conclusion

Decorators are powerful Python features that allow developers to add extra functionality to existing functions without modifying their original code. They improve code reusability, maintainability, and readability, making them widely used in modern Python development and frameworks such as FastAPI, Flask, and Django.