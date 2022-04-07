#Author : Oscar Maldonado
#Date : 9/23/2021
#File : rectangle.py

info = "calculate the perimeter and area of the rectangle"
print(info)

width = int(input("what is the width? "))
length = int(input("what is the length? "))

print("--------")
print("calculating")
print("--------")

perimeter = 2 * (width + length)

area = width * length

print("the width of the rectangle is: " , width)
print("the length of the rectangle is: ", length)
print("the perimeter of the rectangle is: ", perimeter)
print("the area of the rectangle is: ", area)