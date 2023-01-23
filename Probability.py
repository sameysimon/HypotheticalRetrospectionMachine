from enum import Enum
class Probability:
    KentsWords = {
        "Certain": [1, 0],
        "Almost certain": [0.93, 0.06],
        "Probable": [0.75, 0.12],
        "Chances about even": [0.5, 0.1],
        "Probably not": [0.3, 0.1],
        "Almost certainly not": [0.07, 0.05],
        "Impossible": [0,0]
    }
    def multiply(prob, value) -> float:
        return prob*value

    def ToString(self):
        s = ""
    


    def set(self, value):
        if type(value) is int or type(value) is float:
            self.numericProb = value
            self.assignKentWord()
        else:
            self.poeticProb = value
            # Default numericProb to midpoint
    
    def assignKentWord(self):
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word[0]] - Probability.KentsWords[word[1]]
            upperBound = Probability.KentsWords[word[1]] + Probability.KentsWords[word[1]]
            if lowerBound <= self.numericProb and self.numericProb <= upperBound:
                self.poeticProb = word
                return


    def __lt__(self, other):
        return
    

        
    