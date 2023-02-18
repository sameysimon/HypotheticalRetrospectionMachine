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
        if isinstance(value, int) or isinstance(value, float):
            self.poeticProb = "None"
            self.numericProb = value
        else:
            self.poeticProb = value

    def multiply(self, other):
        if self.poeticProb == "None":    
            return Probability(self.numericProb * other.numericProb)
        newMidPoint = Probability.KentsWords[self.poeticProb][0] * Probability.KentsWords[other.poeticProb][0]
        return Probability(self.getClosestKentWord(newMidPoint))

    def getKentWord(self):
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word[0]] - Probability.KentsWords[word[1]]
            upperBound = Probability.KentsWords[word[1]] + Probability.KentsWords[word[1]]
            if lowerBound <= self.numericProb and self.numericProb <= upperBound:
                return word
    def getMidPoint(self):
        if self.poeticProb == "None":
            return self.numericProb
        return Probability.KentsWords[self.poeticProb][0]

    def __mul__(self, other):
        if self.poeticProb == "None":
            return self.numericProb * other
        return Probability.KentsWords[self.poeticProb][0] * other


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


class PoeticProbability(Probability):
    KentsWords = {
        "Certain": [1, 0],
        "Almost certain": [0.93, 0.06],
        "Probable": [0.75, 0.12],
        "Chances about even": [0.5, 0.1],
        "Probably not": [0.3, 0.1],
        "Almost certainly not": [0.07, 0.05],
        "Impossible": [0,0]
    }

    def __init__(self, word) -> None:
        self.poeticProb = word
    
    def __mul__(self, other):
        return PoeticProbability(self.poeticProb + " that it's " + other.poeticProb)
    
    __rmul__ = __mul__

    def getKentWord(self):
        minDistance = 1
        minDistanceTo = ""
        for word in Probability.KentsWords:
            lowerBound = Probability.KentsWords[word][0] - Probability.KentsWords[word[1]]
            upperBound = Probability.KentsWords[word][0] + Probability.KentsWords[word[1]]
            if lowerBound <= self.midPoint and self.midPoint <= upperBound:
                return word
            distance = min(abs(self.midPoint - lowerBound), abs(self.midPoint-upperBound))
            if distance < minDistance:
                minDistance = distance
                minDistanceTo = word
        if self.midPoint > Probability.KentsWords[minDistanceTo][0]:
            return "More than " + minDistanceTo
        else:
            return "Less than " + minDistanceTo
    

    


    