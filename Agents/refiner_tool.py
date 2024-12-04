from .agent_base import AgentBase #calling llm

class RefinerAgentTool(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name='RefinerAgentTool', max_retries=max_retries, verbose=verbose)

    def execute(self,draft):
        messages = [
            {"role": "user", 
             "content": [
                 {
                     'type': 'text',
                     'text':'You are an expert editor who refines and enhances articles for clarity, coherence and academic quality.'
                     },
             ]
         },
            {"role": "assistant", 
             "content": [
                 {
                     'type': 'text',
                     'text': (
                         "Please refine the following article to imrove its language, coheremce, and overall quality.\n\n"
                         f"{draft}\n\nRefinedArticle"
                     )
                     
             }
        ]
            }
        ]
        refined_article = self.call_llm(messages,temperature = 0.3,max_tokens=2048) #calling llm 
        return refined_article
