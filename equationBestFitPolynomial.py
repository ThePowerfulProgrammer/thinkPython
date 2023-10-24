import numpy as np # Linealgebra library

# Ax = b
# find solutions to matrix b

def bestFit(dataset:list):
    print("Data is passed as: Xi,Yi", "\n")
    n = 2
    sum = 0;
    sumList = []
    # Create solutions
    for j in range(n+1):
        for x,y in dataset:
            sum += (x**j)*y
        sumList.append(round(sum,3))
        sum = 0
    return sumList

dataSet = [(0,1),(0.25,1.2840),(0.50,1.6487), (0.75,2.1170), (1.00,2.7183)]

solutionSet = bestFit(dataSet);
# print(solutionSet)

# Create values for matrix A
def createPolynomialEquation(dataset:list):
    coefficentList = []
    for j in range(len(dataSet)):
        sum = 0
        for x,y in dataSet:
            sum += x**j
        coefficentList.append(round(sum,3))
    return coefficentList
        
coefficents = createPolynomialEquation(dataset=dataSet)
# print(coefficents)

def createMarix(solutionSet:list):
    start = 0
    end = 3;
    rows = []
    for equa in range(len(solutionSet)):
        for var in coefficents[start:end]:
            rows.append(var)
            
        start += 1
        end += 1
        
    A = np.array(np.array_split(rows,3))
    B = np.array(solutionSet)
    
    return A,B

A,B = createMarix(solutionSet)

# print(A)
# print(B) 

def solveMatrix(A,B):
    x = np.linalg.solve(A,B)
    return x

x = solveMatrix(A, B)

# Ax = b

print(x)










