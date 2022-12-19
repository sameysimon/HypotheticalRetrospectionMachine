class Action:
    def __init__(self, ID, seedAction):
        self.ID = ID
        self.Name = seedAction
        self.PathList = []
        self.fullyAccepted = True
    def addPath(self, newPath):
        self.PathList.append(newPath)
        return newPath
