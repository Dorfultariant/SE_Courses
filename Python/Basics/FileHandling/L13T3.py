######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 8.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T3.py

# Kirjastot:
import datetime
import sys

# Kiintoarvot:
LUKUEROTIN = ';'
PVMFORMAATTI = "%A, %d %B %Y, %I:%M %p"

class TIEDOT:
    T1 = None
    T2 = None
    T3 = None
    T4 = None
    T5 = None

# Aliohjelmat:
def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot viikonpäivittäin")
    print("0) Lopeta")
    Syote = input("Valintasi: ")
    Valinta = int(Syote)
    return Valinta

def kysyNimi(Kehote):
    Nimi = input("Anna {} tiedoston nimi: ".format(Kehote))
    return Nimi

def lueTiedosto(Nimi, Luettu):
    # Alustus:
    Luettu = []
    Pvm = None
    
    try:
        Tiedosto = open(Nimi,'r',encoding="utf-8")

        Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while(len(Rivi) != 0):
            Rivi = Rivi[:-1:]
            Sarake = Rivi.split(LUKUEROTIN)

            Tiedot = TIEDOT()
            Tiedot.T1 = datetime.datetime.strptime(Sarake[0], PVMFORMAATTI)
            Tiedot.T2 = datetime.datetime.strptime(Sarake[1], PVMFORMAATTI)
            Tiedot.T3 = datetime.datetime.strptime(Sarake[2], PVMFORMAATTI)
            Tiedot.T4 = datetime.datetime.strptime(Sarake[3], PVMFORMAATTI)
            Tiedot.T5 = datetime.datetime.strptime(Sarake[4], PVMFORMAATTI)
            Tiedot.T1 = datetime.datetime.strftime(PVMFORMAATTI).lstrip('0').replace(' 0', ' ')
            Tiedot.T2 = datetime.datetime.strftime(PVMFORMAATTI).lstrip('0').replace(' 0', ' ')
            Tiedot.T3 = datetime.datetime.strftime(PVMFORMAATTI).lstrip('0').replace(' 0', ' ')
            Tiedot.T4 = datetime.datetime.strftime(PVMFORMAATTI).lstrip('0').replace(' 0', ' ')
            Tiedot.T5 = datetime.datetime.strftime(PVMFORMAATTI).lstrip('0').replace(' 0', ' ')
            
            Rivi = Tiedosto.readline()
            
        Tiedosto.close()

    except Exception as virhe:
        print("Tiedoston '{}' käsittelyssä virhe {}, lopetetaan.".format(Nimi, virhe))
        sys.exit(0)


    return Luettu

def analysoi(Luettu):
    # Alustus:
    Palautukset = {}

    for Olio in Luettu:
        # Tehtävä 1, T1
        #Paiva = Olio.T1.weekday()
        Palautukset[Olio.T1.strftime("%A")] += 1
        # Tehtävä 2, T2
        #Paiva = Olio.T2.weekday()
        #Palautukset[Paiva] = Palautukset[Paiva] + 1
        Palautukset[Olio.T2.strftime("%A")] += 1
        # Tehtävä 3, T3
        #Paiva = Olio.T3.weekday()
        #Palautukset[Paiva] = Palautukset[Paiva] + 1
        Palautukset[Olio.T3.strftime("%A")] += 1
        # Tehtävä 4, T4
        #Paiva = Olio.T4.weekday()
        #Palautukset[Paiva] = Palautukset[Paiva] + 1
        Palautukset[Olio.T4.strftime("%A")] += 1
        # Tehtävä 5, T5
        #Paiva = Olio.T5.weekday()
        #Palautukset[Paiva] = Palautukset[Paiva] + 1
        Palautukset[Olio.T5.strftime("%A")] += 1
        
        

    return Palautukset

def tulostaTiedot(Palautukset):
    print(TULOSTUSEROTIN + "Palautuksia viikonpäivittäin")
    for Avain, Arvo in Palautukset.items():
        print(Palautukset[Paiva] + TULOSTUSEROTIN + Palautukset[Maara])

    return None



def paaohjelma():
    # Alustus:
    Luettu = []
    Palautukset = []
    
    while(True):
        Valinta = valikko()

        if(Valinta == 1):
            NimiLue = kysyNimi("luettavan")
            Luettu = lueTiedosto(NimiLue, Luettu)

        elif(Valinta == 2):
            Palautukset = analysoi(Luettu, Palautukset)
            tulostaTiedot(Palautukset)

        elif(Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    return None

paaohjelma()

# End of File

## L13T3D1.txt