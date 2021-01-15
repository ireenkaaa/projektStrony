from pageMenager import numberOfPages, numberOfFrames, addPage
memory = []
timer = 0
listOfPages = []
for i in range(numberOfFrames):
    memory.append([0, 0, 0]) # [0] numer strony [1] timer [2] liczba użyć danej strony
pageCounter=0
for i in range (numberOfPages):
    pageCounter= addPage(memory,timer,pageCounter)
    print(memory)
    timer+=1
# generator wartosci przychodzacych do pamieci
# sprawdzenie czy dana wartosc znajduje się w ramce
# jesli nie to szukamy najstraszej wartosci (t max)
# jesli tak to idziemy do kolejnej wartosci
# licznik ilosci zmian w ramce
#


