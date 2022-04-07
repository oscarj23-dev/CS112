#Oscar Maldonado
#visualizeIncome.py
#11/21/21

import matplotlib.pyplot as plt

#reading in the file line by line and returning a list
def readFile(filename):
    with open("/Users/oscarmaldonado/Desktop/py4e/CS112/lab16/" + filename, "r") as file:
        lines = file.readlines()
        return lines

#filtering the data from the file by putting it through a set to remove duplicates then returning those lists
def processData(data):
    data = list(set(data))
    id = []
    salaries = []
    bonus = []
    names = []
    for i in range(len(data)):
        line = data[i]
        id, names, salaries, bonus = line.split(',')
        print(id,names, salaries, bonus)

    return id, salaries, bonus

#graph function to show graph 
def graph(id, salary, bonus):
    plt.bar(id, salary, width = 0.8, label = "salary", color = "blue")
    plt.bar(id, bonus, width = 0.8, label = "bonus", color = "red", bottom= float(salary))

    plt.xticks(id)
    plt.ylabel("Total Salary")
    plt.xlabel("Employee ID")
    plt.legend(loc = "upper right")
    plt.show()

#graph function to show graph in reverse 
def graphReverse(id, salary, bonus):
    plt.bar(id, bonus, width = 0.8, label = "bonus", color = "blue")
    plt.bar(id, salary, width = 0.8, label = "salary", color = "red", bottom= float(salary))

    plt.xticks(id)
    plt.ylabel("Total Salary")
    plt.xlabel("Employee ID")
    plt.legend(loc = "upper right")
    plt.show()

#run function that calls all the other functions
def run():
    lis = readFile("employees.txt")
    id, salary, bonus = processData(lis)
    graph(id, salary, bonus)
    graphReverse(id, salary, bonus)

run()