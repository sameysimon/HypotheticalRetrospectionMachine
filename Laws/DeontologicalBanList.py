import io
import json
from Laws.Rule import Rule

class DeontologicalBanList(Rule):
    def __init__(self):
        self.Label = "Deontological Ban List"
        self.forebidden = {}
        self.actionExpectations = {}

    def doesAttack(self, attackerPath, defenderPath):
        attackerViolates = self.__checkForViolation(attackerPath)
        defenderViolates = self.__checkForViolation(defenderPath)

        # Find the probability that the attacker's won't violate a rule.
        if not (attackerPath.rootAction.ID in self.actionExpectations.keys()):
            self.actionExpectations[attackerPath.rootAction.ID] = 0
            for alternatePath in attackerPath.rootAction.PathList:
                if not self.__checkForViolation(alternatePath):
                    self.actionExpectations[attackerPath.rootAction.ID] += alternatePath.Probability

        # Find the probability that the defender won't violate a rule.
        if not (defenderPath.rootAction.ID in self.actionExpectations.keys()):
            self.actionExpectations[defenderPath.rootAction.ID] = 0
            for alternatePath in defenderPath.rootAction.PathList:
                if not self.__checkForViolation(alternatePath):
                    self.actionExpectations[defenderPath.rootAction.ID] += alternatePath.Probability

        if (not attackerViolates) and defenderViolates:
            if self.actionExpectations[defenderPath.rootAction.ID] < attackerPath.Probability:
                return 1

        # Check for counter attack (reverse)
        if (not defenderViolates) and attackerViolates:
            if self.actionExpectations[attackerPath.rootAction.ID] < defenderPath.Probability:
                return -1

        return 0
    
    # Check the final state, then every intemediate state for a violation of any forebidden state
    def __checkForViolation(self, path):
        # Iterate through all variables with a forebidden rule associated.
        for bannedVar in self.forebidden:
            # If final state violates the rule, then return as such.
            finalStateViolates = path.State[bannedVar] == self.forebidden[bannedVar]
            if finalStateViolates:
                return finalStateViolates
            # Go through each step of the path's sequence and check for a state that violates the rule.
            for step in path.Sequence:
                if step['Type'] == 'State':
                    if step['Name'] == bannedVar and step['Value'] == self.forebidden[bannedVar]:
                        # This step changes the state, of the forebiddable variable to the forebidden state.
                        # Therefore, it violates the rule and makes a violation.
                        return True   
        return False

    def importListFromScenario(self, fileName):
        with io.open(fileName) as data:
            model = json.load(data)
            self.forebidden = model['Forebidden']

    def addForebiddenLiteral(self, var, state):
        self.forebidden[var] = state