class MenuNavigator:
    def __init__(self, menu):
        self.root = menu
        self.current = self.root
        self.path = []

    def getOptions(self):
        items = list(self.current)
        if(len(self.path)):
            items.insert(0,'..')
        return list(filter(lambda name: name[0] != '_',items))

    def getChild(self, index):
        return self.current[self.getOptions()[index]]

    def getType(self):
        if ('_type' in self.current):
            return self.current['_type']
        else:
            return 'item'
    
    def getChildType(self, index):
        if(len(self.path) and index == 0):
            return 'item'
        item = self.current[self.getOptions()[index]]
        if ('_type' in item):
            return item['_type']
        else:
            return 'item'

    def goUp(self):
        if(len(self.path)):
            self.current = self.path.pop()
        return self

    def goDown(self, index):
        if(self.getChildType(index) == 'item'):
            if(len(self.path) and index == 0):
                self.goUp()
            else:
                items = self.getOptions()
                self.path.append(self.current)
                self.current = self.current[items[index]]
        return self
