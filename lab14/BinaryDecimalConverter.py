#Oscar Maldonado
#BinaryDecimalConverter
#11/10/2021

#This method converts a decimal number to its binary form
def decimalToBinary(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]
    return binary

#This method converts a binary number to its decimal form
def binaryToDecimal(num):
    total = 0
    power = 0
    for i in reversed(num):
        total += int(i) * 2**power
        power += 1
    return total
    
for i in range(135, 146):
    binary = decimalToBinary(i)
    decimal = binaryToDecimal(binary)
    print(decimal, "is", binary, "in binary")