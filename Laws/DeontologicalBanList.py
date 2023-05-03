import io
import json
from Edge import Edge

class DeontologicalBanList():
    def __init__(self, forbidden={}, fileName="",):
        self.Label = "Deontological Ban List"
        
        self.forbidden = forbidden # forbidden literal values
        if fileName != "":
            self.importListFromScenario(fileName=fileName)

        self.actionExpectations = {} # Stores action ID to the probability the action doesn't violate a rule.
    

    def doesAttack(self, pathOne, pathTwo):
        # Check if each makes a violation.
        pathOneViolates = self.__checkForViolation(pathOne)
        pathTwoViolates = self.__checkForViolation(pathTwo)
        attacker = 0
        defender = 0
        if pathOneViolates and (not pathTwoViolates):
            attacker = pathTwo
            defender = pathOne
        elif pathTwoViolates and (not pathOneViolates):
            attacker = pathOne
            defender = pathTwo
        else:
            return None # Neither can attack the other.

        # Find the probability (expectation) of attack
        attackerExpects = self.__findViolationProbability(attacker)
        defenderExpects = self.__findViolationProbability(defender)

        if defenderExpects < attackerExpects:
            # If attacker had greater expectation than defender, then defending path shouldn't have been chosen.
            return Edge(attacker, defender, self)         
    
    def __findViolationProbability(self, path):
        # Check probability hasn't already been found and stored. If it has, returns existing value.
        if not (path.rootAction.ID in self.actionExpectations.keys()):
            # Iterate through all branching paths for action and sum probability of violation.
            self.actionExpectations[path.rootAction.ID] = 0
            for alternatePath in path.rootAction.PathList:
                if not self.__checkForViolation(alternatePath):
                    self.actionExpectations[path.rootAction.ID] += alternatePath.Probability.getMidPoint()

        return self.actionExpectations[path.rootAction.ID]

    # Check the final state, then every intermediate state for a violation of any forbidden state
    def __checkForViolation(self, path):
        # Iterate through all variables with a forbidden rule associated.
        for bannedVar in self.forbidden:
            # If final state violates the rule, then return as such.
            finalStateViolates = path.State[bannedVar] == self.forbidden[bannedVar]
            if finalStateViolates:
                return finalStateViolates
            # Go through each step of the path's sequence and check for a state that violates the rule.
            for step in path.Sequence:
                if step['Type'] == 'State':
                    if step['Name'] == bannedVar and step['Value'] == self.forbidden[bannedVar]:
                        # This step changes the state, of the forbiddable variable to the forbidden state.
                        # Therefore, it violates the rule and makes a violation.
                        return True   
        return False

    def importListFromScenario(self, fileName):
        with io.open(fileName) as data:
            model = json.load(data)
            self.forbidden.update(model['forbidden'])

    def addforbiddenLiteral(self, var, state):
        self.forbidden[var] = state