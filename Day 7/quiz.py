from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

topic = input("Topic: ")

response = llm.invoke(
    f"Generate 5 MCQs on {topic} with answers."
)

print(response.content)