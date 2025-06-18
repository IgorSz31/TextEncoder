import logging



def setup_logger():
    """
    Sets up the logger file, its direction and format
    """

    logging.basicConfig(level=logging.DEBUG, filename='logs/app.log',
                        filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
