import copy

class RenderChain:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Init
            cls.pipeline = []
        return cls._instance

    def set(self, pipeline):
        self.pipeline = copy.copy(pipeline)

    def add(self, renderable):
        self.pipeline.append(renderable)

    def render(self):
        for one in self.pipeline:
            one.render()

