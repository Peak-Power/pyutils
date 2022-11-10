import logging
import sys

logger = logging.getLogger()

class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)

def get_logger(lev="info"):
    level = logging.INFO
    if lev == 'debug':
        level = logging.DEBUG
    

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(level)

    h1 = logging.StreamHandler(sys.stdout)
    h1.addFilter(InfoFilter())
    h1.setFormatter(formatter)
    
    h2 = logging.StreamHandler()
    h2.setLevel(logging.WARNING)
    h2.setFormatter(formatter)

    logger.addHandler(h1)
    logger.addHandler(h2)

    return logger
