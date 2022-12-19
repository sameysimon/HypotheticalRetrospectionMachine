class ExpectedUtility:
    def init(Utilities, Actions):
        ExpectedUtility.PathUtil = {}
        ExpectedUtility.Utilities = Utilities
        ExpectedUtility.Actions = Actions 
        ExpectedUtility.ActionsBestExpectation = {}

    def __lTCompareAltPath(pathOne, pathTwo):
        if not (pathOne.ID in ExpectedUtility.PathUtil):
            ExpectedUtility.__evaluateNewPath(pathOne)
        if not (pathTwo.ID in ExpectedUtility.PathUtil):
            ExpectedUtility.__evaluateNewPath(pathTwo)

        # Step down through utility classes (most important first) to find the first class where one is better than the other.
        for utilClass in range(0, len(ExpectedUtility.Utilities)):
            # Starting from the most important class, see if Two is higher than One at this class
            if ExpectedUtility.PathUtil[pathOne.ID][utilClass] < ExpectedUtility.PathUtil[pathTwo.ID][utilClass]:
                return True
            # Check reverse!!
            # Starting from the most important class, see if One is higher than Two at this class
            if ExpectedUtility.PathUtil[pathOne.ID][utilClass] >= ExpectedUtility.PathUtil[pathTwo.ID][utilClass]:
                return False
        return 0


    def doesAttack(attackerPath, defenderPath):
        if not (attackerPath.ID in ExpectedUtility.PathUtil):
            ExpectedUtility.__evaluateNewPath(attackerPath)
        if not (defenderPath.ID in ExpectedUtility.PathUtil):
            ExpectedUtility.__evaluateNewPath(defenderPath)

        for utilClass in range(0, len(ExpectedUtility.Utilities)):
            
            # Starting from the most important class, see if Two is higher than One

            if ExpectedUtility.PathUtil[attackerPath.ID][utilClass] > ExpectedUtility.PathUtil[defenderPath.ID][utilClass]:
                # Defender's State is less than Attackers State. So Attacker could attack defender.
                # Must check if Defender doesn't guard with a higher expectation.
                # If Defender is already best expectation, then no guard and attack is true.
                if ExpectedUtility.ActionsBestExpectation[defenderPath.rootAction.ID].ID == defenderPath.ID:
                    return 1
                # If Defender's best expectation is less than Attacker, then no guard and attack is true.
                if not (ExpectedUtility.doesAttack(ExpectedUtility.ActionsBestExpectation[attackerPath.rootAction.ID], defenderPath)):
                    return 1

            # Check reverse (does defender attack attacker?)

            if ExpectedUtility.PathUtil[attackerPath.ID][utilClass] < ExpectedUtility.PathUtil[defenderPath.ID][utilClass]:
                # Attacker's State is less than Defender's State. So Defender could attack Attacker.
                # Must check if Attacker doesn't guard with a higher expectation.
                # If Attacker is already the best expectation, then no guard and attack is true.
                if ExpectedUtility.ActionsBestExpectation[attackerPath.rootAction.ID].ID == attackerPath.ID:
                    return -1
                # If Attacker's best expectation is less than Defender then no guard and attack is true
                if not (ExpectedUtility.doesAttack(ExpectedUtility.ActionsBestExpectation[attackerPath.rootAction.ID], defenderPath)):
                    # Defender is better than Attacker, and its expectation. So, Defender attacks Attacker.
                    return -1


                # Check reverse!!
        # Nothing was true. Therefore no attacks.
        return 0


    def __evaluateNewPath(path):
        # Create an entry to store this path's utility.
        ExpectedUtility.PathUtil[path.ID] = []
        # Default utility to 0 for every utility class.
        for utilityClass in ExpectedUtility.Utilities:
            ExpectedUtility.PathUtil[path.ID].append(0)
        # Represents best path (highest positive utility class) for the action
        

        # Iterate through every state variable to add/subtract its utility
        for stateVar in path.State:
            # Find the utility class for stateVar
            for utilityClassCount, utilityClass in enumerate(ExpectedUtility.Utilities):
                if stateVar in utilityClass:
                    # Add utility if the variable is True, subtract if negative.
                    if path.State[stateVar] == True:
                        ExpectedUtility.PathUtil[path.ID][utilityClassCount] += utilityClass[stateVar]
                    else:
                        ExpectedUtility.PathUtil[path.ID][utilityClassCount] -= utilityClass[stateVar]
                    break
        
        # To find the best expectation for this action, need to evaluate all its paths to find the best one.
        # Compare this path against alternatives. Recording which one beats them all (is the greatest utility)
        ExpectedUtility.ActionsBestExpectation[path.rootAction.ID] = path
        for altPath in path.rootAction.PathList:
            if altPath.ID != path.ID:
                if ExpectedUtility.__lTCompareAltPath(ExpectedUtility.ActionsBestExpectation[path.rootAction.ID], altPath):
                    ExpectedUtility.ActionsBestExpectation[path.rootAction.ID] = altPath

        