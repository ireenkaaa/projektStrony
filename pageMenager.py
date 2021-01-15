from dataGenerator import generateDataRandom
from FCFS import FCFS
listPages = []
listTime = []
numberOfPages = 10
numberOfFrames = 5

generateDataRandom(listPages, numberOfPages)

def addPage (memoryList, timer, pageCounter):
    tempPage=listPages[pageCounter]
    isPageInMemory = False
    for i in range(len(memoryList)):
        if memoryList[i]==[0,0,0]:
            memoryList[i][0] = tempPage  # miejsce numeru strony
            memoryList[i][1] = timer
            memoryList[i][2] += 1
            break
        elif tempPage== memoryList[i][0]:#miejsce numeru strony
            isPageInMemory = True
            break
    if isPageInMemory==False:
       FCFS(memoryList , tempPage, timer)

    pageCounter+=1

    return pageCounter
