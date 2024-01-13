## Ohjelman hallintoa: Teemu Hiltunen, 9.10.2022, L05T5
## Ohjelman ideana on kysyä käyttäjältä merkkijonoja tietyin ehdoin ja ilmoittaa virheellisestä merkkijonosta,
## liittää hyväksytyt merkkijonot yhteen ja lopuksi tulostaa ne käyttäjälle.
##
## Globaalit kiintoarvot:
## PITUUS_MIN = merkkijonon minimipituus.
## PITUUS_MAX = merkkijonon maksimipituus.
## EROTIN = merkki, jota ei saa käyttää merkkijonoissa, käytetään erottamaan annetut merkkijonot toisistaan.
## 
## Aliohjelmien muuttujat:
## Kehote = Pääohjelmasta saatu parametri joka tulostetaan käyttäjälle merkkijonoa kysyttäessä riippuen ehdoista.
## Merkit = käyttäjän antama merkkijono, palautetaan pääohjelmaan.
## TarkastusMerkit = pääohjelmasta saatu parametri, tarkastetaan käyttäjän antaman merkkijonon oikeellisuus.
## OikeatMerkkijonot = pääohjelmasta saatu parametri, käytetään tulostamaan käyttäjälle takaisin hyväksytyt merkkijonot. 
## 
## Pääohjelman muuttujat:
## HyvaksytytMerkkijonot = kokooja hyväksytyille merkkijonoille
## Kysymys = kysyMerkkijono aliohjelmaan lähetettävä parametri (kehote) joka riippuu ehdoista.
## Todennus = BOOLEAN, käytetään merkkijonon tarkastuksessa, True = hyväksytty, False = hylätty (epähuomioidaan), None = ohjelman alussa tai kun ei ole annettu hyväksyttyjä merkkijonoja.
## Merkkijono = kysyMerkkijono:sta saatu paluuarvo tallennetaan tänne jatkokäsittelyä varten.
##
## 
## Suoritettava ohjelma alkaa:

# Globaalit kiintoarvot:
PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'

# Aliohjelmat:
def tulostaOhjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.")
    print()
    return None

def kysyMerkkijono(Kehote):
    print(Kehote + " merkkijono 5-15 merkkiä (enter lopettaa): ",end='')
    Merkit = input()
    return Merkit

def tarkistaMerkkijono(TarkastusMerkit):
    if(TarkastusMerkit == ""):      # Todennus -> None, jos käyttäjä lopettaa (painaa enter)
        return None
    elif(len(TarkastusMerkit) < PITUUS_MIN):
        print("Liian lyhyt, ",len(TarkastusMerkit)," merkkiä.",sep='')
        return False
    elif(len(TarkastusMerkit) > PITUUS_MAX):
        print("Liian pitkä, ",len(TarkastusMerkit)," merkkiä.",sep='')
        return False
    elif(EROTIN in TarkastusMerkit):
        print("Merkkijonossa on kielletty merkki '",EROTIN,"'.",sep='')
        return False
    else:
        return True
    
def tulostaHyvaksytyt(OikeatMerkkijonot):
    print()
    print("Annoit seuraavat hyväksytyt merkkijonot:",sep='',end='')     # Jatketaan seuraava rivi tälle riville muotoilun vuoksi...
    print(OikeatMerkkijonot.replace(EROTIN,"\n"))                       # .replace(EROTIN,"\n") korvaa EROTIN -merkin uudella rivillä. En löytänyt muuta tapaa suorittaa tämä kuin tällä.

    return None


# Pääohjelma:
def paaohjelma():
    # Alustus:
    HyvaksytytMerkkijonot = ""
    Kysymys = ""
    Todennus = None
    # Ohjeet:
    tulostaOhjeet()

    while(True):
        if(Todennus == None):           # Ensimmäisellä kierroksella Todennus : on None, joten tämä if lohko suoritetaan vain ohjelman alussa.
            Kysymys = "Anna"
        elif(Todennus == True):         # Tarkastellaan oliko edellinen merkkijono hyväksytty
            Kysymys = "Anna seuraava"
        elif(Todennus == False):        # Tarkastellaan oliko edellinen merkkijono hylätty
            Kysymys = "Anna uusi"
            
        Merkkijono = kysyMerkkijono(Kysymys)    
        Todennus = tarkistaMerkkijono(Merkkijono)
        
        if(Todennus == True):
            HyvaksytytMerkkijonot = HyvaksytytMerkkijonot + EROTIN + Merkkijono
            
        elif(Todennus == None):         # Aliohjelma palauttaa Todennus :ksen None, jos käyttäjä lopettaa (painaa enter)
            if(HyvaksytytMerkkijonot == ""):        # Jos käyttäjä ei ole antanut yhtään hyväksyttyä merkkijonoa tulostetaan seuraava ja lopetetaan:
                print()
                print("Et antanut yhtään hyväksyttävää merkkijonoa.")
                break
            else:                                   # Muussa tapauksessa tulostetaan kaikki hyväksytyt ja lopetetaan.
                tulostaHyvaksytyt(HyvaksytytMerkkijonot)
                break

    # Vakiotulostus:
    print("Kiitos ohjelman käytöstä.")
    return None
    


# Päätaso
paaohjelma()

# eof
