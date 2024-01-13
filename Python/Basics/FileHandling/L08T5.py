######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 2.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py

# Kirjastot:
import L08T5Kirjasto

# Valikko-aliohjelma:
def valikko():
    Valinta = 0
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    SyoteValinta = input("Valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta


# Pääohjelma:
def paaohjelma():
    # Alustus:
    Toiminto = 1
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""

    LuettuTiedosto = []
    AnalysoituTieto = []


    while(Toiminto != 0):
        
        # Tulostetaan valikko:
        Toiminto = valikko()

        if(Toiminto == 1):
            LuettavaTiedosto = L08T5Kirjasto.kysyTiedosto("Anna luettavan tiedoston nimi, nykyinen on '{}'.", LuettavaTiedosto)
            LuettuTiedosto = L08T5Kirjasto.lueTiedosto(LuettavaTiedosto)
            print("Tiedosto '{}' luettu, {} riviä.".format(LuettavaTiedosto,len(LuettuTiedosto)))

        elif(Toiminto == 2):
            AnalysoituTieto = L08T5Kirjasto.analysoi(LuettuTiedosto, AnalysoituTieto)

        elif(Toiminto == 3):
            KirjoitettavaTiedosto = L08T5Kirjasto.kysyTiedosto("Anna kirjoitettavan tiedoston nimi, nykyinen on '{}'.".format(KirjoitettavaTiedosto), KirjoitettavaTiedosto)
            L08T5Kirjasto.kirjoitaTiedosto(KirjoitettavaTiedosto, AnalysoituTieto)
            print("Tulokset tallennettu tiedostoon '{}'.".format(KirjoitettavaTiedosto))

        elif(Toiminto == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()

    # Listojen poisto:
    LuettuTiedosto.clear()
    AnalysoituTieto.clear()
    # Lopputulostus:
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

# Päätaso:
paaohjelma()


# End of File