import os
from langchain.chat_models import init_chat_model

agent = init_chat_model("ollama:qwen2.5:0.5b")
