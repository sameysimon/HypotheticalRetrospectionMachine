import Path
class Action:
    def __init__(self, ID, _name, _firstMech, _scenario):
        self.ID = ID
        self.Name = _name
        self.Effect = _firstMech
        self.Scenario = _scenario
        self.PathList = []
        self.fullyAccepted = True
        self.PathIDRange = []
        self.PathIDList = []

    def addPath(self, newPath):
        self.PathList.append(newPath)
        self.PathIDList.append(newPath.ID)
        return newPath