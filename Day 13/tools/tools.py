from langchain.tools import tool
from pydantic import BaseModel, Field

class AddArgs(BaseModel):
    arg1: float = Field(description="First number")
    arg2: float = Field(description="Second number")

@tool(args_schema=AddArgs)
def add(arg1: float, arg2: float) -> dict:
    try:
        total = arg1 + arg2
        return {"result": total}
    except Exception as e:
        return {"error": str(e)}
