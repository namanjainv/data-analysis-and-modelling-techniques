import sys
import math
import random

seed = 1343
random.seed(seed)

def generateBernoulliData(p):
    u = random.random()
    if u <= p:
        return 1
    else:
        return 0

def generateBinomialData(n, p):
    x = 0
    for i in range(n):
        x = x + generateBernoulliData(p)
    return x

def generateGeometricData(p):
    x = 0
    while(True):
        u = generateBernoulliData(p)
        x = x + 1
        if u == 1:
            break
    return x

def generateNegativeBinomialData(k, p):
    x = 0
    count = 0
    while(count != k):
        y = generateGeometricData(p)
        x = x + y
        count = count + 1
    return x

def generateArbitraryDiscreteData(n, p):
    cdf = [0]                    # Values for F(x)
    sum_probablities = 0
    classes = len(p)
    for i in range(len(p)):
        sum_probablities = sum_probablities + p[i]
        cdf.append(sum_probablities)

    x = []
    for i in range(n):
        u = random.random()
        index = 0
        for j in range(1, len(cdf)):
            if(cdf[j] > u and u >= cdf[j-1]):
                x.append(index)
            index = index + 1
    return x

def myFactorial(x):
    if x == 0:
        return 1
    else:
        return x*myFactorial(x-1)

def generatePoissonData(n, _lambda):

    x = []
    c = float(math.exp(-_lambda))

    for j in range(n):

        f = math.exp(-_lambda)
        u = random.random()
        i = 0

        # f = f + (c*_lambda**i)/
        while u >= f:
            f = f + math.exp(-_lambda)*(_lambda**i)/myFactorial(i)
            i = i+1
        x.append(i-1)
    return x

def generateUniformData(n, a, b):
    x = []

    for i in range(n):
        u = random.random()
        x.append(a + u*(b-a))
    return x

def generateExponentialData(n, _lambda):
    x = []

    for i in range(n):
        u = random.random()
        x.append(-(math.log(1-u))/_lambda)
    return x

def generateGammaData(n ,alpha, _lambda):
    x = []

    for i in range(n):
        v = generateExponentialData(alpha, _lambda)
        u = 0
        for j in range(len(v)):
            u = u + v[j]
        x.append(u)
    return x

def generateNormalData(n, mean, std_deviation):
    x = []

    for i in range(int(n/2)+1):
        u1 = random.random()
        u2 = random.random()
        a = math.sqrt(-2*math.log(u1))
        b = 2*math.pi*u2
        Z0 = a*math.cos(b)
        Z1 = a*math.sin(b)
        x.append(Z0*std_deviation + mean)
        x.append(Z1*std_deviation + mean)
    print str(x[:samples_count])

def __main__(argv):
    samples_count = int(argv[1])
    distribution = argv[2].lower()
    if distribution == "bernoulli":
        data = []
        for i in range(samples_count):
            data.append(generateBernoulliData(float(argv[3])))
        print "Samples: " + str(data)
    elif distribution == "binomial":
        data = []
        for i in range(samples_count):
            data.append(generateBinomialData(int(argv[3]), float(argv[4])))
        print "Samples: " + str(data)
    elif distribution == "geometric":
        data = []
        for i in range(samples_count):
            data.append(generateGeometricData(float(argv[3])))
        print "Samples: " + str(data)
    elif distribution == "neg-binomial":
        data = []
        for i in range(samples_count):
            data.append(generateNegativeBinomialData(int(argv[3]), float(argv[4])))
        print "Samples " + str(data)
    elif distribution == "poisson":
        data = generatePoissonData(samples_count, float(argv[3]))
        print "Samples: " + str(data)
    elif distribution == "arb-discrete":
        mylist=[float(i) for i in argv[3:]]
        data = generateArbitraryDiscreteData(samples_count, mylist)
        print "Samples: " + str(data)
    elif distribution == "uniform":
        data = generateUniformData(samples_count, float(argv[3]), float(argv[4]))
        print "Samples: " + str(data)
    elif distribution == "exponential":
        data = generateExponentialData(samples_count, float(argv[3]))
        print "Samples: " + str(data)
    elif distribution == "gamma":
        data = generateGammaData(samples_count, int(argv[3]), float(argv[4]))
        print "Samples: " + str(data)
    elif distribution == "normal":
        data = generateNormalData(samples_count, float(argv[3]), float(argv[4]))
        print "Samples: " + str(data[:samples_count])
    else:
        print "Wrong Input"

__main__(sys.argv)