from random import randint
from celle import Celle

class Spillbrett():
    def __init__(self, rader, kolonner):
        self.rader = rader
        self.kolonner = kolonner
        self.generasjonsnummer = 0
        self.brett = []

        for i in range(self.rader):
            rad = []
            for j in range(self.kolonner):
                rad.append(Celle())
            self.brett.append(rad)

        self.generer()
        

    def generer(self):
        for i in range(self.rader):
            for j in range(self.kolonner):
                tall = randint(0,3)
                if tall == 3:
                    self.brett[i][j].settLevende()  
            
    def tommeLinjer(self):
        for i in range(5):
            print()

    def tegnBrett(self):
        self.tommeLinjer()
        for rad in self.brett:
            for celle in rad:
                print(celle.hentTegnrepresentasjon(), end="")
            print()

    def oppdatering(self):
        bliLevende = []
        bliDode = []
        for i in range(self.rader):
            for j in range(self.kolonner):
                celle = self.brett[i][j]
                naboer = self.finnNabo(i, j)
                levendeNaboer = 0
                for nabo in naboer:
                    if nabo.erLevende() == True:
                        levendeNaboer += 1
                
                if celle.erLevende() == True:
                    if levendeNaboer > 3 or levendeNaboer < 2:
                        bliDode.append(celle)
                else:
                    if levendeNaboer == 3:
                        bliLevende.append(celle)
        
        for celle in bliLevende:
            celle.settLevende()
        for celle in bliDode:
            celle.settDod()
        
        self.generasjonsnummer += 1
                

    def finnNabo(self, x, y): #TODO skriv denne metoden paa din egen maate
        naboliste = []
        for i in range (-1, 2):
            for j in range (-1, 2):
                naboX = x+i
                naboY = y+j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self.kolonner -1 or naboY > self.rader-1) != True:
                        naboliste.append(self.brett[naboX][naboY])
        return naboliste
    
    def finnAntallLevende(self):
        antallLevende = 0
        for rad in self.brett:
            for celle in rad:
                if celle.erLevende() == True:
                    antallLevende += 1
        return antallLevende
    

    def hentGenerasjon(self):
        return self.generasjonsnummer

