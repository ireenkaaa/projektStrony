def LRU (memoryList, tempPage, timer):
    temp = 0
    number=memoryList[0][2]
    for i in range(1, len(memoryList)):
        if memoryList[i][2] < number:
            number = memoryList[i][2]
            temp=i
    memoryList[temp][0] = tempPage  # miejsce numeru strony
    memoryList[temp][1]= timer
    memoryList[temp][2]=timer