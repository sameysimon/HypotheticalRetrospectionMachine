from Laws.Rule import Rule
class ExpectedUtility(Rule):
    def __init__(self):
        self.Label = "Expected Utility"
        self.PathUtility = {}
        self.ActionsBestExpectation = {}
        
    def doesAttack(self, pathOne, pathTwo):
        pathOneValues = []
        pathTwoValues = []
        # Find which path attacks the other. (has a higher utility in the highest state)
        attackerValues = []
        winningClass = 0
        attacker = 0
        defender = 0
        for utilClass in range(0, len(self.Scenario.Utilities)):
            pathOneValues.append(self.getPathUtilityOnClass(pathOne, utilClass))
            pathTwoValues.append(self.getPathUtilityOnClass(pathTwo, utilClass))
            if pathOneValues[utilClass] < pathTwoValues[utilClass]:
                attacker = pathTwo
                defender = pathOne
                attackerValues = pathTwoValues
                winningClass = utilClass
                break
            elif pathOneValues[utilClass] > pathTwoValues[utilClass]:
                defender = pathTwo
                attacker = pathOne
                attackerValues = pathOneValues
                winningClass = utilClass
                break
        if attacker == 0:
            return 0
        
        probDefenderIsBetter = 0
        defended = False
        #
        for utilClass in range(0, winningClass+1):
            defenderExpected = self.getExpectedUtilityOnClass(defender, utilClass)
            if defenderExpected > attackerValues[utilClass]*attacker.Probability:
                defended = True
        if defended:
            return 0
        if attacker == pathOne:
            return 1
        else:
            return -1



        # If found: Of the defender's alternate paths, find the probability it gets something better.
        for altPath in defender.rootAction.PathList:
            if altPath.ID != defender.ID:
                for utilClass in range(0, winningClass+1):
                    altVal = self.getPathUtilityOnClass(altPath, utilClass)
                    if altVal >= attackerValues[utilClass]:
                        if (utilClass < winningClass):
                            # If value on a higher utilitiy class, then defence always wins.
                            probDefenderIsBetter += 2
                        else:
                            probDefenderIsBetter += altPath.Probability
                        #break
        if probDefenderIsBetter > attacker.Probability:
            return 0
        elif attacker==pathOne:
            return 1
        else:
            return -1
                    

    def getExpectedUtilityOnClass(self, path, utilClass):
        val = 0
        for classVar in self.Scenario.Utilities[utilClass]:
            for altPath in path.rootAction.PathList:
                if altPath.State[classVar] == True:
                    val += altPath.Probability * self.Scenario.Utilities[utilClass][classVar]
        return val

    def getPathUtilityOnClass(self, path, utilClass):
        val = 0
        for classVar in self.Scenario.Utilities[utilClass]:
            if path.State[classVar] == True:
                val += self.Scenario.Utilities[utilClass][classVar]
        return val


