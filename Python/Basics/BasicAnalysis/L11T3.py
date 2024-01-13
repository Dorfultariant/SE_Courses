######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 22.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T3.py

# Aliohjelmat:

def tulostaSana(Sana, i, Maara):
    print("Sana on '{}', {}. kerta.".format(Sana, i))
    if(i < Maara):
        return tulostaSana(Sana, (i + 1), Maara)        # Kutsutaan aliohjelmaa mikäli lopetusehto ei täyty
    else:
        return None                                     # Kun lopetusehto täyttyy voidaan rekursio lopettaa ja palauttaa None


# Pääohjelma:
def paaohjelma():
    Sana = input("Anna tulostettava sana: ")
    Syote = input("Anna tulostuskertojen määrä: ")
    Maara = int(Syote)
    
    # Lähetetään parametreina toistettava sana, 1 (ensimmäisen kerran sanotaan), toistomäärä:
    tulostaSana(Sana, 1, Maara)

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()


# End of File