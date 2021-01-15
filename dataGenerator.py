from random import randint
def saveToFileBefore(list, name):
    with open(name, 'w') as file:
        for item in list:
            file.write("%s\n" % item)

def saveToFileAfter(list, name):
    temp = 0
    for i in range(len(list)):
        temp = temp + list[i][3]
    averageWaitingTime = temp / len(list)
    with open(name, 'w') as file:
        file.write("Numer procesu   Czas trwania  Czas przyjscia  Czas oczekiwania \n")
        for item in list:
            for i in item:
                file.write("%s              " % i)
            file.write("\n")
        file.write("\n")
        file.write("Średni czas oczekiwania to: "+ str(averageWaitingTime))

def generateDataRandom(listPages, numberOfPages):
    for i in range(numberOfPages):
        listPages.append(randint(1, numberOfPages))

    saveToFileBefore(listPages, "numbersOfPages")


def generateDataZero(listTimes, listDuration, numberOfProcesses):
    for i in range(numberOfProcesses):
        listTimes.append(0)
        listDuration.append(randint(1, 7))
    saveToFileBefore(listTimes, "time")
    saveToFileBefore(listDuration, "duration")