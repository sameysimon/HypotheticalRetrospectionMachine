import copy
import Action
from NewPath import NewPath
class BranchFactory:
    def getBranches(self, _scenario):
        self.scenario = _scenario

        # Keep a path list for each mechanism.
        # Choose an action.
        # Do a depth-first generation of one path.
        # Step back through from the bottom up!
        # At each fully determined mechanism, add it to the table (gone down both or paths).
        Actions = []
        actionID = 0
        self.MechTable = {} # Will store the path from each mechanism forward.
        self.MechIDTable = {}

        for actionName in self.scenario.Actions:
            effName = self.scenario.Actions[actionName]['effect']
            self.MechTable[effName] = self.depthSearchMech(effName, self.scenario.Mechanisms[effName])
            print("howdy")
        return self.MechTable
        
    def depthSearchMech(self, mechName, mech):
        # Journey as far down a mechanism as possible to find a leaf. Return a list of paths from the mech (list of lists)
        if mechName in self.MechTable.keys():
            return self.MechTable[mechName]
        Paths = [] # Simple list of object-lists representing all the paths that can come from this mechanism.
        Paths.append(NewPath())
        localElements = 0
        totalElements = 0

        for operator in mech:
            totalElements += localElements
            for elementIndex in range(0, len(mech[operator])):
                element = mech[operator][elementIndex]
                localElements += 1
                if operator == "and":
                    self.appendToAll(Paths, element)
                elif operator == "or":
                    
                    self.appendToAllNew(Paths, element, totalElements+1, elementIndex)

                if element['Type'] == "Mech":
                    # Recur on mechanism to find list of its paths, and add this to the table.
                    self.MechTable[element['Name']] = self.depthSearchMech(element['Name'], self.scenario.Mechanisms[element['Name']])
        if operator == "or":
            for i in range(totalElements+1):
                Paths.remove(Paths[i])

        return Paths

    def appendToAll(self, Paths, newElement):
        for p in Paths:
            p.path.append(newElement)

    def appendToAllNew(self, Paths, newElement, workingCount, index):
        for subIndex in range(0, workingCount):
            newID = [index]
            newID.extend(Paths[subIndex].ID)
            Paths[subIndex].ID.append(newID)

            appendedPath = copy.deepcopy(Paths[subIndex].path)
            appendedPath.append(newElement)
            Paths[subIndex].path.append(appendedPath)


