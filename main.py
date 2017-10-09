from celle import Celle
from spillebrett import Spillbrett

def main():
    antallRader = int(input("Oppgi antall rader: "))
    antallKolonner = int(input("Oppgi antall kolonner: "))

    brett = Spillbrett(antallRader, antallKolonner)
    brett.tegnBrett()

    svar = input("Trykk enter for aa fortsette, for aa fortsette press q og enter: ")
    while svar != "q":
        brett.oppdatering()
        brett.tegnBrett()
        print("Generasjon: {} -- Antall levende celler: {}".format(brett.hentGenerasjon(), brett.finnAntallLevende()))
        svar = input("Trykk enter for aa fortsette, for aa fortsette press q og enter: ")


main()

