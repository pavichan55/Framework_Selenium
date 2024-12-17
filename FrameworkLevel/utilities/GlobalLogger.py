import logging

from datetime import date
today = date.today()
filename=today
class GlobalLogger:
    
    def __init__(self):
        today = date.today()
        filename=today
        logging.basicConfig(filename=f"{filename}.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

        #Creating an object
        logger=logging.getLogger()

        #Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)
        
    @staticmethod
    def logText(text):
        logging.info(text)