import configparser
config=configparser.RawConfigParser()
#this file is created to read the data from config.ini file.without this file we cannot read config.ini
config.read("C://Users//parik//PycharmProjects//nopcommerceApp//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    #by writing @staticmethod we can directly access the methods in readProperties.py   by the class name ReadConfig
    # without creating any object
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info', 'password')
        return password