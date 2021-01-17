from dataGenerator import generateDataRandom, generateDataFromFile
from FIFO import FIFO
from LRU import LRU


def addPage(memoryList, timer, pageCounter, listPages,globalCounter):
    tempPage = listPages[pageCounter]
    isPageInMemory = False
    for i in range(len(memoryList)):
        if tempPage == memoryList[i][0]:  # miejsce numeru strony
            isPageInMemory = True
            memoryList[i][2]=timer
            break
    if [0, 0, 0] in memoryList and isPageInMemory==False:
        i = memoryList.index([0, 0, 0])
        memoryList[i][0] = tempPage  # miejsce numeru strony
        memoryList[i][1] = timer
        memoryList[i][2] =timer


    elif isPageInMemory == False:
        #FIFO(memoryList, tempPage, timer)
        LRU(memoryList,tempPage,timer)
        globalCounter[0] += 1


    pageCounter += 1

    return pageCounter
