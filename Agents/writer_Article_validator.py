from .agent_base import AgentBase #calling llm

class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='WriteArticleValidatorAgent', max_retries=max_retries, verbose=verbose)

    def execute(self,topic,article):
        system_message = "You are an expert academic writer that validates articles. "
        user_content = (
            "Given the topic and the article, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
            "Provide a brief analysis and rate the article on a scale of 1-5, where 5 indicates excellent quality.\n\n"
            f'Topic: {topic}\n\n'
            f'Article: \n{article}\n\n'
            f'Validation: '
        )
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
    
        
        validation = self.call_llm(messages,max_tokens=512) #calling llm 
        return validation
