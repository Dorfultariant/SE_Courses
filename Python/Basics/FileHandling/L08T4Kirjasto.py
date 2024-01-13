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

# Luokat:
class TULOS:
    PieninArvo = None
    SuurinArvo = None
    SummaArvo = 0
    Keskiarvo = 0

# Aliohjelmat:
def lueTiedosto(TiedostoLuku):
    Tiedosto = open(TiedostoLuku,'r',encoding="utf-8")
    Lista=[]
    while(True):
        Rivi = Tiedosto.readline()
        if(len(Rivi) == 0):
            break
        Rivi = Rivi[:-1:]
        Rivi = float(Rivi)
        Lista.append(Rivi)
        
    Tiedosto.close()
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
    Olio.Keskiarvo = Olio.SummaArvo / (alkio + 1) # Lisätään alkioon viimeinen iteraatio.

    # Formatointi:
    Olio.PieninArvo = "{0:.0f}".format(Olio.PieninArvo)
    Olio.SuurinArvo = "{0:.0f}".format(Olio.SuurinArvo)
    Olio.SummaArvo = "{0:.0f}".format(Olio.SummaArvo)
    Olio.Keskiarvo = round(Olio.Keskiarvo,0)
    Olio.Keskiarvo = "{0:.1f}".format(Olio.Keskiarvo)
    
    return Olio

def kirjoitaTiedosto(TiedostoKirjaa, Elio):
    KirjaaTiedosto = open(TiedostoKirjaa,'w',encoding="utf-8")
    # Otsikko:
    KirjaaTiedosto.write("Analyysin tulokset ovat seuraavat:\n")
    # Data:
    KirjaaTiedosto.write("Datan pienin arvo on " + Elio.PieninArvo + ".\n")
    KirjaaTiedosto.write("Datan suurin arvo on " + Elio.SuurinArvo + ".\n")
    KirjaaTiedosto.write("Datan summa on " + Elio.SummaArvo + ".\n")
    KirjaaTiedosto.write("Datan keskiarvo on " + Elio.Keskiarvo + ".\n")
    # Suljetaan tiedosto:
    KirjaaTiedosto.close()
    return None



# End of File