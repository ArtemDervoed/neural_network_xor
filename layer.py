import math

class Layer:
    def __init__(self, firstSynaps, secondSynaps):
        self.firstSynaps = firstSynaps
        self.secondSynaps = secondSynaps

    def activate(self, x):
        return 1 / ( 1 + math.exp(-x))

    def getFirstSynaps(self):
        return self.firstSynaps

    def getSecondSynaps(self):
        return self.secondSynaps

    def getResult(self):
        return self.activate(self.firstSynaps.getOutput() + self.secondSynaps.getOutput())

    def correctWeigths(self, newFirstWeight, newSecondWeight):
        self.firstSynaps.setWeight(newFirstWeight)
        self.secondSynaps.setWeight(newSecondWeight)
