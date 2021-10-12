from PIL import ImageFont

import screen

class Buttons:
    def __init__(self, setDirty):
        self.draw = screen.Screen.instance().getDraw()
        self.setDirty = setDirty

    def updateLabelsViaButton(self, buttons):
        self.labels = buttons.getLabels()
        self.setDirty()

    def render(self):
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 8)
        border = (255, 255, 255)
        self.draw.line((0, 160 - 11, 128, 160 - 11), border)
        self.draw.line((41, 160 - 11, 41, 160 ), border)
        self.draw.line((128 - 41, 160 - 11, 128 - 41, 160 ), border)

        self.draw.text((0, 160 - 10), self.labels[0], font=font, fill=(255, 255, 255))
        self.draw.text((42, 160 - 10), self.labels[1], font=font, fill=(255, 255, 255))
        self.draw.text((128 - 40, 160 - 10), self.labels[2], font=font, fill=(255, 255, 255))
