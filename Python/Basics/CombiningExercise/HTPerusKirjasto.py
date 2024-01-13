######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Hiltunen
# Opiskelijanumero: 000393597
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
import datetime
import sys

# Kiintoarvot:
LUKUEROTIN = ';' # Luettavan tiedoston erotinmerkki.  Vakio on ';'
KIRJOEROTIN = ';' # Kirjoituskohtien erotinmerkki.  Vakio on ';'
VIIKONPAIVAT = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"] # Käytetään analysoiViikonpaivaHinta -aliohjelmassa viikonpäivien tallennuksessa.

# Luokat:
class TIEDOT:
    Pvm = None
    Hinta = None

class TILASTO:
    HalvinHinta = None
    HalvinAikaLeima = None

    KalleinHinta = None
    KalleinAikaLeima = None

    HintaTietoLkm = 0
    KaikkiHintaKA = 0



# Aliohjelmat:
def kysyTiedosto(Tiedostonimi, Kehote):
    SyoteNimi = input(Kehote)
    if(SyoteNimi == ""):
        Tiedostonimi = Tiedostonimi
    else:
        Tiedostonimi = SyoteNimi
    return Tiedostonimi


def lueTiedosto(Tiedostonimi):
    LuettuLista = []
    try:
        Tiedosto = open(Tiedostonimi,'r',encoding="utf-8")

        Rivi = Tiedosto.readline() # Hypätään otsikkorivi yli.
        Rivi = Tiedosto.readline() # Dataa.

        while(len(Rivi) > 0):
            # Leikataan rivinvaihtomerkki pois:
            Rivi = Rivi[:-1:]
            # Jaotellaan rivi alkioihin erottimen mukaan:
            Sarake = Rivi.split(LUKUEROTIN)

            # Muunnetaan toinen sarake desimaaliluvuksi:
            Sarake[1] = float(Sarake[1])
            # Leikataan päivämäärästä " -merkit pois alusta ja lopusta:
            Sarake[0] = Sarake[0][1:-1:]
        
            # Kirjataan tiedot ylös olioon:
            Tiedot = TIEDOT()
            Tiedot.Pvm = datetime.datetime.strptime(Sarake[0],"%Y-%m-%d %H:%M:%S")
            Tiedot.Hinta = Sarake[1]
            # Lisätään olio listaan:
            LuettuLista.append(Tiedot)
            # Luetaan seuraavan kierroksen rivi.
            Rivi = Tiedosto.readline()
        Tiedosto.close()

    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Tiedostonimi))
        sys.exit(0)

    print("Tiedosto '{}' luettu.".format(Tiedostonimi))
    return LuettuLista


def analysoiVrkTuntiHinta(LuettuLista, AnLista):
    AnLista = []
    Paivamaara = None
    Summa = 0.0
    HintaMaara = 0
    VrkKeskiArvoHinta = 0.0

    for Tieto in LuettuLista:
        # Jos luetaan ensimmäistä oliota LuettuLista oliolistassa, määritellään muuttuja Paivamaara ensimmäisen olion päivämäärällä:
        if(Paivamaara == None):
            Paivamaara = Tieto.Pvm.date()
        # Suoritetaan pvm tarkastelu:
        if(Paivamaara == Tieto.Pvm.date()):
            Summa += Tieto.Hinta                        # Lisätään vuorokauden hinnat yhteen kokoojaan.
            HintaMaara += 1                             # Lisätään yksi kokoojamuuttujaan keskiarvon laskua varten.

        if(Paivamaara != Tieto.Pvm.date() or Tieto == LuettuLista[len(LuettuLista)-1]):     # Tarkastetaan vaihtuuko päivä tai ollaanko Luetun listan lopussa..
            VrkKeskiArvoHinta = Summa / HintaMaara      # Lasketaan keskiarvo.
            Tiedot = TIEDOT()                           # Hyödynnetään olemassa olevaa luokkaa tallentamaan analysoidut tiedot.
            Tiedot.Pvm = Paivamaara                     # Lisätään olioon aikaleima.
            Tiedot.Hinta = VrkKeskiArvoHinta            # Lisätään olioon vuorokauden hinnan keskiarvo.
            AnLista.append(Tiedot)                      # Lisätään olio analysoituun listaan.
            Summa = Tieto.Hinta                         # Alustetaan Summa -muuttuja uuden päivän ensimmäisellä hinta -arvolla.
            HintaMaara = 1                              # Alustetaan HintaMaara -kokooja 1:llä, koska yksi hinta on lisätty Summa -muuttujaan.

        Paivamaara = Tieto.Pvm.date()
    

    return AnLista


def analysoiTilasto(LuettuLista, Olio):
    # Alustus:
    Summa = 0.0

    for Data in LuettuLista:
        # Ensimmäisellä kierroksella alustetaan tilasto-olion Halvin ja Kallein -hinnat ensimmäisen LuettuLista -olion Hinta-arvoilla:
        if(Olio.HalvinHinta == None):
            Olio.HalvinHinta = Data.Hinta
            Olio.HalvinAikaLeima = Data.Pvm
        if(Olio.KalleinHinta == None):
            Olio.KalleinHinta = Data.Hinta
            Olio.KalleinAikaLeima = Data.Pvm

        # Tarkastellaan onko luettu arvo pienempi:
        if(Olio.HalvinHinta > Data.Hinta):
            Olio.HalvinHinta = Data.Hinta
            Olio.HalvinAikaLeima = Data.Pvm
        # tai suurempi kuin edellinen:
        if(Olio.KalleinHinta < Data.Hinta):
            Olio.KalleinHinta = Data.Hinta
            Olio.KalleinAikaLeima = Data.Pvm
        # Summataan hinnat yhteen ja lisätään kerääjä jäsenmuuttujaan 1.
        Summa += Data.Hinta
        Olio.HintaTietoLkm += 1
    
    # Lasketaan kaikkien hintojen keskiarvo:
    Olio.KaikkiHintaKA = Summa / Olio.HintaTietoLkm
    return Olio

def tallenneMuotoilu(Muotoilu, AnLista, Olio, KeskiArvo):
    Muotoilu = []
    # Muotoillaan VrkHinta tietoa
    if(KeskiArvo == None):
        # Tiedon formatointi:
        Otsikko01 = "Analyysin tulokset {} tunnilta ovat seuraavat:\n".format(Olio.HintaTietoLkm)
        Otsikko02 = "Päivittäiset keskiarvot (Pvm{}snt/kWh):\n".format(KIRJOEROTIN)
        KeskiHinta = "Sähkön keskihinta oli {0:.1f} snt/kWh.\n".format(Olio.KaikkiHintaKA)
        # Muunnetaan pvm esitystyyliä:
        HalvinAikaLeima = datetime.datetime.strftime(Olio.HalvinAikaLeima, "%d.%m.%Y %H:%M")                # Käytetään apumuuttujaa 'HalvinAikaLeima' formatoinnissa.
        MinHinta = "Halvimmillaan sähkö oli {} snt/kWh, {}.\n".format(Olio.HalvinHinta, HalvinAikaLeima)        
        KalleinAikaLeima = datetime.datetime.strftime(Olio.KalleinAikaLeima, "%d.%m.%Y %H:%M")              # Käytetään apumuuttujaa 'KalleinAikaLeima' formatoinnissa
        MaxHinta = "Kalleimmillaan sähkö oli {} snt/kWh, {}.\n\n".format(Olio.KalleinHinta, KalleinAikaLeima)
        Muotoilu = [Otsikko01, KeskiHinta, MinHinta, MaxHinta, Otsikko02]
        for Alkio in AnLista:
            # Pyöristetään 1 desimaalin tarkkuuteen apumuuttujaa hyödyntäen:
            Hinta = "{0:.1f}".format(Alkio.Hinta)
            # Muunnetaan pvm esitysmuotoa apumuuttujaa hyödyntäen:
            Pvm = datetime.datetime.strftime(Alkio.Pvm, "%d.%m.%Y")
            # Formatoidaan rivin tyyli:
            Rivi = "{}{}{}\n".format(Pvm, KIRJOEROTIN, Hinta)
            Muotoilu.append(Rivi)
    # Muotoillaan ViikonpaivaHinta tietoa
    else:
        Otsikko11 = "Viikonpäivä{}Keskimääräinen hinta snt/kWh\n".format(KIRJOEROTIN)
        Muotoilu.append(Otsikko11)
        # Käydään KeskiArvo -lista läpi ja kirjoitetaan viikonpäivien keskiarvot tiedostoon:
        for i in range(len(KeskiArvo)):
            PyoristysKA = "{0:.1f}".format(KeskiArvo[i])                             # Pyöristetään 1 desimaalin tarkkuuteen.
            FormRivi = "{}{}{}\n".format(VIIKONPAIVAT[i], KIRJOEROTIN, PyoristysKA)  # Formatoidaan kirjoitettava rivi
            Muotoilu.append(FormRivi) # Lisätään muotoillut rivit järjestyksessä listaan.
    
    return Muotoilu


def kirjoitaTiedosto(Tiedostonimi, Muotoilu):
    try:
        Tiedosto = open(Tiedostonimi,'w',encoding="utf-8")
        # Tiedotoston kirjoitus:
        for Alkio in Muotoilu:
            # Kirjoitetaan Rivi:
            Tiedosto.write(Alkio)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(Tiedostonimi))
        sys.exit(0)

    print("Tiedosto '{}' kirjoitettu.".format(Tiedostonimi))
    return None



def analysoiViikonpaivaHinta(Tiedostonimi, LuettuLista, KeskiArvo):
    # Alustus:
    # Jos joskus muutetaan viikonpäivien lukumäärää, niin mm. näitä listoja pitää muokata
    Sum = [0,0,0,0,0,0,0]           # -||-
    Maara = [0,0,0,0,0,0,0]         # -||-
    KeskiArvo = [0,0,0,0,0,0,0]     # -||-
    Paiva = None
    # Päivittäisten hintojen tarkastelua:
    for Olio in LuettuLista:            # Käydään oliot läpi LuettuLista:ssa
        Paiva = Olio.Pvm.weekday()      # Otetaan olion Pvm:n viikonpäivän indeksi talteen.
        Sum[Paiva] += Olio.Hinta        # Lisätään Summa -listaan viikonpäivän indeksiä vastaava olion Hinta
        Maara[Paiva] += 1               # Lisätään Maara -listaan viikonpäivän indeksiä vastaava viikonpäivien lukumäärä
    # Keskiarvon laskenta ja lisäys listaan:
    for i in range(7):                              
        if(Maara[i] != 0):                          # Tarkastellaan Maara -listan indeksin arvoa.
            KeskiArvo[i] = Sum[i] / Maara[i]        # Lasketaan keskiarvo ja lisätään se KeskiArvo -listaan.
    
    # Tyhjennetään listat:
    Sum.clear()
    Maara.clear()

    return KeskiArvo

# End of File