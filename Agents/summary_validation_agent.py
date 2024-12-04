from .agent_base import AgentBase #calling llm

class SummaryValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='SummaryValidatorAgent', max_retries=max_retries, verbose=verbose)

    def execute(self,original_text,summary):
        system_message = "You are an expert AI assisstant that validates the summaries of medical texts."
        user_content = (
            "Given the originalsummary, assess whether the summary accurately capture the key points and is of high quality.\n"
            "Provide a brief analysis and rate the summary  on a scale of 1-5, where 5 indicates excellent quality.\n\n"
            f'Original text: {original_text}\n\n'
            f'Summary: \n{summary}\n\n'
            f'Validation: '
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
    
        
        validation = self.call_llm(messages,max_tokens=512) #calling llm 
        return validation
