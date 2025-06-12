import logging


logging.basicConfig(level=logging.INFO, filename='log.log',
                    filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.error('test error')
logging.warning('test warning')
logging.info('test info')