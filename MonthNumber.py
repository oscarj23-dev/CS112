#Oscar Maldonado
#Lab #2
#9/29/2021

thisMonth = input("What month is this? ")
monthNumber = input("What is the month number? ")
nextMonth = input("What is the next month? ")
print("Right now it is", thisMonth, "Which is month number", monthNumber, ".")

if (int(monthNumber) == 12):
    monthNumber = 0

print("Next month it is", nextMonth, "which is month number", int(monthNumber) + 1)

