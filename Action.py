class Action:
    def __init__(self, seedAction):
        self.Name = seedAction
        self.PathList = []
        self.fullyAccepted = True
    def addPath(self, newPath):
        self.PathList.append(newPath)
        return newPath
