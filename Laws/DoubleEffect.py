from Laws.Rule import Rule
import json
import io
class DoubleEffect(Rule):
        def __init__(self):
            self.Label = "Double Effect"
            self.ForebiddenActions = []
            
        def doesAttack(self, attackerPath, defenderPath):
            attackerViolates = self.__checkForViolation(attackerPath)
            defenderViolates = self.__checkForViolation(defenderPath)
            # Find the probability/expectation that the attacker's won't violate principle of double effect
            if not (attackerPath.rootAction.ID in self.actionExpectations.keys()):
                self.actionExpectations[attackerPath.rootAction.ID] = 0
                for alternatePath in attackerPath.rootAction.PathList:
                    if not self.__checkForViolation(alternatePath):
                        self.actionExpectations[attackerPath.rootAction.ID] += alternatePath.Probability

            # Find the probability/expectation that the defender won't violate principle of double effect
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
        
        def __checkForViolation(self, path):
            # Nature of the act must be good.
            #   We will check not in the bad action list.
            if path.rootAction.Name in self.ForebiddenActions:
                return True
            
            # Bad effect must not be the means by which one achieves good effects (hard part)
            #   Check the intended good is not caused by a bad effect.
            badEffects = []
            for step in path.Sequence:
                pass
            
            
            # Intention must be to achieve only the good effect, the bad must be an unintended side effect (ignore for now)
            #   This is an ethical machine. It's intentions have to be good.
            
            # Proportionality condition.
            #   good must be immeasurably better than the good??
            
            
            pass
            
        def importListFromScenario(self, fileName):
            with io.open(fileName) as data:
                model = json.load(data)
            self.ForebiddenActions = model['ForebiddenActions']
            