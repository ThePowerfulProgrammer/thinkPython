import math
# Create a function that returns the hypotenuse of a right angle triangle
# Given the length of the legs

def generateHypotenuseLength(length1,length2):
    length1Squared = length1**2;
    length2Squared = length2**2;
    sumSquared = length1Squared + length2Squared;
    return math.sqrt(sumSquared), "Is the length";

print(generateHypotenuseLength(3,4));
    

