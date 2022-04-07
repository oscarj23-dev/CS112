#Oscar Maldonado
#10/19/2021
#anonymousFunctions

#takes two parameters and adds them togehter
addTwo = lambda a, b: (a + b)
sum = addTwo(9,9)
print("Add two:", sum)

#takes three parameters and adds them togehter and finds the average
averageThree = lambda a, b, c: (a + b + c) / 3
sum = averageThree(1,2,3)
print("Average three:", round(sum, 2))

#takes one parameter and is multiplied to the power of three
powerThree = lambda a: (a) ** 3
product = powerThree(5)
print("powerThree:", product)

#takes no parameter and prints hello world
info = lambda: "Hello World"
print("info:", info())

#takes one parameter and strips it and converts it to lowercase
lowerString = lambda a: (a.strip().lower())
string = lowerString("CWU        ")
print("lowerString:", string)
 
#takes one parameter and strips it and converts it to uppercase and takes substrings from [1:4]
upperString = lambda a: (a[1:4].strip().upper())
string = upperString("ccwUUuUu        ")
print("UpperString:", string)

#takes one parameter and splits the list in half only printing the first half
halfList = lambda a: a[:len(a)//2]
lis = halfList([1,2,3,4,5,6])
print("first half of the list:", lis)