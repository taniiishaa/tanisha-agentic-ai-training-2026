from langchain_core.callbacks import BaseCallbackHandler

class AgentMiddlewareHandler(BaseCallbackHandler):
    
    @before_agent
    def start1(self, state):
        print("Agent started!")
    
    @after_agent
    def end2(self, state):
        print("Agent finished!")

    @before_model
    def start2(self, state):
        print("Model started!")

    @after_model
    def end2(self, state):
        print("Model finished!")
