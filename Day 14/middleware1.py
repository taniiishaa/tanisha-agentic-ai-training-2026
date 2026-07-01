from langchain.agents.middleware import AgentMiddleware

class LoggingMiddle(AgentMiddleware):
    def before_agent(self, state):
        print("Agent Started!!!")

    def after_agent(self, state):
        print("Agent Finished!!!")
