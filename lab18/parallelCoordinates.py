#Oscar Maldonado
#roughDraft.py
#12/2/21
import pandas
import plotly.express as px

#reading in the labels file and returning a list
def readLabels(filename):
    with open("/Users/oscarmaldonado/Desktop/py4e/CS112/lab18/" + filename) as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.split(",")
        return tokens

#reading in the data file, casting all the elemnets to ints and returning a dataframe
def readData(filename, labels):
    numbers = []
    with open("/Users/oscarmaldonado/Desktop/py4e/CS112/lab18/" + filename) as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.split("\t")
            tokens[0] = int(tokens[0])
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            tokens[3] = int(tokens[3])
            tokens[4] = int(tokens[4])
            tokens[5] = int(tokens[5])
            tokens[6] = int(tokens[6])
            tokens[7] = int(tokens[7])
            tokens[8] = int(tokens[8])
            numbers.append(tokens)
            
        dataFrame = pandas.DataFrame(numbers, columns = labels)
        return dataFrame

#displays graph
def graph(data, labels):
    figure = px.parallel_coordinates(data_frame = data, color = 'class', dimensions = labels)
    figure.show()
lines = readLabels("labels.txt")
data_Frame = readData("data.txt", lines)
graph(data_Frame, lines[:-1])