# LangChain

## Introduction

LangChain is an open-source framework used to build applications powered by Large Language Models (LLMs). It helps developers connect AI models with tools, data sources, memory, and workflows.

## Why Use LangChain?

- Simplifies LLM application development
- Connects AI models with external tools
- Supports chatbots and AI assistants
- Enables Retrieval-Augmented Generation (RAG)
- Works with multiple AI providers

## Key Components

### 1. Models

LangChain can interact with different language models such as:

- OpenAI GPT models
- Ollama local models
- Google Gemini
- Anthropic Claude

Example:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")
```

---

### 2. Prompts

Prompts define the instructions given to the model.

```python
prompt = "Explain cloud computing in simple terms."
```

---

### 3. Chains

Chains combine multiple steps into a workflow.

Example:

```text
User Input
    ↓
Prompt
    ↓
LLM
    ↓
Response
```

---

### 4. Memory

Memory allows applications to remember previous interactions.

Example use cases:

- Chatbots
- Virtual assistants
- Customer support systems

---

### 5. Tools

Tools enable AI models to interact with external systems.

Examples:

- Web search
- APIs
- Databases
- Calculators

---

## Installing LangChain

Using pip:

```bash
pip install langchain
```

Using uv:

```bash
uv pip install langchain
```

For Ollama integration:

```bash
uv pip install langchain-ollama
```

---

## Simple Example

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

response = llm.invoke("What is Artificial Intelligence?")

print(response.content)
```

---

## Applications of LangChain

- AI Chatbots
- Question Answering Systems
- Document Analysis
- Personal Assistants
- Research Tools
- Code Generation

---

## Advantages

- Easy integration with LLMs
- Modular architecture
- Supports local and cloud models
- Large community support
- Suitable for production applications

---

## Common Use Cases

| Use Case | Example |
|-----------|----------|
| Chatbot | Customer support assistant |
| RAG | Querying documents |
| Agent | AI performing tasks |
| Automation | Workflow execution |
| Research | Information retrieval |

---

## Conclusion

LangChain is a powerful framework for developing AI-powered applications. It provides tools for connecting language models with prompts, memory, data sources, and external services, making it easier to build intelligent and scalable AI systems.