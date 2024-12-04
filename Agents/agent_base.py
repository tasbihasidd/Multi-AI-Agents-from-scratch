import openai
from abc import ABC,abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class AgentBase(ABC):
    def __init__(self,name,max_retries=2,verbose=True):
        self.name = name # name of agent 
        self.max_retries = max_retries # no. of retries if llm is not able to generate result for any reason
        self.verbose = verbose # all the description and logs

    @abstractmethod
    def execute(self, *args,**kwargs):
        pass


    def call_llm(self, messages,temperature=0.7, max_tokens=150):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}]: Sending message to OpenAI: ")
                    for msg in messages:
                        logger.debug(f"{msg['role']}:{msg['content']}")

                response = openai.ChatCompletion.create(
                    model = 'gpt-4o',
                    messages = messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                reply = response.choices[0].message
                if self.verbose:
                    logger.info(f"[{self.name}]: Received response from OpenAI: {reply}")
                return reply 
        
            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}]: Failed to generate response from OpenAI. Retrying... {e}")

        raise Exception(f"[{self.name}] Failed to get response from OpenAI after {self.max_retries} retries")

            