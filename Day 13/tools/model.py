from langchain.agents import create_agent
from tools import add

agent = create_agent(
    model="ollama:qwen2.5:0.5b",
    tools=[add],
    # Kept extremely short so the 0.5b model can process it easily
    system_prompt="You are a calculator. Use the add tool for addition."
)