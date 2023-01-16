from Edge import Edge 
class ArgumentGraph:
    def __init__(self, actions, considerations):
        # Evaluate each action by iterating through its paths
        # Compare each path to every other action's paths and see if they attack each other.

        self.edges = []

        # Iterate through first n-1 actions
        for defenderActionIndex in range(0, len(actions)-1):
            # Iterate through the action's different branches.
            for defenderPath in actions[defenderActionIndex].PathList:
                # Compare this defender action's branch to every other action's branches
                for attackerActionIndex in range(defenderActionIndex+1, len(actions)):
                    for attackerPath in actions[attackerActionIndex].PathList:
                        #Check if this branch attacks the other.
                        compare = self.checkForAttack(attackerPath, defenderPath, considerations)
                        if compare > 0:
                            attackerPath.attacks.append(defenderPath)
                            defenderPath.attackedBy.append(attackerPath)
                            defenderPath.fullyAccepted = False
                        if compare == -1 or compare == 2:
                            defenderPath.attacks.append(attackerPath)
                            attackerPath.attackedBy.append(defenderPath)
                            attackerPath.fullyAccepted = False
                        
                            
        print("built argument tree.\n\n\n")

    # Checks for attack between two paths. 
    # Returns 0 if no attacks. 1 if attacker attacks defender. -1 if defender attacks attacker. 2 if both attack each other.
    def checkForAttack(self, pathOne, pathTwo, considerations):
        oneAttacksTwo = False
        twoAttacksOne = False
        conResult = 0
        for law in considerations:
            conResult = law.doesAttack(pathOne, pathTwo)
            if conResult == 1:
                self.edges.append(Edge(pathOne, pathTwo, law))
                oneAttacksTwo = True
            elif conResult==-1:
                self.edges.append(Edge(pathTwo, pathOne, law))
                twoAttacksOne = True
        if oneAttacksTwo and twoAttacksOne:
            return 2
        if oneAttacksTwo:
            return 1
        if twoAttacksOne:
            return -1
        return 0
                

    def findMostAccepted(self, actions):
        acceptability = {}
        mostAcceptedActionID = actions[0].ID
        allEqualFlag = True
        for action in actions:
            acceptability[action.ID] = 0
            for path in action.PathList:
                if path.fullyAccepted:
                    acceptability[action.ID] += path.Probability
            if acceptability[mostAcceptedActionID] != acceptability[path.rootAction.ID]:
                allEqualFlag = False
            if acceptability[mostAcceptedActionID] < acceptability[path.rootAction.ID]:
                mostAcceptedActionID = path.rootAction.ID
            print(action.Name + " acceptability is " + str(acceptability[action.ID]))
            
        if allEqualFlag:
            print("This is a true dilemma. No action would seem superior to any other, from any point of retrospection.")
        else:
            print("Most accepted is " + actions[mostAcceptedActionID].Name)

    def ToString(self, actions):
        for action in actions:
            print("Arguments from " + action.Name + "...")
            for path in action.PathList:
                print(path.ToString())
                print("     Attacks... \n")

                output = ""
                for attacks in path.attacks:
                    output += "     a Path with action, " + attacks.rootAction.Name + ". \n"
                if len(output) == 0:
                    print("Nothing.\n")
                else:
                    print(output)



                

            


    

