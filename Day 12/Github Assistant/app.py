import streamlit as st
import asyncio
import time
from model import create_agent
from tools import all_github_tools

st.title("GitHub  Assistant")

# Created a lookup dictionary for your 20 tools
tools_map = {tool.name: tool for tool in all_github_tools}

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Ask me about any public GitHub handle or repository stats!"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

async def run_agent_workflow(user_prompt):
    agent = create_agent()
    
    ai_message = await agent.ainvoke(user_prompt)
    
    if ai_message.tool_calls:
        tool_call = ai_message.tool_calls[0]
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        
        if tool_name in tools_map:
            tool_result = await tools_map[tool_name].ainvoke(tool_args)
            final_prompt = (
                f"User asked: {user_prompt}\n"
                f"Tool '{tool_name}' executed with arguments {tool_args} and returned this real-time data:\n"
                f"{tool_result}\n\n"
                f"Please provide a clean, direct answer to the user based on this data."
            )
            final_message = await agent.ainvoke(final_prompt)
            return final_message.content
            
    return ai_message.content

if user_prompt := st.chat_input("Type a question..."):
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            ai_text = asyncio.run(run_agent_workflow(user_prompt))
            
            if not ai_text or not ai_text.strip():
                ai_text = "I couldn't retrieve a clear answer for that request."
            
            for word in ai_text.split(" "):
                full_response += word + " "
                time.sleep(0.04)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error processing request: {str(e)}"
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
