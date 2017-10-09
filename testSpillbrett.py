from random import randint
rader = 10
kolonner = 5

brett = []

for i in range(rader):
    rad = []
    for j in range(kolonner):
        rad.append("O")
    brett.append(rad)

print(brett)

for rad in brett:
    for celle in rad:
        print(celle, end=" ")
    print()


def generer(brett, rader, kolonner):
    for i in range(rader):
        for j in range(kolonner):
            tall = randint(0,3)
            if tall == 3:
                brett[i][j] = "I"            

generer(brett, rader, kolonner)
print(brett)

for rad in brett:
    for elem in rad:
        s = 