from pageMenager import addPage
from dataGenerator import generateDataRandom, generateDataFromFile
memory = []
timer = 0
listPages = []
numberOfPages = 12
numberOfFrames = 4
globalCounter=[0]
generateDataFromFile(listPages, numberOfPages)


for i in range(numberOfFrames):
    memory.append([0, 0, 0]) # [0] numer strony [1] przybycie strony [2] ostatnia modyfikacja strony
pageCounter=0
for i in range (numberOfPages):
    pageCounter= addPage(memory,timer,pageCounter, listPages,globalCounter)
    for i in range(len(memory)):

        print("["+str(memory[i][0])+"]", end='')

    print()
   # print(memory)

    timer+=1
print(globalCounter[0])



