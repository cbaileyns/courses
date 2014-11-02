import numpy
import matplotlib
import math as m
import random

#answers: c, d, c, e, d, e, a, d, a, e

#Question 1 - Linear Regression Error

def inSampleError(sigma, features, observations):
    '''d = features and n = observations'''
    return (sigma*sigma)*(1 - ((features + 1)/float(observations)))

print "Q1: In sample error with 10 observations " + str(inSampleError(0.1, 8, 10))
print "Q1: In sample error with 25 observations " + str(inSampleError(0.1, 8, 25))
print "Q1: In sample error with 100 observations " + str(inSampleError(0.1, 8, 100))
print "Q1: In sample error with 500 observations " + str(inSampleError(0.1, 8, 500))
print "Q1: In sample error with 1000 observations " + str(inSampleError(0.1, 8, 1000))


#Question 5 - Gradient Descent

def inSamErr(u,v):
    '''This is the E(u,v) function from the assignment question'''
    return (u*m.exp(v) - 2*v*m.exp(-u))**2

def partialU(u, v):
    '''This is the partial derivative with respect to U'''
    return 2*(m.exp(v) + 2*v*m.exp(-u))*(u*m.exp(v) - 2*v*m.exp(-u))

def partialV(u, v):
    '''This is the partial derivative with respect to V'''
    return 2*(u*m.exp(v) - 2*m.exp(-u))*(u*m.exp(v) - 2*v*m.exp(-u))

def gDescent(lRate, u, v):
    '''Gradient Descent: calculate the values of the partial derivative w.r.t U and V.
       Then update U and V with these Values.
       returns: the number of iterations, u, and v values.'''
    iterations = 0
    while (inSamErr(u, v) > 10**-14 and inSamErr(u, v) < 100):
        a = partialU(u, v)
        b = partialV(u, v)
        u -= lRate*a
        v -= lRate*b
        iterations += 1
    return iterations, u, v

iterations, u, v = gDescent(0.1, 1, 1)

print "Q5: The correct answer is " + str(iterations)

#I use this for Question 6. This was obtained in line 49 above.
w = [u, v]

#Question 6 - Euclidian Distance

def getDistance(x, y):
    '''Euclidian distance formula for two points in R^2'''
    y = m.sqrt(((x[0] - y[0])**2) + ((x[1] - y[1])**2))
    return y

a = [1.0, 1.0]
b = [0.713, 0.045]
c = [0.016, 0.112]
d = [-0.083, 0.029]
e = [0.045, 0.024]

print "Q6: The distance to A is " + str(getDistance(w, a))
print "Q6: The distance to B is " + str(getDistance(w, b))
print "Q6: The distance to C is " + str(getDistance(w, c))
print "Q6: The distance to D is " + str(getDistance(w, d))
print "Q6: The distance to E is " + str(getDistance(w, e))

#Question 7 - Coordinate Descent

def cDescent(lRate, u, v):
    '''Very similar to Gradient Descent, but different in the timing of the updates to both U and V'''
    for i in range(15):
        a = partialU(u, v)
        u -= lRate*a
        b = partialV(u, v)
        v =- lRate*b
    return inSamErr(u, v)

print "Q7: After 15 iterations of Coordinate Descent, the in sample error is " + str(cDescent(0.1, 1, 1))

#Question 8 - Logistic Regression

class Point:
    def __init__(self):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        self.x = x
        self.y = y

class Line:
    def __init__(self):
        PointA = Point()
        PointB = Point()
        slope = (PointB.y - PointA.y) / (PointB.x - PointA.x)
        intercept = PointB.y - slope*PointB.x
        self.slope = slope
        self.intercept = intercept

def dataset(n):
    '''Generates n random points'''
    return [[Point().x, Point().y] for i in range(n)]

def output(data, line):
    '''Given a line, this will return a list of y-values for a given set of points'''
    output = []
    for i in range(len(data)):
        if data[i][0]*line.slope + line.intercept < data[i][1]:
            output.append(1)
        else:
            output.append(-1)
    return output

def partialDeriv(weightOne, weightTwo, weightThree, datapoint):
    '''upside down triangle e as per lecture notes and discussion board'''
    a = (1 + m.exp(datapoint[3]*(weightOne*datapoint[0] + weightTwo*datapoint[1] + weightThree*datapoint[2])))
    b = datapoint[3]*datapoint[0]
    c = datapoint[3]*datapoint[1]
    d = datapoint[3]*datapoint[2]
    e = -b/float(a)
    f = -c/float(a)
    g = -d/float(a)
    return e, f, g

def errorIn(data, weightOne, weightTwo, weightThree):
    '''error function'''
    values = [m.log(1+m.exp(-data[i][3]*(weightOne+weightTwo*data[i][1] + weightThree*data[i][2]))) for i in range(len(data))]
    sV = sum(values)
    return sV / float(len(data))

def getDistance3(x, y):
    '''returns the euclidian distance between two points in R3'''
    y = m.sqrt(((x[0] - y[0])**2) + ((x[1] - y[1])**2) + ((x[2] - y[2])**2))
    return y

def sgDescent(point, lRate, weightOne, weightTwo, weightThree):
    '''Inputs: A point, learning rate, and weights
       Calculations: partial derivative w.r.t the weights at that point. updates the weights with these values
       Outputs: updated weights'''
    a, b, c = partialDeriv(weightOne, weightTwo, weightThree, point)
    weightOne -= lRate*a
    weightTwo -= lRate*b
    weightThree -= lRate*c
    return weightOne, weightTwo, weightThree

def epoch(data, lRate, weightOne, weightTwo, weightThree):
    '''Inputs: The Dataset, Eta, the initial weights
       Calculations: From the dataset, selects 100 points, at random, to update the weights.
       After selecting each point once, if the distance between the beginning weights and the
       updated weights is too large, it completes another epoch.
       Returns: Number of epochs, final weights.'''
    epochs = 0
    dist = 1
    while (dist > 0.01):
        wt = [weightOne, weightTwo, weightThree]
        points = [i for i in range(len(data))]
        while (len(points) > 0):
            p = random.choice(points)
            points.remove(p)
            weightOne, weightTwo, weightThree = sgDescent(data[p], lRate, weightOne, weightTwo, weightThree)
        wt1 = [weightOne, weightTwo, weightThree]
        epochs += 1
        dist = getDistance3(wt1, wt)
    return epochs, weightOne, weightTwo, weightThree

epochz = 0
eOut = 0
for i in range(100):
    line = Line()
    x = dataset(100)
    y = output(x, line)
    D = [[1, x[i][0], x[i][1], y[i]] for i in range(len(x))]
    epochs, weightOne, weightTwo, weightThree = epoch(D, 0.01, 0, 0, 0)
    x = dataset(1000)
    y = output(x, line)
    D = [[1, x[i][0], x[i][1], y[i]] for i in range(len(x))]
    eOut += errorIn(D, weightOne, weightTwo, weightThree)
    epochz += epochs

print "Q8: After 100 runs, the average amount of epochs is " + str(epochz / float(100))
print "Q9: After 100 runs, the average eOut is " + str(eOut / float(100))
