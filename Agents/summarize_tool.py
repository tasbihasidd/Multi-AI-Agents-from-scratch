from .agent_base import AgentBase #calling llm

class SummarizeTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='SummarizationTool', max_retries=max_retries, verbose=verbose)

    def execute(self,text):
        messages = [
            {"role": "user", "content": 'You are an AI assisstant that summarizes medical texts.'},
            {"role": "assistant", "content": ("Please provide summary of the following medical text:\n\n"
             f"{text}\n\nSummary:")
             }
        ]
        summary = self.call_llm(messages,max_tokens=300) #calling llm 
        return summary
