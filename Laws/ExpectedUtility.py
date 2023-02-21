from Laws.Rule import Rule
from Probability import Probability
from Expectation import Expectation
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

        defended = False
        for utilClass in range(0, winningClass+1):
            defenderExpected = self.getExpectedUtilityOnClass(defender, utilClass)
            attackerExpected = self.getExpectedUtilityOnClass(attacker, utilClass)
            if defenderExpected > attackerExpected:
                defended = True
                break
        if defended:
            return None
        return Edge(attacker, defender, self)

    def getExpectedUtilityOnClass(self, path, utilClass):
        val = 0
        for classElement in self.Scenario.Utilities[utilClass]:
            for altPath in path.rootAction.PathList:
                if altPath.State[classElement['Literal']] == classElement['Value']:
                    val += Expectation(altPath.Probability, classElement['Utility']).ToNumeric()
        return val

    def getPathUtilityOnClass(self, path, utilClass):
        val = 0
        for classElement in self.Scenario.Utilities[utilClass]:
            if path.State[classElement['Literal']] == classElement['Value']:
                val += classElement['Utility']
        return val
