######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Päivämäärä: 17.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

# Kirjastot:
import HTPerusKirjasto


# Valikko-aliohjelma:
def valikko():
    Valinta = 0
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta


# Pääohjelma:
def paaohjelma():
    # Alustus:
    Valinta = 1
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""
    AnalyysiTiedostonimi = ""

    LuettuLista = []
    AnalysoituLista = []
    Muotoilu = []
    KeskiArvoLista = []
    

    while(Valinta != 0):
        
        # Valikon tulostus:
        Valinta = valikko()

        if(Valinta == 1):
            LuettavaTiedosto = HTPerusKirjasto.kysyTiedosto(LuettavaTiedosto, "Anna luettavan tiedoston nimi: ")
            LuettuLista = HTPerusKirjasto.lueTiedosto(LuettavaTiedosto)
            
        elif(Valinta == 2):
            # Tarkastetaan onko mitään analysoitavaa:
            if(len(LuettuLista) > 0):
                Tilasto = HTPerusKirjasto.TILASTO()     # Luodaan Tilasto -olio
                # Analysoidaan LuettuLista kahdella erillisellä aliohjelmalla:
                AnalysoituLista = HTPerusKirjasto.analysoiVrkTuntiHinta(LuettuLista, AnalysoituLista)
                Tilasto = HTPerusKirjasto.analysoiTilasto(LuettuLista, Tilasto)

                print("Tilastotietojen analyysi suoritettu {} alkiolle.".format(Tilasto.HintaTietoLkm))
                print("Päivittäiset keskiarvot laskettu {} päivälle.".format(len(AnalysoituLista)))
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif(Valinta == 3):
            # Tarkastetaan onko mitään kirjoitettavaa:
            if(len(AnalysoituLista) > 0):    
                KirjoitettavaTiedosto = HTPerusKirjasto.kysyTiedosto(KirjoitettavaTiedosto, "Anna kirjoitettavan tiedoston nimi: ")
                # Lähetetään tiedot muotoiltavaksi:
                Muotoilu = HTPerusKirjasto.tallenneMuotoilu(Muotoilu, AnalysoituLista, Tilasto, None)
                # Kirjoitetaan muotoillut tiedot
                HTPerusKirjasto.kirjoitaTiedosto(KirjoitettavaTiedosto, Muotoilu)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")

        elif(Valinta == 4):
            # Tarkistetaan onko mitää analysoitavaa:
            if(len(LuettuLista) > 0):
                AnalyysiTiedostonimi = HTPerusKirjasto.kysyTiedosto(AnalyysiTiedostonimi, "Anna kirjoitettavan tiedoston nimi: ")
                # Analysoidaan tiedot:
                KeskiArvoLista = HTPerusKirjasto.analysoiViikonpaivaHinta(AnalyysiTiedostonimi, LuettuLista, KeskiArvoLista)
                # Lähetetään tiedot muotoiltavaksi:
                Muotoilu = HTPerusKirjasto.tallenneMuotoilu(Muotoilu, None, None, KeskiArvoLista)
                # Kirjoitetaan muotoillut tiedot:
                HTPerusKirjasto.kirjoitaTiedosto(AnalyysiTiedostonimi, Muotoilu)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif(Valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()

    # Lopetusrutiinit:
    LuettuLista.clear()
    AnalysoituLista.clear()
    Muotoilu.clear()
    KeskiArvoLista.clear()
    HTPerusKirjasto.VIIKONPAIVAT.clear()
    
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

# Päätaso:
paaohjelma()


# End of File
