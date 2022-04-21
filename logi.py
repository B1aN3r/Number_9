from loguru import logger

logger.add('logs.log', format = '{time} {level} {message}',
level = "INFO", rotation= '50 KB', compression= 'zip')

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
