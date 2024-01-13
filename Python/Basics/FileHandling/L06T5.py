## Ohjelman hallintoa: Teemu Hiltunen, 16.10.2022, L06T5
## Ohjelman ideana on lukea käyttäjän valitsemaa tiedostoa ja kirjata toiseen tiedostoon
## analysoitua tietoa.
## 
## Aliohjelman muuttujat:
## TiedostoonTallennus = pääohjelmasta saatu parametri käyttäjän kohdetiedostolle.
## PaivaMaara = parametrina saatu päivämäärä
## Kulutus = parametrina saatu kWh lukema (merkkijonona)
## Tiedosto = itse kohdetiedosto
## 
## Pääohjelman muuttujat:
## KulutusVRK = tänne lasketaan vrk aikana tullut kWh lukema, lähetetään kirjoitettavaksi aliohjelmaan.
## Pv = päivämäärän päivän osuus, edellisen pvm säilytys
## Kk = päivämäärän kuukauden osuus, edellisen pvm säilytys
## Vvvv = päivämäärän vuoden osuus, edellisen pvm säilytys
## Otsikkorivi = Boolean, käytetään ohittamaan otsikkorivi analysoinnissa. (Oletetaan, että ensimmäinen rivi on otsikkorivi, vaarallinen oletus tiedän.)
## LuettavaTiedosto = käyttäjän antama lähdetiedosto nimi
## KirjoitettavaTiedosto = käyttäjän antama kohdetiedosto nimi
## KirjausTiedosto = itse kohdetiedosto
## LukuTiedosto = itse lähdetiedosto
## LuettuRivi = lähdetiedostosta luettu rivi
## Pvm = aliohjelmaan lähetettävä parametri joka muodostuu Pv, Kk, Vvvv ("01.01.2000")
## Paiva = päivämäärän päivän osuus, nykyisen pvm säilytys
## Kuukausi = päivämäärän kuukauden osuus, nykyisen pvm säilytys
## Vuosi = päivämäärän vuoden osuus, nykyisen pvm säilytys
## YoKulutus = luetun rivin kWh merkkijono, yö
## PaivaKulutus = luetun rivin kWh merkkijono, päivä
## YoKWh = float yön kWh arvo
## PaivaKWh = float päivän kWh arvo
## 
## 
## 
## 
## Suoritettava ohjelma alkaa:


# Aliohjelmat:
def tallennaTiedostoon(TiedostoonTallennus, PaivaMaara, Kulutus):
    Tiedosto = open(TiedostoonTallennus,'a',encoding="utf-8")
    # Formatoidaan tiedot annetun ohjeen mukaisesti pvm osio: 10 merkkiä, kWh osio: 5 merkkiä. 
    Tiedosto.write('{:>10}'.format(PaivaMaara) + ':' + '{:>5}'.format(Kulutus) + "\n")
    Tiedosto.close()

    return None

# Pääohjelma:
def paaohjelma():
    # Alustus:
    KulutusVRK = 0.0
    Pv = None
    Kk = None
    Vvvv = None
    Otsikkorivi = True

    # Kysytään käyttäjältä lähdetiedosto ja kohdetiedosto.
    LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    KirjoitettavaTiedosto = input("Anna tallennettavan tiedoston nimi: ")

    # Kirjoitettavan tiedoston alustus ja otsikointi:
    KirjausTiedosto = open(KirjoitettavaTiedosto,'w',encoding="utf-8")
    KirjausTiedosto.write('{:>10}'.format("Pvm") + ':' + '{:>5}'.format("kWh") + "\n") # Otsikko pvm levelys = 10 merkkiä, kulutus leveys = 5, tasattu oikealle molemmat
    KirjausTiedosto.close()

    # Avataan luettava tiedosto:
    LukuTiedosto = open(LuettavaTiedosto,'r',encoding="utf-8")

    while(True):
        
        LuettuRivi = LukuTiedosto.readline()
        # Otsikkoriviä ei haluta tarkastella tämän kummemmin joten hypätään sen yli silmukassa.
        if(Otsikkorivi == True):
            Otsikkorivi = False
            continue
        # Kun viimeinen rivi saavutetaan, kirjataan sen rivin tiedot ylös kohdetiedostoon ja lopetetaan silmukka.
        elif(len(LuettuRivi) == 0):
            Pvm = Pv + '.' + Kk + '.' + Vvvv
            tallennaTiedostoon(KirjoitettavaTiedosto, Pvm, '{0:.0f}'.format(KulutusVRK))
            break

        # Leikellään lähdetiedostossa oleva tieto tarkasteltaviin palasiin:
        Paiva = LuettuRivi[:2:]
        Kuukausi = LuettuRivi[3:5:]
        Vuosi = LuettuRivi[6:10:]
        YoKulutus = LuettuRivi[14:18:]
        PaivaKulutus = LuettuRivi[19:23:]

        # Muunnetaan kWh lukemat liukuluvuiksi:
        YoKWh = float(YoKulutus)
        PaivaKWh = float(PaivaKulutus)
        # Kirjataan ensimmäinen luettu kulutusrivi ylös:
        if((Pv == None) and (Kk == None) and (Vvvv == None)):
            Pv = Paiva
            Kk = Kuukausi
            Vvvv = Vuosi

        # Tarkastellaan mikäli sama pvm on nyt luetussa rivissä ja edellisessä luetussa rivissä:
        if((Paiva == Pv) and (Kuukausi == Kk) and (Vuosi == Vvvv)):
            KulutusVRK = KulutusVRK + YoKWh + PaivaKWh
        # Kun pvm vaihtuu, kirjataan edellisen pvm:n tiedot ylös ja siirrytään uuteen päivään:
        elif((Paiva != Pv) or (Kuukausi != Kk) or (Vuosi != Vvvv)):
            Pvm = Pv + '.' + Kk + '.' + Vvvv
            tallennaTiedostoon(KirjoitettavaTiedosto, Pvm, '{0:.0f}'.format(KulutusVRK))
            # Päivämäärän vaihtuessa nollataan kertynyt kulutus ja kirjataan uuden päivän kulutus:
            KulutusVRK = 0
            KulutusVRK = YoKWh + PaivaKWh
        
        # Tallennetaan nykyinen pvm seuraavan rivin tarkastelua varten.
        Pv = Paiva
        Kk = Kuukausi
        Vvvv = Vuosi

    # Suljetaan tiedosto:
    LukuTiedosto.close()
    # Vakiotulostus ja lopetus:
    print("Kiitos ohjelman käytöstä.")
    return None

# Päätaso:
paaohjelma()


# End of File