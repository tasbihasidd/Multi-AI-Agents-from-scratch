from .agent_base import AgentBase #calling llm

class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='WriteArticleTool', max_retries=max_retries, verbose=verbose)

    def execute(self,topic,outline=None):
        system_message = "You are an expert academic writer "
        user_content = f"Write a research article on the following topic:\nTopic: {topic}\n\n"

        if outline:
            user_content += f"Outline:\n{outline}\n\n"
        user_content += f"Articler:\n"

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_content}
        ]
    
        
        article = self.call_llm(messages,max_tokens=1000) #calling llm 
        return article
