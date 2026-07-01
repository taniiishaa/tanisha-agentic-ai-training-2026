# LangChain Middleware - Complete Notes

Middleware in LangChain is a feature that lets you add extra functionality to an AI agent **without changing the agent's main code**. It acts as an intermediate layer that can inspect, modify, or control requests and responses as they move through the agent.

Instead of putting logging, security checks, retries, or model selection directly inside the agent, these tasks can be handled separately using middleware.

---

# Why Middleware?

Imagine building an AI assistant. Besides generating answers, you may also want to:

- Record every request
- Validate user input
- Retry failed API calls
- Block unsafe prompts
- Switch between different language models
- Cache previous responses
- Monitor tool usage

If all this logic is written inside the agent, the code becomes difficult to maintain.

Middleware keeps these responsibilities separate, making the project cleaner and easier to extend.

---

# Agent Execution Flow

A typical LangChain agent processes a request in several stages.

```text
User Input
      │
      ▼
before_agent
      │
      ▼
before_model
      │
      ▼
wrap_model_call
      │
      ▼
Language Model
      │
      ▼
after_model
      │
      ▼
Need a Tool?
   │        │
   │ No     │ Yes
   ▼        ▼
         wrap_tool_call
               │
               ▼
             Tool
               │
               ▼
after_agent
      │
      ▼
Final Response
```

Each middleware hook executes at a different point in this pipeline.

---

# Types of Middleware

LangChain mainly provides two styles of middleware:

1. Node Hooks
2. Wrap Hooks

Although both allow customization, they work differently.

---

# 1. Node Hooks

Node hooks run automatically at specific stages during execution.

They are ideal for tasks that need to happen before or after an operation.

Examples include:

- Logging
- Input validation
- Updating state
- Permission checking
- Collecting analytics

---

## Available Node Hooks

| Hook | Purpose |
|------|---------|
| `before_agent` | Runs before the agent begins execution |
| `before_model` | Runs before each model request |
| `after_model` | Runs immediately after the model responds |
| `after_agent` | Runs after the complete agent execution |

---

## Example: before_model

```python
@before_model
def validate_messages(state, runtime):

    if len(state["messages"]) > 30:
        return {"jump_to": "end"}
```

### What this does

- Checks the conversation history.
- Stops execution if the conversation becomes too long.
- Prevents unnecessary model calls.

---

## Example: after_model

```python
@after_model
def save_response(state, runtime):

    print(state["messages"][-1])
```

This hook executes after the language model returns a response.

Typical use cases:

- Save responses to a database
- Track token usage
- Create logs
- Generate analytics

---

# 2. Wrap Hooks

Wrap hooks are more flexible than node hooks.

Instead of simply running before or after an action, they wrap around the execution itself.

Conceptually:

```text
Your Middleware
       │
       ▼
handler()
       │
       ▼
Your Middleware
```

The `handler()` function represents the actual model or tool execution.

Your middleware decides:

- Whether to call it
- When to call it
- How many times to call it
- Whether to modify the request or response

---

# Example: Retry Logic

```python
@wrap_model_call
def retry_request(request, handler):

    try:
        return handler(request)

    except Exception:
        return handler(request)
```

If the first request fails, the middleware automatically tries again.

---

# Example: Selecting Different Models

Suppose an application has two models.

- Small model for simple questions
- Large model for complex questions

```python
@wrap_model_call
def choose_model(request, handler):

    if len(request.messages) > 12:
        request = request.override(model=advanced_model)

    else:
        request = request.override(model=basic_model)

    return handler(request)
```

The middleware decides which model should answer based on the conversation.

---

# Example: Monitoring Tool Calls

```python
@wrap_tool_call
def monitor_tool(request, handler):

    print("Running:", request.tool_call["name"])

    result = handler(request)

    print("Finished")

    return result
```

This records which tool was used without modifying the tool's implementation.

---

# Practical Uses of Middleware

Middleware can solve many real-world problems.

## Logging

- Store prompts
- Store responses
- Debug agent behavior

---

## Security

- Detect harmful prompts
- Block restricted requests
- Filter unsafe outputs

---

## Retry Mechanism

- Retry failed API calls
- Improve reliability during network failures

---

## Caching

- Return stored responses
- Reduce API costs
- Improve response speed

---

## Dynamic Routing

- Choose different LLMs
- Route requests based on complexity
- Optimize performance and cost

---

## Monitoring

- Track tool usage
- Measure execution time
- Record system metrics

---

# Multiple Middleware Example

```python
agent = create_agent(

    model=model,

    tools=tools,

    middleware=[

        LoggingMiddleware(),

        RetryMiddleware(),

        SafetyMiddleware(),

        DynamicModelMiddleware(),

        CacheMiddleware()

    ]
)
```

Each middleware focuses on a single responsibility.

| Middleware | Responsibility |
|------------|----------------|
| Logging | Records requests and responses |
| Retry | Handles temporary failures |
| Safety | Blocks unsafe content |
| Dynamic Model | Chooses the appropriate LLM |
| Cache | Returns stored responses when available |

This modular approach keeps the agent code clean and maintainable.

---

# Node Hooks vs Wrap Hooks

| Node Hooks | Wrap Hooks |
|------------|------------|
| Execute at predefined stages | Surround model or tool execution |
| Simpler to implement | Provide greater control |
| Best for validation and logging | Best for retries, caching, and routing |
| Cannot repeat execution | Can execute the handler multiple times |
| Mostly observe execution | Can modify execution behavior |

---

# Summary

Middleware is an important component in LangChain that allows developers to extend an agent's functionality without modifying its core logic.

### Node Hooks

- Execute at fixed points in the workflow.
- Useful for validation, logging, and state management.

### Wrap Hooks

- Surround model or tool execution.
- Allow request modification, retries, caching, routing, and response processing.

By separating these responsibilities into middleware, applications become more modular, reusable, and easier to maintain.

---

# Key Points

- Middleware adds custom behavior without changing the agent.
- Node hooks run before or after specific stages.
- Wrap hooks provide full control over model and tool execution.
- Middleware helps implement logging, retries, caching, monitoring, safety checks, and intelligent model selection.
- Separating concerns makes LangChain agents more scalable and maintainable.