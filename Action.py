import Path
import copy
from queue import LifoQueue
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
    
        self.setup = False
        self.branchNoStack = LifoQueue()
        self.MechStack = LifoQueue()
        self.PathStack = LifoQueue()
        self.nextPathCount = 0
        self.PathGrid = []



    def addPath(self, newPath):
        self.PathList.append(newPath)
        self.PathIDList.append(newPath.ID)
        return newPath

    def setupPaths(self):
        self.branchNoStack.empty()
        self.MechStack.empty()
        self.branchNoStack.put(0)
        self.MechStack.put(self.Scenario.Mechanisms[self.Effect])
        self.PathGrid = []
        self.path = []
        self.setup = True

    def nextPath(self, level=-1):
        self.nextPathCount = self.nextPathCount + 1
        if level == -1:
            level = len(self.PathGrid)
        if self.setup == False:
            self.setupPaths()
            level = 1


        # Check if any mechanism left
        if self.MechStack.empty():
            return []
        # Get current mechanism.
        # Peek by getting reference, then putting back
        m = self.MechStack.get()
        self.MechStack.put(m)

        # Get the operator of the mechanism.
        operator = 'and'
        if 'or' in m:
            operator = 'or'
        
        # Coming back or getting to a mechanism, but need to check child.
        c = self.branchNoStack.get()
        c = c + 1
        
        # Check if checked all mechanism's children
        if c > len(m[operator]):
            x = self.MechStack.get() # Take off the stack 
            return self.PathGrid[level]

        # Process children in different ways.
        if operator == 'or':
            # Process the c'th branch for this mech.
            # Will need to return to this mech for later branches, so save mech's child count on stack.
            # The or operator wipes the additions previously made by other or branches
            self.branchNoStack.put(c)
            branch = m[operator][c-1]

            if len(self.PathGrid) < level:
                self.PathGrid.append([branch['Name']])
            else:
                self.PathGrid[level-1] = [branch['Name']]

            if branch['Type'] == 'Mech':
                self.branchNoStack.put(0)
                self.MechStack.put(self.Scenario.Mechanisms[branch['Name']]) # Add mechanism to be processed next.
                
                childPath = self.nextPath(level+1)
                self.PathGrid[level-1].extend(childPath)
                
                return self.PathGrid[level-1]
            else:
                return self.PathGrid[level-1]


            
        if operator == 'and':
            # Process the c'th branch for this mech.
            # Will need to return to this mech for later branches, so save mech's child count on stack.
            self.branchNoStack.put(c)
            branch = m[operator][c-1]
            nextLevel = level
            
            if len(self.PathGrid) < level:
                self.PathGrid.append([branch['Name']])
            else:
                self.PathGrid[level-1].append(branch['Name'])

            if branch['Type'] == 'Mech':
                self.branchNoStack.put(0)
                self.MechStack.put(self.Scenario.Mechanisms[branch['Name']]) # Add mechanism to be processed next.
                p = copy.deepcopy(self.PathGrid[level-1])
                p.extend(self.nextPath(level+1))
                self.MechStack.put(m)
                self.branchNoStack.put(c)

            return self.nextPath(level)

            return self.PathGrid[level-1]
            
