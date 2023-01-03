from Laws.ExpectedUtility import ExpectedUtility
class ArgumentGraph:
    def __init__(self, actionBranches):
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
                        compare = ExpectedUtility.doesAttack(attackerPath, defenderPath)
                        if compare > 0:
                            # Attacker has better state.
                            attackerPath.attacks.append(defenderPath)
                            defenderPath.attackedBy.append(attackerPath)
                            defenderPath.fullyAccepted = False
                        elif compare < 0:
                            # Defender has better state.
                            defenderPath.attacks.append(attackerPath)
                            attackerPath.attackedBy.append(defenderPath)
                            attackerPath.fullyAccepted = False
        print("built argument tree.\n\n\n")

    def findMostAccepted(self, actionBranches):
        acceptability = {}
        mostAcceptedActionID = actionBranches[0].ID
        for action in actionBranches:
            acceptability[action.ID] = 0
            for path in action.PathList:
                if path.fullyAccepted:
                    acceptability[action.ID] += path.Probability
            if acceptability[mostAcceptedActionID] < acceptability[path.rootAction.ID]:
                mostAcceptedActionID = path.rootAction.ID
            print(action.Name + " acceptability is " + str(acceptability[action.ID]))
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

                

            


    

