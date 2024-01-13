## Ohjelman hallintoa: Teemu Hiltunen, 15.10.2022, L06T4
## Ohjelman ideana on tulostaa käyttäjälle valikko ja kysyä analysoitavat tiedostot, 
## analysoida ne ja tulostaa tulokset. 
## 
## 
## Muuttujat:
## valikko()
##  Valinta = Käyttäjän antama valinta kokonaislukuna
##  SyoteValinta = käyttäjän antama valinta merkkinä
#
## kysyTiedosto()
##  Kehote = pääohjelmasta tullut parametri liittyen tiedostonimen kysymiseen
##  AiempiTiedosto = aiemman tiedoston parametri pääohjelmasta
##  TiedostoNimi = käyttäjän antama uusi tiedosto
#
## pieninArvo()
##  AnalysoitavaTiedosto = pääohjelmasta tullut parametri käyttäjän pyytämästä tiedostonimestä
##  AlaArvo = pääohjelmasta saatu parametri
##  TiedostoPieni = luettava tiedosto
##  Rivi = tiedoston luettava rivi
##  RiviArvo = tiedoston rivin arvo kokonaislukuna
#
## suurinArvo()
##  AnalyysiTiedosto = pääohjelmasta tullut parametri käyttjän pyytämästä tiedostonimestä
##  YlaArvo = pääohjelmasta saatu parametri
##  TiedostoSuuri = luettava tiedosto
##  RiviLuku = tiedostosta luettava rivi
##  RiviLukuArvo = luetun rivin kokonaislukuarvo
#
## kirjoitaTiedosto()
##  TiedostoKirjaus = pääohjelmasta saatu parametri käyttäjän määrittämästä kirjoitettavasta tiedostosta
##  ArvoAla = parametri, luetun tiedoston alin arvo
##  ArvoYla = parametri, luetun tiedoston ylin arvo
##  TiedostoKirjoita = kirjoitettava tiedosto
#
## paaohjelma()
##  Toiminto = käyttäjän valitsema toiminto valikosta
##  LuettavaTiedosto = käyttäjän määrittämä analysoitava tiedosto
##  KirjoitettavaTiedosto = käyttäjän määrittämä kirjoitettava tiedosto
##  AlinArvo = luetun tiedoston alin arvo
##  YlinArvo = luetun tiedoston ylin arvo
## 
## 
## Suoritettava ohjelma alkaa:

# Aliohjelmat:
def valikko():
    Valinta = 0
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta

def kysyTiedosto(Kehote,AiempiTiedosto):
    print(Kehote.format(AiempiTiedosto))
    TiedostoNimi = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    # Mikäli käyttäjä haluaa lukea / kirjoittaa entiseen tiedostoon hän painaa enter jolloin palautetaan takasin saatu parametri
    if(TiedostoNimi == ""):
        return AiempiTiedosto
    else:
        return TiedostoNimi

def pieninArvo(AnalysoitavaTiedosto, AlaArvo):
    TiedostoPieni = open(AnalysoitavaTiedosto,'r',encoding="utf-8")
    while(True):
        Rivi = TiedostoPieni.readline()
        if(len(Rivi) == 0):
            break
        # Poistetaan rivinvaihtomerkki rivin lopusta ja muunnetaan kokonaisluvuksi.
        RiviArvo = int(Rivi[:-1:])
        # Kirjoitetaan ensimmäinen tiedoston arvo pienimmäksi vertailukohdaksi.
        if(AlaArvo == None):
            AlaArvo = RiviArvo
        elif(AlaArvo > RiviArvo):
            AlaArvo = RiviArvo
        
    TiedostoPieni.close()
    return AlaArvo
    

def suurinArvo(AnalyysiTiedosto, YlaArvo):
    TiedostoSuuri = open(AnalyysiTiedosto,'r',encoding="utf-8")
    while(True):
        RiviLuku = TiedostoSuuri.readline()
        if(len(RiviLuku) == 0):
            break
        # Poistetaan rivinvaihtomerkki rivin lopusta ja muunnetaan kokonaisluvuksi.
        RiviLukuArvo = int(RiviLuku[:-1:])
        if(YlaArvo < RiviLukuArvo):
            YlaArvo = RiviLukuArvo
        if(len(RiviLuku) == 0):
            break

    TiedostoSuuri.close()
    return YlaArvo

def kirjoitaTiedosto(TiedostoKirjaus, ArvoAla, ArvoYla):
    TiedostoKirjoita = open(TiedostoKirjaus,'w',encoding="utf-8")
    TiedostoKirjoita.write("Analyysin tulokset ovat seuraavat:\n")
    TiedostoKirjoita.write("Datan pienin arvo on " + str(ArvoAla) + '.\n')
    TiedostoKirjoita.write("Datan suurin arvo on " + str(ArvoYla) + '.\n')
    TiedostoKirjoita.close()
    return None
    

# Pääohjelma:
def paaohjelma():
    # Alustus:
    Toiminto = 0
    LuettavaTiedosto = ""
    KirjoitettavaTiedosto = ""
    AlinArvo = None
    YlinArvo = 0


    # Alkutulostus:
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    

    while(True):
        # Valikon tulostus:
        Toiminto = valikko()
 
        if(Toiminto == 1):
            print("Anna tiedostonimet")
            LuettavaTiedosto = kysyTiedosto("Luettavan tiedoston nimi on '{}'.", LuettavaTiedosto)
            KirjoitettavaTiedosto = kysyTiedosto("Kirjoitettavan tiedoston nimi on '{}'.", KirjoitettavaTiedosto)
            
        elif(Toiminto == 2):
            print("Suoritetaan analyysi")
            AlinArvo = pieninArvo(LuettavaTiedosto, AlinArvo)
            YlinArvo = suurinArvo(LuettavaTiedosto, YlinArvo)

        elif(Toiminto == 3):
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoitaTiedosto(KirjoitettavaTiedosto, AlinArvo, YlinArvo)

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