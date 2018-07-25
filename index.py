from input import Input
from synaps import Synaps
from layer import Layer
import math

trainingSet = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

epochCount = 100

def sigmoid(out):
    return (1 - out)*out

def calcError(calculatedValue, expectedValue):
    return math.sqrt(math.pow(expectedValue - calculatedValue, 2)/1)


firstInput = Input(1)
secondInput = Input(0)

firstSynaps = Synaps(firstInput, 0.4)
secondSynaps = Synaps(secondInput, 0.7)

hiddenLayer = Layer(firstSynaps, secondSynaps)

# for epoch in range(epochCount):
#     for set in trainingSet:
result = hiddenLayer.getResult()
error = calcError(result, 1)
delta0 = (1 - result) * sigmoid(result)

gradW1 = result * delta0


print(gradW1)
