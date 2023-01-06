class ArgumentGraph:
    def __init__(self, actionBranches, considerations):
        # Evaluate each action by iterating through its paths
        # Compare each path to every other action's paths and see if they attack each other.

        # Iterate through first n-1 actions
        for defenderActionIndex in range(0, len(actionBranches)-1):
            # Iterate through the action's different branches.
            for defenderPath in actionBranches[defenderActionIndex].PathList:
                # Compare this defender action's branch to every other action's branches
                for attackerActionIndex in range(defenderActionIndex+1, len(actionBranches)):
                    for attackerPath in actionBranches[attackerActionIndex].PathList:
                        
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
    def checkForAttack(self, attackerPath, defenderPath, considerations):
        compare = 0
        new = 0
        for law in considerations:
            new = law.doesAttack(attackerPath, defenderPath)
            if new == 1:
                print("Path ID {0} attacks ID {1} with rule {2}".format(attackerPath.ID, defenderPath.ID, law.Label))
            elif new==-1:
                print("Path ID {0} attacks ID {1} with rule {2}".format(defenderPath.ID, attackerPath.ID, law.Label))
            
            
            if (compare == -1 and new == 1) or (compare == 1 and new == -1):
                return 2
            if new != 0:
                compare = new
        return compare
                

    def findMostAccepted(self, actionBranches):
        acceptability = {}
        mostAcceptedActionID = actionBranches[0].ID
        allEqualFlag = True
        for action in actionBranches:
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
            print("Most accepted is " + actionBranches[mostAcceptedActionID].Name)


    def ToString(self, actionBranches):
        for action in actionBranches:
            print("Arguments from " + action.Name + "...")
            for path in action.PathList:
                print(path.ToString())
                print("     Attacks... \n")

                output = ""
                for attacks in path.attacks:
                    output += "     a Path with action, " + attacks.lastAction + ". \n"
                if len(output) == 0:
                    print("Nothing.\n")
                else:
                    print(output)

                

            


    

