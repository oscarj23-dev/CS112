#Oscar Maldonado
#10/31/2021
#createHouseData.py

import random
random.seed()

with open("HouseData.txt", "a") as file:
    #here we create a small convenient method to decide bedroom size
    def room():
        bedroom = random.randint(1, 4)
        return bedroom

    #initialize the variables needed for the program
    rooms = room()
    garage = random.randint(1, 3)
    stories = random.randint(1, 2)
    roof = ["gable", "hip", "shed"]
    deck = bool(random.getrandbits(1))
    roofStyle = roof[random.randint(0,2)]
    
    #for loop to calculate the sqfootage needed based on the amount of rooms the house has
    for i in range(1, 5, 1):
        if rooms == i:
            squarefootage = random.randint(500 * i, 1000 + i * 500 - 500 )

    #appending the info to the file
    file.write(str(squarefootage) + "," + str(rooms) + "," + str(garage) + "," + str(deck) + "," + roofStyle + "," + str(stories) + "\n")



