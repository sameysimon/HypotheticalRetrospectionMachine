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
        
    

