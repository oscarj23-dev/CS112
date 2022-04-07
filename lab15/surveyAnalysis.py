#Oscar Maldonado
#surveyAnalysis.py
#11/18/21

import matplotlib.pyplot as plt

#reading in the file
with open("/Users/oscarmaldonado/Desktop/py4e/CS112/lab15/surveyData.txt", "r") as file:
    lines = file.readlines()
   #print(lines)
work = [0, 0, 0, 0, 0] #[] very happy      []happy      [] neutral        [] unhappy     [] very unhappy
pet = [0, 0, 0, 0, 0] #[] strongly agree     [] agree      [] neutral        [] disagree     [] strongly disagree 

answersWork = ["very happy", "happy", "neutral", "unhappy", "very unhappy"]
answersPet = ["very agree\n", "agree\n", "neutral\n", "disagree\n", "very disagree\n"]

#Chain if elifs to determine how the right list becomes incremented.
for i in range(len(lines)):
    line = lines[i]
    choice1, choice2 = line.split(',')

    if choice1 == answersWork[0]:
        work[0] += 1
    elif choice1 == answersWork[1]:
        work[1] += 1
    elif choice1 == answersWork[2]:
        work[2] += 1
    elif choice1 == answersWork[3]:
        work[3] += 1
    elif choice1 == answersWork[4]:
        work[4] += 1

    if choice2 == answersPet[0]:
        pet[0] += 1
    elif choice2 == answersPet[1]:
        pet[1] += 1
    elif choice2 == answersPet[2]:
        pet[2] += 1
    elif choice2 == answersPet[3]:
        pet[3] += 1
    elif choice2 == answersPet[4]:
        pet[4] += 1

#histogram method to show the data visually`
def showHistogram(list, bars):
    plt.bar(bars, list)
    plt.show()

showHistogram(work, answersWork)

print(work)
print(pet)
