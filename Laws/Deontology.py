from Laws.Rule import Rule
class Deontology(Rule):
    def __init__(self, banned):
        self.Forebidden = banned
        self.Label = "Deontology"
        
    def doesAttack(self, pathOne, pathTwo):
        # Find if one path could attack the other. (one path violates and the other doesn't)
        pathOneViolates = self.checkForViolation(pathOne)
        pathTwoViolates = self.checkForViolation(pathTwo)
        attacker = 0
        defender = 0

        if pathOneViolates and not pathTwoViolates:
            # Path two could attack path one
            defender = pathOne
            attacker = pathTwo
        elif pathTwoViolates and not pathOneViolates:
            # Path one could attack path two
            attacker = pathOne
            defender = pathTwo
        else:
            # Neither can attack the other.
            return 0
        defenceProb = 0
        for altPath in defender.rootAction.PathList:
            if altPath.ID != defender.ID:
                if not self.checkForViolation(altPath):
                    defenceProb += altPath.Probability
        if defenceProb > attacker.Probability:
            return 0
        if pathOne == attacker:
            return 1
        else:
            return -1
         

                

    def checkForViolation(self, path):
        for literal in self.Forebidden:
            return (path.State[literal] == True)
            
        


