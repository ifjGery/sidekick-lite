from PIL import ImageFont
import threading
import os

import screen

class Command:
    def __init__(self, setDirty):
        self.draw = screen.Screen.instance().getDraw()
        self.setDirty = setDirty
        self.results = "Loading..."
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)

    def _execute(self, command):
        stream = os.popen(command)
        self.results = stream.read()
        self.setDirty()

    def run(self, command):
        threading.Thread(target=self._execute, args=(command,)).start()

    def render(self):
        self.draw.text((0, 0), self.results, font=self.font, fill=(255, 255, 255))
