from Laws.Rule import Rule
from Probability import Probability
from Edge import Edge
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
            return None
        
        probDefenderIsBetter = 0
        defended = False
        for utilClass in range(0, winningClass+1):
            defenderExpected = self.getExpectedUtilityOnClass(defender, utilClass)
            attackerExpected = self.getExpectedUtilityOnClass(attacker, utilClass)
            if defenderExpected > attackerExpected:
                defended = True
                break
        """
        for utilClass in range(0, winningClass+1):
            defenderExpected = self.getExpectedUtilityOnClass(defender, utilClass)
            
            if defenderExpected > Probability.multiply(attacker.Probability, attackerValues[utilClass]):
                defended = True
                break
        """
        if defended:
            return None
        return Edge(attacker, defender, self)
    
                    

    def getExpectedUtilityOnClass(self, path, utilClass):
        val = 0
        for classElement in self.Scenario.Utilities[utilClass]:
            for altPath in path.rootAction.PathList:
                if altPath.State[classElement['Literal']] == classElement['Value']:
                    val += Probability.multiply(altPath.Probability, classElement['Utility'])
        return val

    def getPathUtilityOnClass(self, path, utilClass):
        val = 0
        for classElement in self.Scenario.Utilities[utilClass]:
            if path.State[classElement['Literal']] == classElement['Value']:
                val += classElement['Utility']
        return val

class ExpectedUtilityResult:
    def __init__(self, _defence, _attack, _class) -> None:
        self.defenderExpected = _defence
        self.attackerValue = _attack
        self.utilityClass = _class
    def ToString(self):
        return "On utility class {0}, the attacking argument had a probability weighted value of {1}, greater than the defender's expectation of {2}. So, retrospecting from the defending argument's endpath, the better choice would be ".format(self.utilityClass, self.attackerValue, self.defenderExpected) 