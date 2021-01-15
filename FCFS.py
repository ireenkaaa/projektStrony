def FCFS (memoryList, tempPage, timer):
    temp = 0
    for i in range((len(memoryList))-1):
        if memoryList[i][1] < memoryList[i + 1][1]:  # miejsce timera zapisanego w liscie
            temp = i
    memoryList[temp][0] = tempPage  # miejsce numeru strony
    memoryList[temp][1]= timer
    memoryList[temp][2] += 1  # miejsce licznika