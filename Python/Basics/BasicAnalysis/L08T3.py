######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
# Päivämäärä: 01.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T3.py

import datetime


# Aliohjelmat:
def valikko():
    Valinta = 0
    print("Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit")
    print("2) Laske ikä päivinä")
    print("3) Tulosta viikonpäivät")
    print("4) Tulosta kuukaudet")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta


def aika():
    Pvm = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    Paivamaara = datetime.datetime.strptime(Pvm, "%d.%m.%Y %H:%M")
    print("Annoit vuoden {}".format(Paivamaara.year))
    print("Annoit kuukauden {}".format(Paivamaara.month))
    print("Annoit päivän {}".format(Paivamaara.day))
    print("Annoit tunnin {}".format(Paivamaara.hour))
    print("Annoit minuutin {}".format(Paivamaara.minute))
    return None


def kulunutAika():
    VertailuPvm = datetime.datetime(2000, 1, 1)
    SyntymaPvm = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ")
    VuosijuhlaPaivamaara = datetime.datetime.strptime(SyntymaPvm, "%d.%m.%Y")
    PaivaEro = VertailuPvm - VuosijuhlaPaivamaara
    print("1.1.2000 henkilö oli {} päivää vanha.".format(PaivaEro.days))
    return None


def viikonPaivat():
    Paiva = datetime.datetime(2022, 10, 31)
    for alkio in range(0,7):
        print(Paiva.strftime("%A"))
        Paiva = Paiva + datetime.timedelta(days=+1)
    return None


def kuukaudet():
    Kuukausi = datetime.datetime(2022, 1, 1)
    for alkio in range(0,12):
        print(Kuukausi.strftime("%b"))
        Kuukausi = Kuukausi + datetime.timedelta(days=+31)
    return None


# Pääohjelma:
def paaohjelma():
    # Alustus:
    Toiminto = 0
 
    # Alkutulostus:
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")

    while(True):

        # Valikon tulostus:
        Toiminto = valikko()

        if(Toiminto == 1):
            aika()
            
        elif(Toiminto == 2):
            kulunutAika()

        elif(Toiminto == 3):
            viikonPaivat()

        elif(Toiminto == 4):
            kuukaudet()

        elif(Toiminto == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()


    # Lopputulostus:
    print()
    print("Kiitos ohjelman käytöstä.")
    return None


# Päätaso
paaohjelma()


# End of File