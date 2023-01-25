import io, copy, json
from Action import Action
from Path import Path


class Scenario:
    def __init__(self, scenarioName='DefaultScenario'):
        self.Actions = {}
        self.InitState = {}
        self.Mechanisms = {}
        self.MechConsequences = {}
        self.Utilities = []


        self.Name = scenarioName
        self.Considerations = []
        self.Branches = []

    def getArgumentList(self):
        l = {}
        for branch in self.Branches:
            for path in branch.PathList:
                l[path.ID] = path.ToArgument()
        return l

    def generateActionPaths(self, _consequences):
        actionPathways = []
        self.MechConsequences = _consequences
        actionID = 0
        time = 0
        for currAction in self.Actions:
            self.getAllPaths(self.Actions[currAction]['effect'], "")
            """
            if self.checkActionCompatable(currAction, self.InitState, time):
                actionObj = Action(actionID, currAction, self.Actions[currAction]['effect'], self)
                actionObj.PathIDRange = self.getMechPathIDs(self.Actions[currAction]['effect'])
                actionPathways.append(actionObj)
                actionID+=1
                """

    # A path ID is the index of the branch pursued on each mech in the path.
    # So pathID=103 is a path that took branch 1 on the initial mech;
    # reached a second mech and took branch 0;
    # reached a third mech and took branch 3.
    def getMechPathIDs(self, mechName):
        MechIDRanges = []
        numOfElements = len(self.MechConsequences[mechName])
        for branch in self.MechConsequences[mechName]: 
            # Find the first mech (at the end of this branch, unless there's no mech)
            lastElement = branch[len(branch)-1]
            if lastElement['Type'] != 'Mech':
                # End of branch.
                # If no branch ranges were added, add this mech's ID range (1)
                if len(MechIDRanges) == 0:
                    MechIDRanges.append([1])
                return MechIDRanges
            else:
                # Found another mech down this branch.
                # Add a branch with the number of this mech's range
                numOfBranches = len(self.MechConsequences[lastElement['Name']])
                # Find the last end point's range IDs
                subMechRanges = self.getMechPathIDs(lastElement['Name'])

                # For each of its ranges, add a range to this mech (since conatinment)
                for newBranchIndex in range(0, numOfBranches):
                    newBranch = [numOfBranches]
                    for subBranchIndex in range(0, len(subMechRanges)):
                        newBranch = [numOfBranches]
                        newBranch.extend(subMechRanges[subBranchIndex])
                        MechIDRanges.append(newBranch)
                    

                return MechIDRanges# Return it.
    

    def getAllPaths(self, mechName, header):
        atEnd = False
        pathList = []
        for branchIndex in range(0, len(self.MechConsequences[mechName])):
            # Add branch index to id
            newPath = header + str(branchIndex)
            pathList.append(newPath)
            for element in self.MechConsequences[mechName][branchIndex]:
                if element['Type'] == 'Mech':
                    return self.getAllPaths(element['Name'], newPath)
            return ""



    def checkActionCompatable(self, action, state, time):
        return True


    def addConsideration(self, rule):
        rule.Scenario = self
        self.Considerations.append(rule)
        
    def writeToJSON(self, fileName):
        data = {}
        data['Name'] = self.Name
        data['Actions'] = self.Actions
        data['Mechanisms'] = self.Mechanisms
        data['Utilities'] = self.Utilities
        data['State'] = self.InitState

        with open(fileName, 'w') as f:
            json.dump(data,f)

    def readFromJSON(self, fileName):
        with io.open(fileName) as data:
            model = json.load(data)
            self.Actions = model['Actions']
            self.InitState = model['State']
            self.Mechanisms = model['Mechanisms']
            self.Utilities = model['Utilities']


    def addAction(self, name, preConds, effs, start, end):
        self.Actions[name] = {}
        self.Actions[name]['StartTime'] = start
        self.Actions[name]['EndTime'] = end
        self.Actions[name]['effects'] = effs
        self.Actions[name]['preconditions'] = preConds
    
    def addMech(self, name):
        self.Mechanisms[name] = {}
        return self.Mechanisms[name]

    def addToMech(self, mechanism, connector, name, prob, type, value):
        if not (connector in mechanism.keys()):
            mechanism[connector] = []
        mechanism[connector].append({"Name": name, "Value": value, "Probability": prob, "Type": type})

    def addState(self, name, Value):
        self.InitState[name] = Value
    
    def addUtility(self, utilClass, name, state, util):
        NumOfUtilClasses = len(self.Utilities)
        print(NumOfUtilClasses)
        print(utilClass)
        if utilClass >= NumOfUtilClasses:
            for uClass in range(0, utilClass - (NumOfUtilClasses-1)):
                self.Utilities.append([])
        self.Utilities[utilClass].append({"Literal": name, "Value": state, "Utility": util})        
        
    

