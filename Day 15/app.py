import streamlit as st
import time
from agent import Agent

st.title("Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Let's start chatting!"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if message := st.chat_input("What is going on?"):
    
    st.session_state.messages.append({"role": "user", "content": message})
    with st.chat_message("user"):
        st.markdown(message)
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            result = Agent.invoke({
                "input": message,
                "chat_history": []
            })
            
            assistant_response = result.get("output", "I couldn't process that.")
            
            for chunk in assistant_response.split(" "):
                full_response += chunk + " "
                time.sleep(0.04)
                message_placeholder.markdown(full_response + "▌")
                
            message_placeholder.markdown(full_response.strip())
            
            st.session_state.messages.append({"role": "assistant", "content": full_response.strip()})
            
        except Exception as e:
            message_placeholder.markdown(f"An error occurred: `{str(e)}`")
