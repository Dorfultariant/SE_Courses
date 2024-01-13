######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 2.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T3.py

# Kirjastot:
import jsonpickle
import sys



# Kiintoarvot:
CSVEROTIN = ';'

# Luokat:
class TIEDOT:
    Nimike = None
    Tekija = None
    ISBN = None
    Varauksia = None
    Niteita = None
    Lisakpl = None
    Varaukset = None
    Nide = None


# Aliohjelmat:
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto")
    print("2) Lue JSON tiedosto")
    print("3) Kirjoita CSV tiedosto")
    print("4) Kirjoita JSON tiedosto")
    print("0) Lopeta")
    Syote = input("Anna valintasi: ")
    Valinta = int(Syote)
    return Valinta

def kysyNimi(Kehote):
    Nimi = input("Anna {} tiedoston nimi: ".format(Kehote))
    return Nimi


def lueCSV(Nimi, Luettu, Olio):
    # Alustus:
    Luettu = []
    try:
        Tiedosto = open(Nimi,'r',encoding="utf-8")
        Tiedosto.readline()
        while(True):
            Rivi = Tiedosto.readline()
            if(len(Rivi) == 0):
                break

            Rivi = Rivi[:-1:]
            Sarake = Rivi.split(CSVEROTIN)

            Olio.Nimike = Sarake[0]
            Olio.Tekija = Sarake[1]
            Olio.ISBN = Sarake[2]
            Olio.Varauksia = Sarake[3]
            Olio.Niteita = Sarake[4]
            Olio.Lisakpl = Sarake[5]
            Olio.Varaukset = Sarake[6]
            Olio.Nide = Sarake[7]

            Luettu.append(Olio)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan".format(Nimi))
        sys.exit(0)

    print("Luettu {} kirjan tiedot.".format(len(Luettu)))
    return Luettu

def lueJSON(Nimi, Luettu):
    # Alustus:
    Luettu = []
    try:
        Tiedosto = open(Nimi,'r', encoding="utf-8")
        Koodattu = Tiedosto.read()
        Luettu = jsonpickle.decode(Koodattu)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu {} kirjan tiedot.".format(len(Luettu)))
    return Luettu

def kirjoitaCSV(Nimi, Luettu):
    try:
        Tiedosto = open(Nimi,'w',encoding="utf-8")
        Tiedosto.write()
        while(True):
            Rivi = Tiedosto.readline()
            if(len(Rivi) == 0):
                break

            Rivi = Rivi[:-1:]
            Sarake = Rivi.split(CSVEROTIN)

            Olio.Nimike = Sarake[0]
            Olio.Tekija = Sarake[1]
            Olio.ISBN = Sarake[2]
            Olio.Varauksia = Sarake[3]
            Olio.Niteita = Sarake[4]
            Olio.Lisakpl = Sarake[5]
            Olio.Varaukset = Sarake[6]
            Olio.Nide = Sarake[7]

            Luettu.append(Olio)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan".format(Nimi))
        sys.exit(0)

    return None


def kirjoitaJSON():

    return None



# Pääohjelma:
def paaohjelma():
    # Alustus:
    Luettu = []

    # Luodaan Tiedot olio:
    Tiedot = TIEDOT()

    while(True):
        # Tulostetaan valikko ja kysytään valinta:
        Valinta = valikko()
        if(Valinta == 1):
            NimiLueCSV = kysyNimi("luettavan CSV")
            lueCSV(NimiLueCSV, Luettu, Tiedot)
        
        elif(Valinta == 2):
            NimiLueJSON = kysyNimi("luettavan JSON")
            Luettu = lueJSON(NimiLueJSON, Luettu)
            print(Luettu)

        elif(Valinta == 3):
            NimiKirjoitaCSV = kysyNimi("kirjoitettavan CSV")
        
        elif(Valinta == 4):
            NimiKirjoitaJSON = kysyNimi("kirjoitettavan JSON")

        elif(Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta, yritä uudestaan.")


        print()





    # Lopetusrutiini:
    Luettu.clear()
    # Vakiotulosteet:
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# End of File