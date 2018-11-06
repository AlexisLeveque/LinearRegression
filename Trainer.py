import matplotlib.pyplot as plt
import re

learningRate = 0.015


def estimatePrice(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def sommeTheta0(kms, prices, theta0, theta1):
    res = 0
    for i in range(len(kms)):
        res += estimatePrice(kms[i], theta0, theta1) - prices[i]
    return res


def sommeTheta1(kms, prices, theta0, theta1):
    res = 0
    for i in range(len(kms)):
        res += (estimatePrice(kms[i], theta0, theta1) - prices[i]) * kms[i]
    return res


def minimize(dataSet, maxi):
    newDataSet = []
    for data in dataSet:
        newDataSet.append(data / maxi)
    return newDataSet


def getDatas(file):
    pattern = re.compile("([0-9.\-]+),([0-9.\-]+)")
    kms = []
    prices = []
    file.readline()
    for line in file.readlines():
        try:
            match = re.match(pattern, line)
            km = match.group(1)
            price = match.group(2)
            kms.append(float(km))
            prices.append(float(price))
        except:
            print("Bad data.")
            exit(0)
    return kms, prices


file = open("data.csv", "r")

kms, prices = getDatas(file)

kmMax = max(kms)
priceMax = max(prices)

Mkms = minimize(kms, kmMax)
Mprices = minimize(prices, priceMax)

theta0 = 0
theta1 = 0
dataLen = len(Mkms)
for i in range(20000):
    tmpTheta0 = learningRate * (1/dataLen) * sommeTheta0(Mkms, Mprices, theta0, theta1)
    tmpTheta1 = learningRate * (1/dataLen) * sommeTheta1(Mkms, Mprices, theta0, theta1)
    theta0 = theta0 - tmpTheta0
    theta1 = theta1 - tmpTheta1

for i in range(dataLen):
    plt.plot(kms[i], prices[i], 'ro')

theta0 = theta0*priceMax

theta1 = theta1*priceMax/kmMax

def f(x, theta0, theta1):
    return theta1 * x + theta0


plt.plot([0, 300000], [f(0, theta0, theta1), f(300000, theta0, theta1)])

plt.axis([0, 250000, 3000, 9000])

plt.show()

file2 = open("theta", "w")
file2.write("%s,%s" % (theta0, theta1))
