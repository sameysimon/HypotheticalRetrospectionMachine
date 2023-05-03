from Edge import Edge 
class ArgumentGraph:
    def __init__(self, scenario):
        self.actions = scenario.Branches
        self.Considerations = scenario.Considerations

        # Evaluate each action by iterating through its paths
        # Compare each path to every other action's paths and see if they attack each other.
        self.edges = []
        self.isNotAccepted = []
    
        # Iterate through first n-1 self.actions
        for defenderActionIndex in range(0, len(self.actions)-1):
            # Iterate through the action's different branches.
            for defenderPath in self.actions[defenderActionIndex].PathList:
                # Compare this defender action's branch to every other action's branches
                for attackerActionIndex in range(defenderActionIndex+1, len(self.actions)):
                    for attackerPath in self.actions[attackerActionIndex].PathList:
                        #Check if this branch attacks the other.
                        result = self.checkForAttack(attackerPath, defenderPath)
                        if result == 1 and not (defenderPath.ID in self.isNotAccepted):
                            self.isNotAccepted.append(defenderPath.ID)
                        elif result == -1 and not (attackerPath.ID in self.isNotAccepted):
                            self.isNotAccepted.append(attackerPath.ID)


        print("built argument tree.\n\n\n")

    # Checks for attack between two paths.
    def checkForAttack(self, pathOne, pathTwo):
        attackDirection = 0
        isAttack = False
        for law in self.Considerations:
            e = law.doesAttack(pathOne, pathTwo)
            if e is not None:
                self.edges.append(e)
                a = 1 if pathOne.ID == e.source.ID else -1
                if not isAttack:
                    attackDirection = a
                if isAttack and a != attackDirection:
                    attackDirection = 0
        return attackDirection


            
    def getMostAccepted(self):
        acceptability = {}
        mostAcceptedActionID = self.actions[0].ID
        allEqualFlag = True
        for action in self.actions:
            acceptability[action.ID] = 0
            for path in action.PathList:
                if not (path.ID in self.isNotAccepted):
                    acceptability[action.ID] += path.Probability.numericProb
            if acceptability[mostAcceptedActionID] != acceptability[path.rootAction.ID]:
                allEqualFlag = False
            if acceptability[mostAcceptedActionID] < acceptability[path.rootAction.ID]:
                mostAcceptedActionID = path.rootAction.ID
            
        if allEqualFlag:
            return "This is a true dilemma. No action would seem superior to any other, from any point of retrospection."
        else:
            return "Most accepted is " + self.actions[mostAcceptedActionID].Name

    def ToString(self):
        output = ""
        for action in self.actions:
            output += "Arguments from " + action.Name + "..."
            for path in action.PathList:
                output += path.ToString()
                output += "     Attacks... \n"

                for attacks in path.attacks:
                    output += "     a Path with action, " + attacks.rootAction.Name + ". \n"
                if len(output) == 0:
                    output+= "Nothing.\n"
        return output
                    

    def getNodeList(self):
        list = {}
        for act in self.actions:
            list[act.Name] = act.PathIDList
        return list

    def getEdgeList(self):
        list = []
        for edge in self.edges:
            list.append(edge.getTuple())
        return list