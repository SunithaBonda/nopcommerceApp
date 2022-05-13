import inspect
import logging
class LogGen:
    @staticmethod
    def loggen(logLevel=logging.DEBUG):
       # Gets the name of the class / method from where this method is called
       loggerName = inspect.stack()[1][3]
       logger = logging.getLogger("sunitha")
       # By default, log all messages
       logger.setLevel(logging.DEBUG)
       fileHandler = logging.FileHandler(filename='Logs')
       fileHandler.setLevel(logLevel)
       formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
       fileHandler.setFormatter(formatter)
       logger.addHandler(fileHandler)
       return logger
#import logging
#class LogGen:
    #@staticmethod
    #def loggen():
      ## formatter=logging.formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
       #handler=logging.FileHandler(filename='.\\Logs\\automation.log')
       #handler.setFormatter(formatter)
       #logger=logging.getLogger()
       #logger.setLevel(logging.INFO)
       #logger.addHandler(handler)
      # return logger
