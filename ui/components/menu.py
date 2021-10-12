from PIL import ImageFont

import screen

class Menu:
    def __init__(self, setDirty):
        self.draw = screen.Screen.instance().getDraw()
        self.setDirty = setDirty
        self.selected = 0
        self.items = []
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)

    def setItems(self, items):
        self.selected = 0
        self.items = items
        self.setDirty()

    def getSelected(self):
        return self.selected

    def selectNext(self):
        self.selected += 1
        self.selected = self.selected % len(self.items)
        self.setDirty()

    def selectPrev(self):
        self.selected -= 1
        self.selected = self.selected % len(self.items)
        self.setDirty()

    def render(self):
        text = "\n".join(
                list(
                    map(
                        lambda one: "%s%s" % (">" if one[0] == self.selected else " ", one[1]), 
                        enumerate(self.items)
                        )
                    )
                )


        self.draw.text((0, 0), text, font=self.font, fill=(255, 255, 255))

