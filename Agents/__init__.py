from .summarize_tool import SummarizeTool
from .summary_validation_agent import SummaryValidatorAgent
from .sanitize_data_tool import SanitizeDataTool
from .sanitize_data_validator import SanitizeDataValidatorAgent
from .refiner_tool import RefinerAgentTool
from .write_article_tool import WriteArticleTool
from .writer_Article_validator import WriteArticleValidatorAgent


class AgentManager:
    def __init__(self,max_retries=2,verbose=True):
        self.agents = {
        "summarize":SummarizeTool(max_retries=max_retries,verbose=verbose),
        "write_article": WriteArticleTool(max_retries=max_retries,verbose=verbose),
        "sanitize_data": SanitizeDataTool(max_retries=max_retries,verbose=verbose),
        "summarize_validator_agent": SummaryValidatorAgent(max_retries=max_retries,verbose=verbose),
        "sanitize_data_validator_agent": SanitizeDataValidatorAgent(max_retries=max_retries,verbose=verbose),
        "writer_article_validator_agent": WriteArticleValidatorAgent(max_retries=max_retries,verbose=verbose),
        "refiner_agent": RefinerAgentTool(max_retries=max_retries,verbose=verbose)
}
    def get_agent(self,agent_name):
        agent = self.agents.get(agent_name)
        if not agent:
            raise ValueError(f"Agent {agent_name} not found.")
        return agent