import json
import io

class Scenario:
    def __init__(self, scenarioName='DefaultScenario'):
        self.Actions = {}
        self.InitState = {}
        self.Mechanisms = {}
        self.Utilities = []
        self.Name = scenarioName
        self.Considerations = []

    def addConsideration(self, rule):
        rule.addToScenario(self)
        self.Considerations.append(rule)
        
    def writeToJSON(self, fileName):
        data = {}
        data['Name'] = self.Name
        data['Actions'] = self.Actions
        data['Mechanisms'] = self.Mechanisms
        data['Values'] = self.Utilities
        data['State'] = self.InitState

        with open(fileName, 'w') as f:
            json.dump(data,f)

    def readFromJSON(self, fileName):
        with io.open(fileName) as data:
            model = json.load(data)
            self.Actions = model['Actions']
            self.InitState = model['State']
            self.Mechanisms = model['Mechanisms']
            self.Utilities = model['Values']


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
    
    def addValue(self, utilClass, name, util):
        NumOfUtilClasses = len(self.Utilities)-1
        for uClass in range(0, utilClass - NumOfUtilClasses):
            self.Utilities.append({})
        self.Utilities[utilClass][name] = util
    

