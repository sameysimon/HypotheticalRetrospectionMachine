class Path:
    def __init__(self, state, Utilities) -> None:
        self.Actions = []
        self.Mech = []
        self.Probability = 1
        self.State = state
        self.Log = []
        self.Sequence = []

        self.Utility = []
        self.bestUtilityClass = len(Utilities)-1
        self.defaultUtility(Utilities)
        

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
        self.State[variable] = value
        self.Probability *= prob
        if self.State[variable] != value:
            self.setUtility(variable=variable, value=value, Utilities=Utilities)

        self.Log.append(msg)
        self.Sequence.append({"Name": variable, "Value": value, "Prob":prob, "Type":"State"})

    def defaultUtility(self, Utilities):
        for var in self.State:
            self.Utility.append(0)
            self.setUtility(var, self.State[var], Utilities)


    def setUtility(self, variable, value, Utilities):
        # Find referenced variable in utility classes
        for utilityClassCount, utilityClass in enumerate(Utilities):
            if (variable in utilityClass):
                # If class has key, add or subtract utilitiy for class.
                if (value == True):    
                    self.Utility[utilityClassCount] += utilityClass[variable]
                    # Check if this now the best utility class.
                    if (utilityClassCount < self.bestUtilityClass and self.Utility[utilityClassCount] > 0):
                        self.bestUtilityClass = utilityClassCount
                else:
                    self.Utility[utilityClassCount] -= utilityClass[variable]
                    # May no longer be the be the best utility class now.
                    # So, must see which next highest class is greater than 0, having the greatest utility.
                    if (utilityClassCount == self.bestUtilityClass and self.Utility[utilityClassCount] < 0):
                        self.bestUtilityClass = len(Utilities)
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

    def compareTo(self, otherPath):
        if otherPath.bestUtilityClass < self.bestUtilityClass:
            return -1
        elif otherPath.bestUtilityClass > self.bestUtilityClass:
            return 1
        else:
            if otherPath.Utility[otherPath.bestUtilityClass]*self.Probability < self.Utility[self.bestUtilityClass]*self.Probability:
                return -1
            elif otherPath.Utility[otherPath.bestUtilityClass]*otherPath.Probability > self.Utility[self.bestUtilityClass]*self.Probability:
                return 1
            else:
                return 0

