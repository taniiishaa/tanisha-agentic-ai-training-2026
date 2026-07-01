from langchain.agents.middleware import before_agent, after_agent, after_model, before_model

class LoggingMiddle:
    
    @before_agent
    def before_agent_started(self, state):
        print("agent started lets kill all the other tasks!!!")
        
    @after_agent
    def after_agent_finished(self, state):
        print("agent finished lets watch the movie!!!")
        
    @before_model
    def before_model_started(self, state):
        print("model started the tasks lets wait for to agent to start and finish!!!")
        
    @after_model
    def after_model_finished(self, state):
        print("tool work completed lets wait for agent to complete!!!")
