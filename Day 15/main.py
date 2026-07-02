from fastapi import FastAPI
from agent import Agent

app = FastAPI(title="Agentic AI")

@app.get("/chat")
def chat(message: str):
    try:
        response = Agent.invoke({
            "input": message,
            "chat_history": []
        })
        return {"response": response.get("output", "No response generated.")}
        
    except Exception as error:
        return {"error": f"Failed to execute pipeline: {str(error)}"}
