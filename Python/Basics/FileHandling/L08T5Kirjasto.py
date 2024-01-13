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

# Kiintoarvot:
EROTIN = ';'

# Luokat:
class TUOTETIEDOT():
    TuoteTunniste = None
    TuoteLkm = None
    KplHinta = None


# Aliohjelmat:
def kysyTiedosto(Kehote,Tiedosto):
    print(Kehote.format(Tiedosto))
    SyoteTiedosto = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    
    if(SyoteTiedosto == ""):
        SyoteTiedosto = Tiedosto
    return SyoteTiedosto


def lueTiedosto(LukuTiedosto):
    # Alustus:
    LuettuLista = []
    # Tiedoston avaus:
    TiedostoLue = open(LukuTiedosto,'r',encoding="utf-8")

    while(True):
        Rivi = TiedostoLue.readline()
        # Luetaan rivejä kunnes ne loppuvat:
        if(len(Rivi) == 0):
            break
        # Leikataan rivinvaihto pois:
        Rivi = Rivi[:-1:]
        # Olio:
        TuoteTiedot = TUOTETIEDOT()
        # Erotetaan luettavan rivin tiedot ja määritellään olion jäsenmuuttujiin:
        Sarake = Rivi.split(EROTIN)
        TuoteTiedot.TuoteTunniste = Sarake[0]
        TuoteTiedot.TuoteLkm = Sarake[1]
        TuoteTiedot.KplHinta = Sarake[2]
        # Oliolista:
        LuettuLista.append(TuoteTiedot)

    TiedostoLue.close()
    

    return LuettuLista



def analysoi(AnalysoitavaLista,AnalysoituLista):
    # Alustus:
    AnalysoituLista = []
    TuoteArvo = 0.0
    VarastoArvo = 0.0

    for alkio in range(0,len(AnalysoitavaLista)):
        # Lasketaan varastoarvoa jokaisen tuotteen kohdalla:
        TuoteArvo = float(AnalysoitavaLista[alkio].KplHinta) * float(AnalysoitavaLista[alkio].TuoteLkm)
        # Lisätään tuotteen arvo listaan ja summataan VarastoArvo tähän asti:
        AnalysoituLista.append(TuoteArvo)
        VarastoArvo = VarastoArvo + TuoteArvo

    # Pyöristetään ja formatoidaan:
    VarastoArvo = "{0:.2f}".format(VarastoArvo)
    # Tulostetaan varaston arvo:
    print("Tiedot analysoitu, varaston arvo on {} EUR.".format(VarastoArvo))
    return AnalysoituLista


def kirjoitaTiedosto(KirjaaTiedosto, TietoLista):
    TiedostoKirjattava = open(KirjaaTiedosto,'w',encoding="utf-8")
    # Kirjataan TietoListan alkiot omille riveilleen tiedostoon kahden desimaalin tarkkuudella:
    for alkio in range(0,len(TietoLista)):
        Pyoristys = "{0:.2f}".format(TietoLista[alkio])
        TiedostoKirjattava.write(Pyoristys + "\n")

    TiedostoKirjattava.close()

    return None

# End of File