from langchain_ollama import ChatOllama
from tools import all_github_tools

def create_agent(model="qwen2.5:0.5b"):
    llm = ChatOllama(model=model)
    agent_with_tools = llm.bind_tools(all_github_tools)
    return agent_with_tools