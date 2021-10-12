import yaml

class Config:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            with open('./config/menu.yml') as configFile:
                cls.config = yaml.load(configFile)
        return cls._instance

    def getConfig(self):
        return self.config
