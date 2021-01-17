def FIFO (memoryList, tempPage, timer):
    temp = 0
    number=memoryList[0][1]
    for i in range(1, len(memoryList)):
        if memoryList[i][1] < number:
            number = memoryList[i][1]
            temp=i
    memoryList[temp][0] = tempPage  # miejsce numeru strony
    memoryList[temp][1]= timer
    memoryList[temp][2] += 1  # miejsce licznika