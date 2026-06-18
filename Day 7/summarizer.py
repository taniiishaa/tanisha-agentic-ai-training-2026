from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

text = """
Artificial Intelligence is transforming industries
by enabling machines to perform tasks that normally
require human intelligence.
"""

response = llm.invoke(
    f"Summarize this text in 3 points:\n{text}"
)

print(response.content)