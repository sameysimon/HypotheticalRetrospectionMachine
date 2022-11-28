

class Path:
    def __init__(self, state) -> None:
        self.Actions = []
        self.Mech = []
        self.Probability = 1
        self.State = state
        self.Log = []
        self.Sequence = []
    
    def addAction(self, action, actionName):
        self.Actions.append(action)
        self.Log.append("Agent does action " + actionName)
        self.Sequence.append({"Name": actionName, "Type":"Action"})
    
    def addMech(self, mech, prob, name):
        self.Mech.append(mech)
        self.Probability *= prob
        self.Log.append(name + " happened with " + str(prob) + " chance.")
        self.Sequence.append({"Name": name,"Prob":prob, "Type":"Mech"})

    def AddToState(self, variable, value, prob=1):
        msg = (variable + " changed from " + str(self.State[variable]) + " to " + str(value) + " with " + str(prob) + " chance.")
        self.State[variable] = value
        self.Probability *= prob
        self.Log.append(msg)
        self.Sequence.append({"Name": variable, "Value": value, "Prob":prob, "Type":"State"})

    def ToString(self):
        output = ""
        for msg in self.Log:
            output += msg + "\n"
        return output