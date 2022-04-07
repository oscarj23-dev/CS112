"""
Date: 10/14/2021
File: myOwnFunctions
Author: Oscar Maldonado
"""
#function 1 which creates the list from 1 - 13 inclusive
def creatList(start = 0, end = 0 , increment = 0):
    nums = []
    for i in range(start, end, increment):
        nums.append(i)
    return nums
lis = creatList(1, 14, 1)

#function 2 which sums up all of the elements in the list from function 1
def sum(nums):
    add = 0
    for i in nums:
        add += i
    print(add)
    return add
total = sum(lis)

#function 3 which multplies all of the elements in the list from function 1
def product(nums):
    x = nums[0]
    for i in nums:
        x *= i
    print(x)
    return x
total = product(lis)

#function 4 which determines what elements are even and prints them out.
def evenOdd(nums):
    for i in nums:
        if i % 2 == 0:
            print(i, end=",")
evenOdd(lis)

