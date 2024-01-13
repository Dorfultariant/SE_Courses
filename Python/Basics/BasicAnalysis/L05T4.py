## Ohjelman hallintoa: Teemu Hiltunen, 8.10.2022, L05T4
## Kyseessä on valikkopohjainen ohjelma, joka kysyy käyttäjältä kaksi kokonaislukua, laskee niiden summan ja erotuksen
## Sekä tulostaa tiedot käyttäjälle. Valintojen perusteella luonnollisesti.
## 
## Aliohjelmien muuttujat:
## Valinta = valikko :aliohjelman sisällä, valinta jonka käyttäjä tekee.
## SyoteValinta = käyttäjän syötteen tallennuspaikka, muunnetaan kokonaisluvuksi -> Valinta :muuttujaan.
## Kehote = pääohjelmasta tullut kehote joka tulostetaan käyttäjälle ennen lukujen kysymistä.
## Luku = muunnettu kysytyn luvun sijoituspaikka, palautetaan pääohjelmaan.
## SyoteLuku = käyttäjän antaman syötteen sijoituspaikka
## SumLuku1 = pääohjelmasta tullut parametri, käyttäjän ensimmäinen antama luku
## SumLuku2 = pääohjelmasta tullut parametri, käyttäjän toinen antama luku
## Sum = summan säilö, palautetaan pääohjelmaan.
## EroLuku1 = pääohjelmasta tullut parametri, käyttäjän ensimmäinen luku
## EroLuku2 = pääohjelmasta tullut parametri, käyttäjän toinen luku
## Ero = lukujen erotus, palautetaan pääohjelmaan.
## Arvo1 = käyttäjän ensimmäinen antama luku
## Arvo2 = käyttäjän toinen antama luku
## Tulos1 = Summan arvo
## TUlos2 = Erotuksen arvo
##
## Pääohjelman muuttujat:
##  Toiminto = valikosta saatu valinta
##  KokonaisLuku1 = käyttäjän antama ensimmäinen kokonaisluku
##  KokonaisLuku2 = käyttäjän antama toinen kokonaisluku
##  Yhteensa = yhteenlaskun tulos
##  Vahenna = erotuksen tulos
##
## Suoritettava ohjelma alkaa:


# Aliohjelmat:
def valikko():
    Valinta = 0
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    SyoteValinta = input("Anna valintasi: ")
    Valinta = int(SyoteValinta)
    return Valinta

def kysyLuku(Kehote):
    Luku = 0
    print(Kehote,end='')
    SyoteLuku = input()
    Luku = int(SyoteLuku)
    return Luku

def summa(SumLuku1, SumLuku2):
    Sum = SumLuku1 + SumLuku2
    return Sum

def erotus(EroLuku1, EroLuku2):
    Ero = EroLuku1 - EroLuku2
    return Ero

def tulostaTulokset(Arvo1, Arvo2, Tulos1, Tulos2):
    print("Tulosta tulokset")
    print("Luvut ovat ",Arvo1, " ja ",Arvo2,'.',sep='')
    print("Lukujen summa on ",Tulos1," ja erotus on ",Tulos2,'.',sep='')

    return None
    

# Pääohjelma:
def paaohjelma():
    # Alustus:
    Toiminto = 0
    KokonaisLuku1 = 0
    KokonaisLuku2 = 0
    Yhteensa = 0
    Vahenna = 0
    # Alkutulostus:
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    
    while(True):
        Toiminto = valikko()

        if(Toiminto == 1):
            print("Syötä tiedot")
            KokonaisLuku1 = kysyLuku("Anna kokonaisluku 1: ")
            KokonaisLuku2 = kysyLuku("Anna kokonaisluku 2: ")
        elif(Toiminto == 2):
            print("Laske")
            Yhteensa = summa(KokonaisLuku1, KokonaisLuku2)
            Vahenna = erotus(KokonaisLuku1, KokonaisLuku2)
        elif(Toiminto == 3):
            tulostaTulokset(KokonaisLuku1, KokonaisLuku2, Yhteensa, Vahenna)
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

# eof
