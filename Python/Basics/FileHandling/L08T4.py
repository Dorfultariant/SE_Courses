######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T4.py

# Kirjastot:
import L08T4Kirjasto


# Pääohjelma:
def paaohjelma():
    # Alustus:
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""
    LukuTiedosto = ""
    KirjaTiedosto = ""
    LuettuTiedosto = []

    # Olion luonti:
    Tulos1 = L08T4Kirjasto.TULOS()

    # Alkutulostus:
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    
    while(True):
        # Valikon tulostus:
        Toiminto = 0
        print("Valitse haluamasi toiminto:")
        print("1) Lue tiedosto")
        print("2) Analysoi")
        print("3) Kirjoita tiedosto")
        print("0) Lopeta")
        SyoteValinta = input("Anna valintasi: ")
        Toiminto = int(SyoteValinta)

        if(Toiminto == 1):
            print("Luettavan tiedoston nimi on '{}'.".format(LuettavaTiedosto))
            LukuTiedosto = input("Anna uusi nimi, enter säilyttää nykyisen: ")
            if(LukuTiedosto == ""):
                LuettuTiedosto = L08T4Kirjasto.lueTiedosto(LuettavaTiedosto)
                print("Tiedosto '{}' luettu.".format(LuettavaTiedosto))
            else:
                LuettuTiedosto = L08T4Kirjasto.lueTiedosto(LukuTiedosto)
                print("Tiedosto '{}' luettu.".format(LukuTiedosto))
            
            
        elif(Toiminto == 2):
            Tulos1 = L08T4Kirjasto.analysoi(LuettuTiedosto, Tulos1)
            print("Analyysi suoritettu.")


        elif(Toiminto == 3):
            print("Kirjoitettavan tiedoston nimi on '{}'.".format(KirjoitettavaTiedosto))
            KirjaTiedosto = input("Anna uusi nimi, enter säilyttää nykyisen: ")
            if(KirjaTiedosto == ""):
                L08T4Kirjasto.kirjoitaTiedosto(KirjoitettavaTiedosto, Tulos1)
            else:
                L08T4Kirjasto.kirjoitaTiedosto(KirjaTiedosto, Tulos1)
            print("Tulokset kirjoitettu tiedostoon.")


        elif(Toiminto == 0):
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()

    # Poistetaan lista:
    LuettuTiedosto.clear()
    
    # Lopputulostus:
    print()
    print("Kiitos ohjelman käytöstä.")
    return None


# Päätaso
paaohjelma()



# End of File 