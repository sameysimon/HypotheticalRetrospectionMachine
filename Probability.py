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
        self.isPoetic = False
        if isinstance(value, int) or isinstance(value, float):
            self.numericProb = value
            self.poeticProb = self.getClosestKentWord(value)
        else:
            self.isPoetic = True
            self.poeticProb = value
            self.numericProb = Probability.KentsWords[self.poeticProb][0]

    def ToString(self):
        if self.isPoetic:
            return self.poeticProb
        return str(self.numericProb)


    def multiply(self, other):
        if self.numericProb == 1:
            self.numericProb = other.numericProb
            self.poeticProb = other.poeticProb
        if self.otherProb == 1:
            return
        
        


    def getKentWord(self):
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word[0]] - Probability.KentsWords[word[1]]
            upperBound = Probability.KentsWords[word[1]] + Probability.KentsWords[word[1]]
            if lowerBound <= self.numericProb and self.numericProb <= upperBound:
                return word

    def getMidPoint(self):
        if not self.isPoetic:
            return self.numericProb
        return Probability.KentsWords[self.poeticProb][0]

    def getClosestKentWord(self, value):
        minDistance = 1
        minDistanceTo = ""
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word][0] - Probability.KentsWords[word][1]
            upperBound = Probability.KentsWords[word][0] + Probability.KentsWords[word][1]
            if lowerBound <= value and value <= upperBound:
                return word
            distance = min(abs(value - lowerBound), abs(value-upperBound))
            if distance < minDistance:
                minDistance = distance
                minDistanceTo = word
        return minDistanceTo

    


    