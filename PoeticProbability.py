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

    def __init__(self, value) -> None:
        self.poeticProb = "None"
        self.set(value)

    def multiply(prob, value) -> float:
        return prob*value

    def ToString(self):
        s = ""

    def ToWord(self):
        if self.poeticProb == "None":
            return self.getKentWord()
        else:
            return self.poeticProb

    def set(self, value):
        if type(value) is int or type(value) is float:
            self.numericProb = value
        else:
            self.poeticProb = value
    
    def getKentWord(self):
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word[0]] - Probability.KentsWords[word[1]]
            upperBound = Probability.KentsWords[word[1]] + Probability.KentsWords[word[1]]
            if lowerBound <= self.numericProb and self.numericProb <= upperBound:
                return word

    def __mul__(self, other):
        pass

    __rmul__ = __mul__

    def __lt__(self, other):
        return
    
    
    