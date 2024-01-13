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
# Tehtävä L09T3.py

# Kirjastot:
import sys


# Aliohjelmat:
def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi,'r',encoding="utf-8")
        Rivi = Tiedosto.readline()
        # Jos tiedosto on tyhjä, palautetaan tyhjä lista:
        if(Rivi == ""):
            return Lista
        
        while(len(Rivi) > 0):
            Rivi = Rivi[:-1:]
            Lista.append(Rivi)
            Rivi = Tiedosto.readline()
            
        Tiedosto.close()
    
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Nimi))
        sys.exit(0)

    return Lista



def analysoiLista(LuettuLista, AutoLista):
    AiempiMerkki = LuettuLista[0]
    
    for Alkio in range(len(LuettuLista)):
        if(AiempiMerkki == LuettuLista[Alkio]):
            continue
        else:
            AutoLista.append(AiempiMerkki)
            AiempiMerkki = LuettuLista[Alkio]

    AutoLista.append(LuettuLista[Alkio])
    return AutoLista


def kirjoitaTiedosto(Nimi, AutoLista):
    try:
        Tiedosto = open(Nimi,'w',encoding="utf-8")
        for Auto in AutoLista:
            Tiedosto.write(Auto + '\n')

        Tiedosto.close()

    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    print("Tiedostossa oli {} eri automerkkiä.".format(len(AutoLista)))
    for Auto in AutoLista:
        print(Auto)
    
    return None

# Pääohjelma:
def paaohjelma():
    # Alustus:
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""
    LueLista = []
    AutoLista = []

    LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    KirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")

    LueLista = lueTiedosto(LuettavaTiedosto, LueLista)
    if(len(LueLista) == 0):
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        AutoLista = analysoiLista(LueLista, AutoLista)
        kirjoitaTiedosto(KirjoitettavaTiedosto, AutoLista)

    # Lopetusrutiini:
    LueLista.clear()
    AutoLista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()


# End of File