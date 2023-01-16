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
        time = 0
        self.MechTable = {} # Will store the path from each mechanism forward.
        self.MechIDTable = {}

        for actionName in self.scenario.Actions:
            effName = self.scenario.Actions[actionName]['effect']
            result = self.depthSearchMech(effName, self.scenario.Mechanisms[effName])
            self.MechTable[effName] = result
            if self.actionCompatable(actionName, time):
                self.scenario.openingActions.append(Action(actionID, actionName, effName, self.scenario))
                actionID = actionID + 1
        return self.MechTable
    
    def actionCompatable(self, actionName, time):
        return True

    def depthSearchMech(self, mechName, mech):
        # Journey as far down a mechanism as possible to find a leaf. Return a list of paths from the mech (list of lists)
        if mechName in self.MechTable.keys():
            return self.MechTable[mechName]
        Paths = [] # Simple list of object-lists representing all the paths that can come from this mechanism.
        Paths.append(NewPath())
        localElements = 0
        totalElements = 0
        totalSubroutes = 1

        for operator in mech:
            totalElements += localElements
            for element in mech[operator]:
                localElements += 1
                if operator == "and":
                    # Adds mechanism's elements to all paths from the mechanism.
                    self.appendToAll(Paths, element)
                elif operator == "or":
                    # Creates new paths from this mechanism's with this element
                    self.appendToAllNew(Paths, element, totalElements+1)
                    totalSubroutes = totalElements+1
                if element['Type'] == "Mech":
                    # Recur on mechanism to find list of its paths, and add this to the table.
                    self.MechTable[element['Name']] = self.depthSearchMech(element['Name'], self.scenario.Mechanisms[element['Name']])
                    totalSubroutes *= self.MechTable[element['Name']][0].totalSubRoutes
        if operator == "or":
            for i in range(totalElements+1):
                Paths.remove(Paths[i])
        for i in range(len(Paths)):
            Paths[i].totalSubRoutes = totalSubroutes
        
        return Paths

    def appendToAll(self, masterList, newElement):
        for subList in masterList:
            subList.path.append(newElement)
            subList.totalSubRoutes 

    def appendToAllNew(self, masterList, newElement, workingCount):
        for subIndex in range(0, workingCount):
            appendedPath = copy.deepcopy(masterList[subIndex])
            appendedPath.path.append(newElement)
            masterList.append(appendedPath)



