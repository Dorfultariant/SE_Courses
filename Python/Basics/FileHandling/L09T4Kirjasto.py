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
import sys


# Luokat:
class TULOS:
    PieninArvo = None
    SuurinArvo = None
    SummaArvo = 0
    Keskiarvo = 0


# Aliohjelmat:
def kysyNimi(Nimi, Kehote):
    print(Kehote.format(Nimi))
    Syote = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if(Syote == ""):
        Syote = Nimi
    return Syote


def lueTiedosto(Nimi):
    Lista=[]
    try:
        Tiedosto = open(Nimi,'r',encoding="utf-8")
        while(True):
            Rivi = Tiedosto.readline()
            if(len(Rivi) == 0):
                break
            Rivi = Rivi[:-1:]
            Rivi = float(Rivi)
            Lista.append(Rivi)

        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)
    print("Tiedosto '{}' luettu.".format(Nimi))
    return Lista


def analysoi(AnalysoitavaLista, Olio):
    # Määritellään pienin ja suurin arvo alussa:
    if(Olio.PieninArvo == None):
        Olio.PieninArvo = AnalysoitavaLista[0]
        
    if(Olio.SuurinArvo == None):
        Olio.SuurinArvo = AnalysoitavaLista[0]

    for alkio in range(0,len(AnalysoitavaLista)):
        if(Olio.PieninArvo > AnalysoitavaLista[alkio]):
            Olio.PieninArvo = AnalysoitavaLista[alkio]

        if(Olio.SuurinArvo < AnalysoitavaLista[alkio]):
            Olio.SuurinArvo = AnalysoitavaLista[alkio]

        # Summaus:
        Olio.SummaArvo = Olio.SummaArvo + AnalysoitavaLista[alkio]

    # Keskiarvo:
    Olio.Keskiarvo = Olio.SummaArvo / len(AnalysoitavaLista)

    print("Analyysi suoritettu.")
    AnalysoitavaLista.clear()
    return Olio


def kirjoitaTiedosto(Nimi, Olio):
    try:
        Tiedosto = open(Nimi,'w',encoding="utf-8")
        
        # Datan formatointi:
        Olio.PieninArvo = "{0:.0f}".format(Olio.PieninArvo)
        Olio.SuurinArvo = "{0:.0f}".format(Olio.SuurinArvo)
        Olio.SummaArvo = "{0:.0f}".format(Olio.SummaArvo)
        Olio.Keskiarvo = round(Olio.Keskiarvo,0)
        Olio.Keskiarvo = "{0:.1f}".format(Olio.Keskiarvo)
        
        # Otsikko:
        Tiedosto.write("Analyysin tulokset ovat seuraavat:\n")

        # Datan kirjaus:
        Tiedosto.write("Datan pienin arvo on " + Olio.PieninArvo + ".\n")
        Tiedosto.write("Datan suurin arvo on " + Olio.SuurinArvo + ".\n")
        Tiedosto.write("Datan summa on " + Olio.SummaArvo + ".\n")
        Tiedosto.write("Datan keskiarvo on " + Olio.Keskiarvo + ".\n")
        
        # Suljetaan tiedosto:
        Tiedosto.close()

    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)

    print("Tulokset kirjoitettu tiedostoon.")
    return None

# End of File