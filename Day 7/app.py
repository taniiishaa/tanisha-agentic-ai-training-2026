from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b"
)

response = llm.invoke("Why do parrots talk?")

print(response.content)
