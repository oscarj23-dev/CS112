#Oscar Maldonado
#BinaryDecimalConverter
#11/10/2021

def decimalToBinary(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num = num // 2
    binary = binary[::-1]
    return binary

def binaryToDecimal():
    pass

bin = decimalToBinary(125)
print(bin)
