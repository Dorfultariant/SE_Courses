######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 22.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T4.py

# (c) LUT 20221120 L11T4.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
###########################################################################
# Ohjelma, joka etsii sopivia numeroita

# Kirjastot:
import time
import sys


# Luokat:
class TULOKSET:
    Suurempi = None
    Pienempi = None

# Aliohjelmat:
def hakufunktio(Nimi, Luvut):
    Numerot = []
    # Luetaan tiedosto ensin listaan:
    try:
        Tiedosto = open(Nimi,'r')
        while(True):
            Rivi = Tiedosto.readline()
            if(len(Rivi) == 0):
                break
            Rivi = Rivi[:-1:]
            Luku = int(Rivi)
            Numerot.append(Luku)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
        
    # Lajitellaan lista:
    Lajiteltu = sorted(Numerot)
    # Haetaan lajitellusta listasta:
    Eka = Lajiteltu[0]
    i = 0
    while(i < len(Lajiteltu)):
        if(Eka < (Lajiteltu[i] / 3)):
            Luvut.Pienempi = Eka
            Luvut.Suurempi = Lajiteltu[i]
            break
        i += 1
    
    # Listojen tyhjennys:
    Numerot.clear()
    Lajiteltu.clear()
    return Luvut


# Pääohjelma:
def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
###########################################################################
# End of File