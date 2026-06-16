# Day 5 - Asyncio Task Failure Handling

## Objective

Learn how to execute multiple asynchronous tasks using Python's `asyncio` module and determine the overall result based on different success and failure conditions.

---

## Concepts Used

- `asyncio`
- `async def`
- `await`
- `asyncio.gather()`
- Concurrent Task Execution
- Success and Failure Validation

---

## Scenario 1: Four Tasks with One Failure

### Description

Execute four asynchronous tasks where one task fails while the remaining tasks succeed.

### Example Result

```python
[True, True, False, True]
```

### Observation

One task failed while three tasks completed successfully.

---

## Scenario 2: One Failure Causes Overall Failure

### Business Rule

If any one task fails, the entire operation is considered failed.

### Condition

```python
1 Failure → Overall Failure
```

### Example

```python
[True, False, True, True]
```

### Result

```text
FAILED
```

### Use Case

This approach is suitable for critical systems where every task must complete successfully.

Examples:

- Banking Transactions
- Payment Processing
- Authentication Systems

---

## Scenario 3: Three Failures Cause Overall Failure

### Business Rule

If three out of four tasks fail, the overall operation should fail.

### Condition

```python
3 Failures → Overall Failure
```

### Example

```python
[False, False, False, True]
```

### Result

```text
FAILED
```

### Observation

Only one task succeeded, which is insufficient to consider the operation successful.

---

## Scenario 4: Four Failures Treated as Success

### Business Rule

If all four tasks fail, the overall result should be marked as success.

### Condition

```python
4 Failures → SUCCESS
```

### Example

```python
[False, False, False, False]
```

### Result

```text
SUCCESS
```

### Note

This is a special business requirement and is not a common real-world implementation. It may be used in custom workflows where failure of all tasks triggers an expected fallback behavior.

---

## Scenario 5: All Four Tasks Pass

### Business Rule

If all tasks complete successfully, the overall operation is successful.

### Condition

```python
4 Successes → SUCCESS
```

### Example

```python
[True, True, True, True]
```

### Result

```text
SUCCESS
```

### Observation

This represents the ideal execution path where every task completes successfully.

---

## Summary Table

| Scenario | Task Result | Overall Status |
|-----------|-------------|---------------|
| Case 1 | 3 Success, 1 Failure | Mixed Result |
| Case 2 | 1 Failure | FAILED |
| Case 3 | 3 Failures | FAILED |
| Case 4 | 4 Failures | SUCCESS |
| Case 5 | 4 Successes | SUCCESS |

---

## Key Learnings

- Learned how to execute multiple tasks concurrently using `asyncio.gather()`.
- Understood different strategies for handling task failures.
- Implemented custom business rules based on success and failure counts.
- Practiced asynchronous programming and concurrent execution in Python.
- Explored how overall system status can be derived from individual task outcomes.

---
