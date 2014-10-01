import random

def randomize():
    return random.uniform(-1, 1)

def genRandomPoint():
    x = randomize()
    y = randomize()
    return 1.0, x, y

def calculateLine(a, b):
    slope = (a[2] - b[2]) / (a[1] - b[1])
    intercept = slope*-a[1] + b[2]
    return 1, slope, intercept 

def dotproduct(x, y):
    return x[0]*y[0] + x[1]*y[1] + x[2]*y[2]

def createDataSet(N):
    return [genRandomPoint() for i in range(N)]

def sign(x):
    return (1 if x > 0 else -1)
    
def createMissclassified(x, y, N):
    return [point for point in range(N) if sign(x[point]*y[point]) == -1]

def selectPoint(x):
    return random.choice(x)

def determineSign(line, point):
    return sign(dotproduct(line,point))

def perceptronAlgorithm(c, x, y, N, dataSet, yActual, yPredicted):
    g = [c, x, y]
    misclassified = createMissclassified(yActual, yPredicted, N)        
    wrongDataPoint = random.choice(misclassified)
    g[0] += yActual[wrongDataPoint]*dataSet[wrongDataPoint][0]
    g[1] += yActual[wrongDataPoint]*dataSet[wrongDataPoint][1]
    g[2] += yActual[wrongDataPoint]*dataSet[wrongDataPoint][2]
    return g


def simulate(N, S):
    totalSError = 0
    totalSSims = 0
    for i in range(S):
        dataSet = createDataSet(N)
        f = calculateLine(genRandomPoint(), genRandomPoint())
        yActual = [determineSign(f,dataSet[i]) for i in range(N)]
        g = [0, 0, 0]
        yPredicted = [determineSign(g,dataSet[i]) for i in range(N)]
        maxIterations = 10000
        totalSimulations = 0
        totalError = 0
        for i in range(maxIterations):
            if len(createMissclassified(yActual, yPredicted, N)) > 0:
                g = perceptronAlgorithm(g[0], g[1], g[2], N, dataSet, yActual, yPredicted)
                yPredicted = [determineSign(g,dataSet[i]) for i in range(N)]
            else:
                totalSimulations += (i + 1)
                newData = createDataSet(10000)
                newYActual = [determineSign(f,newData[i]) for i in range(10000)]
                newYPredicted = [determineSign(g,newData[i]) for i in range(10000)]
                totalError += len(createMissclassified(newYActual, newYPredicted, 10000))
                break
        totalSError += totalError
        totalSSims += totalSimulations
    return float(totalSSims/float(S)), float(totalSError/float(S)/10000.0)
        
            
    
