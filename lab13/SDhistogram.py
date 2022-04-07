#Oscar Maldonado
#SDhistogram.py
#11/7/21
import math
import matplotlib.pyplot as plt

#reads in the file data and splits it on '\n' and returns that list
def readFile(fileName):
    with open(fileName, "r") as file:
        lines = file.read()
        nums = lines.split('\n')
    return nums

#calculates the mean of the data in the file
def calculateMean(nums):
    total = 0
    for i in nums:
        total += int(i)
    mean = total / len(nums)
    print("The mean is :", mean)
    return mean

#calculates the variance of the data in the file
def variance(nums, mean):
    total = 0
    for i in nums:
        total += (int(i) - mean) ** 2    
    print("The variance is :", total / len(nums))
    return total / len(nums)

#calculates the standard deviation of the data
def calculateSD(var):
    sd = math.sqrt(var)
    print("The Standard Deviation is :", sd)
    return sd

#displays the histogram
def showHistogram(nums):
    numBins = 10
    plt.hist(nums, numBins)
    plt.show()

lis = readFile("/Users/oscarmaldonado/Desktop/py4e/CS112/lab13/data_3.txt")
avg = calculateMean(lis)
var = variance(lis, avg)
sd = calculateSD(var)
showHistogram(lis)