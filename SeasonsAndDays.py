#Oscar Maldonado
#Lab #5
#10/7/2021
import sys
weekday = input("Please enter a number 1-7: ")
day = ""
month = ""

#chain of if elifs that dictate what day it is based on user input
#program will exit if anything >7 is entered
if int(weekday) == 1:
    day = "monday"
elif int(weekday) == 2:
    day = "tuesday"
elif int(weekday) == 3:
    day = "wednesday"
elif int(weekday) == 4:
    day = "thrusday"
elif int(weekday) == 5:
    day = "friday"
elif int(weekday) == 6:
    day = "saturday"
elif int(weekday) == 7:
    day = "sunday"
else:
    print("incorrect number was entered.")
    sys.exit()

#four lists for the seasons
spring = ["spring", "Spring", "SPRING"]
summer = ["summer", "Summer", "SUMMER"]
fall = ["fall", "Fall", "FALL"]
winter = ["winter", "Winter", "WINTER"]

season = input("What season is it? ")

#chain of if elifs and nested logic structures to determine what season and month the user is in.
#program will cleanly exit if something that is not a season is entered
if season == spring[0] or season == spring[1] or season == spring[2]:
    month = "march"
    print("The day is", day, "which is day number:", weekday)
    print("The month is", month, "which is in the", season)
elif season == summer[0] or season == summer[1] or season == summer[2]:
    if int(weekday) <= 3:
        month = "june"
        print("The day is", day, "which is day number:", weekday)
        print("The month is", month, "which is in the", season)
    else:
        month = "july"
        print("The day is", day, "which is day number:", weekday)
        print("The month is", month, "which is in the", season)
        if int(weekday) == 6:
            print("Go swimming!")
elif season == fall[0] or season == fall[1] or season == fall[2]:
    month = "september"
    print("The day is", day, "which is day number:", weekday)
    print("The month is", month, "which is in the", season)
elif season == winter[0] or season == winter[1] or season == winter[2]:
    month = "december"
    print("The day is", day, "which is day number:", weekday)
    print("The month is", month, "which is in the", season)
else:
    print("that is not a season.")
    sys.exit()