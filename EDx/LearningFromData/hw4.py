import random
import math
from numpy import linalg as np
import numpy
import itertools

xOne = random.uniform(-1, 1)
xTwo = random.uniform(-1, 1)

yOne = math.sin(xOne)
pointTwo = math.sin(xTwo)

#Question 4

def genRandomPoint():
    x = random.uniform(1, -1)
    y = math.sin(math.pi*x)
    return 1, x, y

def genRandomPointS(power):
    x = random.uniform(1, -1)
    y = math.sin(math.pi*x)
    return 1, x**power, y

def calculateLine(a, b):
    slope = (a[2] - b[2]) / (a[1] - b[1])
    return 1, slope

def calculateLineB(a, b):
    slope = (a[2] - b[2]) / (a[1] - b[1])
    intercept = b[2] - slope*b[1]
    return 1, slope, intercept

###Question 4

def calculateLineS(a, b, slope=True):
    '''Calculate the slope and the intercept of the line formed by two points.
       If slope is passed as false, the calculate the average between the two y
       values'''
    s = (a[2] - b[2]) / (a[1] - b[1])
    intercept = b[2] - s*b[1]
    if slope == False:
        s = 0
        intercept = (a[2] + b[2]) / 2
    return 1, s, intercept


def simulate(slope=True):
    '''Generate two points and calculate the slope and intercept of the line
       created by them. If slope is passed at false, the average of the two
       points is calculated'''
    pointOne = genRandomPoint()
    pointTwo = genRandomPoint()
    a, s, intercept = calculateLineS(pointOne, pointTwo, slope)
    return s, intercept

def simulations(x, slope=True):
    '''Perform x iterations of the simulate function. Returns average slope and
       intercept'''
    data = [simulate(slope) for i in range(x)]
    s = sum([data[i][0] for i in range(x)]) / float(x)
    i = sum([data[i][1] for i in range(x)]) / float(x)
    return i, s

i, s = simulations(1000000, True)
#print "Question 4: The answer is " + str(s)


### Question 5

def gR():
    '''Generate a random value along [-1, 1]'''
    return random.uniform(-1, 1)

def biasOne(interceptValue, slopeValue, intercept=True):
    '''Input the g(bar) values for slope and intercept. A random point is generated
       and the bias is calculated for that point'''
    i = 1
    if intercept == False:
        i = 0
    xOne = gR()
    xTwo = gR()
    total = (slopeValue*xOne + interceptValue*i - math.sin(math.pi*xOne))**2 + (slopeValue*xTwo + interceptValue*i - math.sin(math.pi*xTwo))**2
    return total / float(2)

def getBias(trials, interceptValue, slopeValue, intercept=True):
    '''Repeat the biasOne function for "trials" number of points'''
    return sum([biasOne(interceptValue, slopeValue, intercept) for i in range(trials)]) / float(trials)


#print "Question 5: The answer is " + str(getBias(100000, 0, s, False))

### Question 6

def value(a, b, x):
    '''returns the y value for an x value with the given slope and intercept'''
    return a*x + b

def varOne(interceptValue, slopeValue, intercept = True, slope = True):
    '''Takes the g(bar) slope and intercept values as input.
       Returns ( for a randomly generated point) squared difference between
       randomly generated hypothesis (line) and the g(bar)'''
    pOne = genRandomPoint()
    pTwo = genRandomPoint()
    a, s, inter = calculateLineS(pOne, pTwo, slope) #get the slope and intercept values from two random points
    i = 1
    if intercept == False:
        i = 0
    valu = (value(s, inter*i, pOne[1]) - value(slopeValue, interceptValue, pOne[1]))**2
    valu2 = (value(s, inter*i, pTwo[1]) - value(slopeValue, interceptValue, pTwo[1]))**2
    return (valu + valu2) / float(2)

def getVar(x, interceptValue, slopeValue, intercept = True, slope = False):
    '''Repeats varOne function x-times'''
    return sum([varOne(interceptValue, slopeValue, intercept, slope) for i in range(x)]) / float(x)

#print "Question 6: The answer is " + str(getVar(100000, 0, s, False, True))

#Question 7

def genX(power, slope=True):
    '''Power is the power of the x-value (linear or quadratic).
       Slope refers to whether or not hypothesis = b
       Returns two X-matrixes. One with x-values^power, one with plain x-values'''
    xList = [(1, gR()**power) for i in range(2)]
    xAlt = [(1,math.pow(xList[i][1],1/float(power))) for i in range(2)]
    if slope == False:
        xList = [1 for i in range(2)]
        xList = numpy.matrix(xList)
        xList = numpy.matrix.transpose(xList)
    return numpy.matrix(xAlt), numpy.matrix(xList)

def genY(x):
    '''Creates Y matrix for the sin(pi x) function'''
    y = [[math.sin(math.pi*x[i,1])] for i in range(x.shape[0])]
    y = numpy.matrix(y)
    return y

def getWeights(X, Y):
    '''Linear regression weights'''
    X = numpy.matrix(X)
    Y = numpy.matrix(Y)
    Xt = numpy.matrix.transpose(X)
    weights = np.inv(Xt*X)*(Xt*Y)
    if numpy.size(weights) == 1:
        return weights, 0
    else:
        return weights

def eOutOne(power, slope=True, intercept=False):
    xA, xB = genX(power, slope)
    yM = genY(xA)
    i, s = getWeights(xB, yM)
    x1, x2 = gR(), gR()    
    if slope == True and intercept == False:
        return (s*(x1**power) - math.sin(math.pi*x1))**2 + (s*(x2**power) - math.sin(math.pi*x2))**2
    elif slope == True and intercept == True:
        return (s*(x1**power) + i - math.sin(math.pi*x1))**2 + (s*(x2**power) + i - math.sin(math.pi*x2))**2
    else:
        return (i - math.sin(math.pi*x1))**2 + (i - math.sin(math.pi*x2))**2

def getEOut(x, power, slope=True, intercept=False):
    return sum([eOutOne(power, slope=True, intercept=False) for i in range(x)]) / float(x)

#a = getEOut(100000, 1, False, True)
#b = getEOut(100000, 1, True, False)
#c = getEOut(100000, 1, True, True)
#d = getEOut(100000, 2, True, False)
#e = getEOut(100000, 2, True, True)

#print "The answer for 7A is " + str(a)
#print "The answer for 7B is " + str(b)
#print "The answer for 7C is " + str(c)
#print "The answer for 7D is " + str(d)
#print "The answer for 7E is " + str(e)
