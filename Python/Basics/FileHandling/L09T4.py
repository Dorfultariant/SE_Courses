######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 8.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T4.py


# Kirjastot:
import L09T4Kirjasto


# Valikko aliohjelma:
def valikko():
    Toiminto = 0
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Toiminto = int(SyoteValinta)
    return Toiminto


# Pääohjelma:
def paaohjelma():
    # Alustus:
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""
    LuettuTiedosto = []

    # Olion luonti:
    Tulos = L09T4Kirjasto.TULOS()

    # Alkutulostus:
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    
    while(True):
        # Valikon tulostus:
        Toiminto = valikko()

        if(Toiminto == 1):
            LuettavaTiedosto = L09T4Kirjasto.kysyNimi(LuettavaTiedosto, "Luettavan tiedoston nimi on '{}'.")
            LuettuTiedosto = L09T4Kirjasto.lueTiedosto(LuettavaTiedosto)
            
        elif(Toiminto == 2):
            if(len(LuettuTiedosto) == 0):
                print("Ei analysoitavia tietoja, ei analysoitu.")
            else:
                Tulos = L09T4Kirjasto.analysoi(LuettuTiedosto, Tulos)
                


        elif(Toiminto == 3):
            if(Tulos.PieninArvo == None or Tulos.SuurinArvo == None):
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
            else:
                KirjoitettavaTiedosto = L09T4Kirjasto.kysyNimi(KirjoitettavaTiedosto, "Kirjoitettavan tiedoston nimi on '{}'.".format(KirjoitettavaTiedosto))
                L09T4Kirjasto.kirjoitaTiedosto(KirjoitettavaTiedosto, Tulos)
                

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