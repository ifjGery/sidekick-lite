from PIL import Image
from PIL import ImageDraw

import ST7735

class Screen():
    _instance = None

    def __init__(self):
            raise RuntimeError('Call instance() instead' )

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            # Init
            cls.disp = ST7735.ST7735(
                    port=0,
                    cs=0,
                    dc=23,
                    backlight=12,
                    rst=22,
                    width=128,
                    height=160,
                    rotation=0,
                    invert=False
                    )

            cls.disp.begin()

            width = cls.disp.width
            height = cls.disp.height

            cls.img = Image.new('RGB', (width, height), color=(0, 0, 0))
            cls.draw = ImageDraw.Draw(cls.img)

            cls.draw.fontmode = "1"
        return cls._instance

    def getDraw(self):
        return self.draw

    def clear(self):
        self.draw.rectangle((0, 0, 128, 160), (0, 0, 0))

    def render(self):
        self.disp.display(self.img)
