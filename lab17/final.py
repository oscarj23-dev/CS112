#Oscar Maldonado
#Final.py
#12/4/21

#reading in the file line by line and returning a list
def readFile(filename):
    with open("/Users/oscarmaldonado/Desktop/py4e/CS112/lab17/" + filename, "r") as file:
        lines = file.readlines()
        return lines

#filtering the data from the file, reading the data into lists then returning those lists
def processData(data):
    description = []
    time = []
    amount = []
    category = []
    
    for i in range(len(data)):
        line = data[i]
        lines = line.split(",")
        for x in range(len(lines)):
            description.append(lines[0])
            time.append(lines[1])
            amount.append(lines[2])
            category.append(lines[3])
        print(line)
        
    return description, time, amount, category

#Calculates how much was spent within the time given, projects how much will be
#spent in one year if the same rate of expenditure is maintained, and the avg
#amount spent with each transaction. Data is put through a set to filter any duplicates.
def calculations(amount):
    total = 0
    avg = 0
    amount = list(set(amount))
    for i in amount:  
        i.strip()    
        total += round(float(i), 2)
        avg = round(total / len(amount), 2)
    print("total amount spent over 3 month period:", total)
    print("average spent per purchase:", avg)
    print("projected amount over 1 year in expenses:", total * 4)

#run function that calls all the other functions
def run():
    lis = readFile("expenses.txt")
    description, time, amount, category = processData(lis)
    calculations(amount)
run()