# Day 4 - Synchronous and Asynchronous Programming

## Topics Covered

- Synchronous Programming
- Asynchronous Programming
- Coroutines
- Event Loop
- async and await Keywords
- asyncio Module
- sleep() Function
- gather() Function
- Concurrent Execution
- Async File Processing

---

## What is Synchronous Programming?

Synchronous programming executes tasks one after another. A task must complete before the next task starts.

### Characteristics

- Sequential execution
- Blocking in nature
- Easy to understand
- Suitable for simple applications

---

## What is Asynchronous Programming?

Asynchronous programming allows tasks to pause while waiting and enables other tasks to execute during that time.

### Characteristics

- Non-blocking execution
- Efficient for I/O-bound operations
- Improves resource utilization
- Uses an Event Loop

---

## Synchronous vs Asynchronous

| Synchronous | Asynchronous |
|------------|-------------|
| Sequential execution | Concurrent execution |
| Blocking | Non-blocking |
| Simpler implementation | Better performance for I/O operations |
| Waits for task completion | Uses waiting time efficiently |

---

## Coroutine

A coroutine is a special function created using `async def` that can pause and resume execution.

Example:

```python
async def greet():
    print("Hello")
```

---

## async Keyword

The `async` keyword is used to define a coroutine.

```python
async def task():
    pass
```

---

## await Keyword

The `await` keyword pauses the current coroutine until the awaited operation completes.

```python
await sleep(3)
```

---

## Event Loop

The Event Loop manages and schedules asynchronous tasks. It switches between coroutines whenever a task is waiting.

---

## asyncio.run()

Used to start the Event Loop and execute the main coroutine.

```python
from asyncio import run

run(main())
```

---

## sleep()

`asyncio.sleep()` creates a non-blocking delay.

```python
await sleep(3)
```

Unlike `time.sleep()`, it does not block the entire program.

---

## gather()

The `gather()` function executes multiple coroutines concurrently.

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

---

## Concurrent File Processing

Multiple files can be processed using separate coroutines and executed concurrently using `gather()`.

Example Structure:

```python
from asyncio import run, gather

async def task1():
    pass

async def task2():
    pass

async def task3():
    pass

async def main():
    await gather(
        task1(),
        task2(),
        task3()
    )

run(main())
```

---

## Key Learnings

- Learned the difference between synchronous and asynchronous programming.
- Understood coroutines and the Event Loop.
- Used async and await keywords.
- Executed multiple tasks concurrently using gather().
- Implemented asynchronous file processing.

---

## Technologies Used

- Python 3
- Asyncio
- VS Code
- Ubuntu (WSL)
- Git & GitHub

---

Industrial Training 2026 | Agentic AI
