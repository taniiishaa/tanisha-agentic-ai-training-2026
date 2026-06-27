import streamlit as st
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from pydantic import BaseModel, Field
from langchain.tools import tool

st.title("Calculator Agent")

class AddArgs(BaseModel):
    arg1: float = Field(description="First number")
    arg2: float = Field(description="Second number")

@tool(args_schema=AddArgs)
def add(arg1: float, arg2: float):
    """Adds two numbers together."""
    total = arg1 + arg2
    return {"result": total}

agent = create_agent(
    model="ollama:qwen2.5:0.5b",
    tools=[add],
    system_prompt="You are a simple calculator. Use the add tool to compute additions."
)

user_query = st.text_input("Enter your request:")

if st.button("Run Agent"):
    if user_query:
        config = {"configurable": {"thread_id": "session_123"}}
        
        response = agent.invoke(
            {"messages": [HumanMessage(content=user_query)]}, 
            config=config
        )
        
        final_message = response["messages"][-1]
        
        st.subheader("Final Output")
        st.write(final_message.content)
        
        st.subheader("Raw Metadata Response")
        st.json({
            "content": final_message.content,
            "tool_calls": final_message.tool_calls,
            "type": final_message.type,
            "id": final_message.id
        })