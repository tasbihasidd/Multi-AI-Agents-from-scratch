from .agent_base import AgentBase #calling llm

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='SanitizeDataTool', max_retries=max_retries, verbose=verbose)

    def execute(self,medical_data):
        messages = [
            {"role": "user", "content": 'You are an AI assisstant that sanitizess medical data by removing Protected Health Information (PHI) .'},
            {"role": "assistant", "content": ("Remove all PHI from the following:\n\n"
             f"{medical_data}\n\nSanitized Data:")
             }
        ]
        sanitized_data = self.call_llm(messages,max_tokens=300) #calling llm 
        return sanitized_data
