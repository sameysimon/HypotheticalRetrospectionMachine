class Edge:
    def __init__(self, source, target, law):
        self.source = source
        self.target = target
        self.law = law
        self.source.attacks.append(self.target)
        self.target.attackedBy.append(self.source)
        self.target.fullyAccepted = False


    def getTuple(self):
        return [self.source.ID, self.target.ID, self.law.Label]

    def ToString(self):
        return "Path ID {0} attacks Path ID {1} with rule {2}".format(self.source.ID, self.target.ID, self.law.Label)