import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getuserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
