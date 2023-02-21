from Probability import Probability
class Path:
    def __init__(self, ID, state, rootAction) -> None:
        self.ID = ID
        self.rootAction = rootAction
        self.Actions = []
        self.Mech = []
        self.Probability = Probability(1)
        self.State = state
        self.Log = []
        self.Sequence = []

        self.fullyAccepted = True
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
        
        print("prob is " + str(prob))
        self.Probability = self.Probability.multiply(Probability(prob))

        self.Log.append(name + " happened with " + str(prob) + " chance.")
        self.Sequence.append({"Name": name,"Prob":prob, "Type":"Mech"})

    def AddToState(self, variable, value, prob=1):
        msg = (variable + " changed from " + str(self.State[variable]) + " to " + str(value) + " with " + str(prob) + " chance.")
        
        print("prob is " + str(prob))
        self.Probability = self.Probability.multiply(Probability(prob))

        self.State[variable] = value
        self.Log.append(msg)
        self.Sequence.append({"Name": variable, "Value": value, "Prob":prob, "Type":"State"})

    def defaultUtility(self, Utilities):
        for utilityClass in Utilities:
            self.Utility.append(0)
            

    def ToString(self):
        output = "Path ID: " + str(self.ID) + " Probability:" + str(self.Probability) + "\n"
        for step in self.Sequence:
            if (step['Type'] == 'State'):
                output += (step['Name'] + " changed to " + str(step['Value']) + " with " + str(step['Prob']) + " chance.")
            elif (step['Type'] == 'Mech'):
                output += (step['Name'] + " happened with " + str(step['Prob']) + ' chance.')
            elif (step['Type'] == 'Action'):
                output += ("Agent does action " + step['Name'])
            output += '\n'
        return output

    def ToArgument(self):
        output = "From the initial situation,"
        output += " it was right to do action, " + self.rootAction.Name
        output += " resulting in: "
        for i, step in enumerate(self.Sequence):
            if step['Type'] == 'State':
                output += (step['Name'] + " changed to " + str(step['Value']))
            elif (step['Type'] == 'Mech'):
                output += (step['Name'] + " happened with " + str(step['Prob']))
            elif (step['Type'] == 'Action'):
                output += ("Agent does action " + step['Name'])
            if i < len(self.Sequence) - 1:
                output += "; "
            else:
                output += ", "

        output += "with probability, " + self.Probability.ToString() + ".\n"
        
        return output
    
