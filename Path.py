class Path:
    def __init__(self, state, Utilities) -> None:
        self.Actions = []
        self.Mech = []
        self.Probability = 1
        self.State = state
        self.Log = []
        self.Sequence = []

        self.Utility = []
        self.bestUtilityClass = len(Utilities) - 1
        self.defaultUtility(Utilities)
        
        self.bestExpectation = 0

        self.attacks = []
        self.attackedBy = []
        self.lastAction = ""

        
    
    def addAction(self, action, actionName):
        self.lastAction = actionName
        self.Actions.append(action)
        self.Log.append("Agent does action " + actionName)
        self.Sequence.append({"Name": actionName, "Type":"Action"})
    
    def addMech(self, mech, prob, name):
        self.Mech.append(mech)
        self.Probability *= prob
        self.Log.append(name + " happened with " + str(prob) + " chance.")
        self.Sequence.append({"Name": name,"Prob":prob, "Type":"Mech"})

    def AddToState(self, variable, value, prob=1, Utilities=[]):
        msg = (variable + " changed from " + str(self.State[variable]) + " to " + str(value) + " with " + str(prob) + " chance.")
        
        self.Probability *= prob
        if self.State[variable] != value:
            self.setUtility(variable=variable, value=value, Utilities=Utilities)
        self.State[variable] = value
        self.Log.append(msg)
        self.Sequence.append({"Name": variable, "Value": value, "Prob":prob, "Type":"State"})

    def defaultUtility(self, Utilities):
        for utilityClass in Utilities:
            self.Utility.append(0)
            
        
            


    def setUtility(self, variable, value, Utilities):
        # Find referenced variable in utility classes
        for utilityClassCount, utilityClass in enumerate(Utilities):
            if (variable in utilityClass):
                # If class has key, add or subtract utilitiy for class.
                if (value == True):    
                    self.Utility[utilityClassCount] += utilityClass[variable]
                    # Check if this now the best utility class.
                    if (utilityClassCount < self.bestUtilityClass and self.Utility[utilityClassCount] > self.Utility[self.bestUtilityClass]):
                        self.bestUtilityClass = utilityClassCount
                else:
                    self.Utility[utilityClassCount] -= utilityClass[variable]
                    # May no longer be the be the best utility class now.
                    # So, must see which next highest class is greater than 0, having the greatest utility.
                    if (utilityClassCount == self.bestUtilityClass and self.Utility[utilityClassCount] < 0):
                        self.bestUtilityClass = len(Utilities)-1
                        for i in range(utilityClassCount+1, len(Utilities)):
                            if self.Utility[i] > 0:
                                self.bestUtilityClass = i
                                break
                break

    # def ToString(self):
    #     output = ""
    #     for msg in self.Log:
    #         output += msg + "\n"
    #     return output

    def ToString(self):
        output = ""
        for step in self.Sequence:
            if (step['Type'] == 'State'):
                output += (step['Name'] + " changed to " + str(step['Value']) + " with " + str(step['Prob']) + " chance.")
            elif (step['Type'] == 'Mech'):
                output += (step['Name'] + " happened with " + str(step['Prob']) + ' chance.')
            elif (step['Type'] == 'Action'):
                output += ("Agent does action " + step['Name'])
            output += '\n'
        return output

    def getArgumentString(self):
        output = "From the initial situation,"
        output += " it was right to do initial action " + self.Actions[0]
        output += " resulting in: "
        for var in self.State:
            output += var + " is " + self.State[var]
        output += "\n"
    
    # Returns 1 if self attacks Two.
    def compare(self, pathTwo):
        pathOneClass = self.bestUtilityClass
        pathTwoClass = pathTwo.bestUtilityClass
        # Check if path one has better utility class or, (if the same class) one has better utility.
        if (pathOneClass < pathTwoClass) or ((pathOneClass == pathTwoClass) and self.Utility[pathOneClass] > pathTwo.Utility[pathOneClass]):
            # Rule two. Check path two doesn't have higher expectation.
            if (self > pathTwo.bestExpectation):
                return 1
        #Reverse
        if (pathOneClass > pathTwoClass) or ((pathOneClass == pathTwoClass) and self.Utility[pathOneClass] < pathTwo.Utility[pathOneClass]):
            # Rule two. Check path one doesn't have higher expectation.
            if (self.bestExpectation < pathTwo):
                return -1

        # If neither of these succeeded, must be equal.
        return 0

    def __lt__(pathOne, pathTwo):
        #These seem opposite, but lower utility classes are better.
        if pathOne.bestUtilityClass < pathTwo.bestUtilityClass:
            return False
        if pathOne.bestUtilityClass > pathTwo.bestUtilityClass:
            return True

        if pathOne.Utility[pathOne.bestUtilityClass]*pathOne.Probability < pathTwo.Utility[pathTwo.bestUtilityClass]*pathTwo.Probability:
            return True
        if pathOne.Utility[pathOne.bestUtilityClass]*pathOne.Probability > pathTwo.Utility[pathTwo.bestUtilityClass]*pathTwo.Probability:
            return False
        return 0
