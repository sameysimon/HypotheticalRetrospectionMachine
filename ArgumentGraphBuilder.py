class ArgumentGraphBuilder:
    def __init__(self, actionBranches):
        self.ActionBranches = actionBranches
        # Evaluate each action by iterating through its paths
        # Compare each path to every other action's paths and see if they attack each other.

        # Iterate through first n-1 actions 
        for defenderActionIndex in range(0, len(self.ActionBranches)-1):
            # Iterate through the action's different branches.
            for defenderPath in self.ActionBranches[defenderActionIndex].PathList:
                # Compare this defender action's branch to every other action's branches
                for attackerActionIndex in range(defenderActionIndex+1, len(self.ActionBranches)):
                    for attackerPath in self.ActionBranches[attackerActionIndex].PathList:
                        
                        #Check if this branch attacks the other.
                        compare = attackerPath.compare(defenderPath)

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
                        else:
                            #TODO: COMPARE BY ETHICAL RULES.
                            print ("to do, implement ethical rules.")
        print("built argument tree.\n\n\n")

    def ToString(self):
        for action in self.ActionBranches:
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

                

            


    

