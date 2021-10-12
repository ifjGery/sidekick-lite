left = 0
center = 1
right = 2

class Buttons:
    def __init__(self):
        self.callbacks = [
                ("", lambda : None),
                ("", lambda : None),
                ("", lambda : None)
        ]
    
    def setButton(self, id, label, callback):
        self.callbacks[id] = (label, callback)

    def clearButton(self, id):
        self.callbacks[id] = ("", lambda : None)

    def callButton(self, id):
        self.callbacks[id][1]()

    def getLabels(self):
        return list(map(lambda one: one[0], self.callbacks))
    
