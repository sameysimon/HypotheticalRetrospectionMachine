class Expectation:
    def __init__(self, _probability, _value) -> None:
        self.probability = _probability
        self.value = _value
        
    def ToString(self):
        if self.probability.isPoetic:
            return "odds are " + self.probability.poeticProb + " of " + str(self.value)
        return str(self.probability.numericProb * self.value)
    
    def ToNumeric(self):
        return self.probability.numericProb * self.value


