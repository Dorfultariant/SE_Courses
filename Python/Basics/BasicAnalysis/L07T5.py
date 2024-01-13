######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 25.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T5.py

# Globaalit kiintoarvot:
EROTIN = ';'

# Luokat:
class AUTO:
    Merkki = ""
    Hinta = 0

# Aliohjelmat:
def valikko():
    Valinta = 0
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("3) Tallenna autojen tiedot tiedostoon")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta



def autoTiedot(OlioLista):
    AutoN = AUTO()
    AutoN.Merkki = input("Anna auton merkki: ")
    AutoN.Hinta = input("Anna auton hinta: ")
    AutoN.Hinta = int(AutoN.Hinta)
    
    # Lisätään auton tiedot oliolistaan:
    OlioLista.append(AutoN)

    # Palautetaan muokattu oliolista:
    return OlioLista



def tulostaAutojenTiedot(ListaAutoista):
    print("Listalta löytyy seuraavat autot ja hinnat:")

    for auto in ListaAutoista:
        print(auto.Merkki, auto.Hinta)
        
    return None



def kirjoitaTiedosto(TiedostoKirjaa, ElioLista):
    Tiedosto = open(TiedostoKirjaa,'w',encoding="utf-8")

    Tiedosto.write("Auton merkki;Auton hinta\n")
    for elio in ElioLista:
        Tiedosto.write(elio.Merkki + EROTIN + str(elio.Hinta) + "\n")
    Tiedosto.close()

    return None



# Pääohjelma:
def paaohjelma():
    # Alustus:
    Toiminto = 0
    KirjoitettavaTiedosto = ""
    AutoLista = []

    # Alkukysely ja tulostus:
    KirjoitettavaTiedosto = input("Anna tallennettavan tiedoston nimi: ")
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")
    

    while(True):
        # Valikon tulostus:
        Toiminto = valikko()
 
        if(Toiminto == 1):
            AutoLista = autoTiedot(AutoLista)
            
        elif(Toiminto == 2):
            tulostaAutojenTiedot(AutoLista)

        elif(Toiminto == 3):
            kirjoitaTiedosto(KirjoitettavaTiedosto, AutoLista)
            print("Tapahtumat kirjoitettu tiedostoon '{}'.".format(KirjoitettavaTiedosto))

        elif(Toiminto == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()

    # Poistetaan oliolista:
    del AutoLista

    # Lopputulostus:
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

# Päätaso:
paaohjelma()

# End of File