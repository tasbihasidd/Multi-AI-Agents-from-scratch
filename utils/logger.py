from loguru import logger 
import sys
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger.remove() #to remove the default logger
logger.add(sys.stdout, level='INFO', format='<green>{timestamp}</green><level>{message}</level>')
logger.add('logs/multi_agent_system.log',rotation='1 MB',retention = "10 days",level= 'DEBUG', format = '{time} {level} {message}')


logger.info("Agent Manager initialized")