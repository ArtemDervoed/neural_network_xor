class Synaps:
    def __init__(self, input, weight):
        self.input = input
        self.weight = weight

    def setWeight(self, newWeight):
        self.weight = newWeight

    def getOutput(self):
        return self.input.getValue() * self.weight
