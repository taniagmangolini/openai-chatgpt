import logging
import sys

class Logger:
    def __init__(self, name=None, level=logging.INFO, stream=sys.stdout, format_str="%(asctime)s - %(name)s - %(levelname)s - %(message)s"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(stream)
        handler.setLevel(level)
        
        formatter = logging.Formatter(format_str)
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
