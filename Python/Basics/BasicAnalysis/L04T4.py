## Teemu Hiltunen, 30.9.2022, L04T4
## Valikkopohjainen ohjelma, jota parannetaan edelliseen viikkon verrattuna. Käyttäjä valitsee valikosta haluamansa
## toimii sen mukaisesti ja päättää ohjelman kun haluaa.
## 
## Muuttujat:
## Summa = tähän lasketaan annettujen numeroiden summa
## Numero1 = alustetaan muuttuja, jotta vältytään virheeltä tapauksessa jossa käyttäjä yrittää laskea suoraan antamatta arvoja
## Numero2 = alustetaan muuttuja, jotta vältytään virheeltä tapauksessa jossa käyttäjä yrittää laskea suoraan antamatta arvoja
## Valinta = käyttäjän antama valintasyöte
## Numero1 = ensimmäinen käyttäjän antama numero   käyttäjän syöte kirjoitetaan suoraan muunnetussa muodossa muuttujaan
## Numero2 = toinen käyttäjän antama numero        käyttäjän syöte kirjoitetaan suoraan muunnetussa muodossa muuttujaan
##
## Ohjelma alkaa:

Summa = 0
Numero1 = 0
Numero2 = 0
# Tulostus käyttäjälle ohjelman tehtävästä:
print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
# While silmukka jota toistetaan kunnes siitä poistutaan break komennolla.
while(True):
    # Valikon tulostus joka iteraation alussa:
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")

    # Pyydetään käyttäjältä valinta:
    Valinta = input('Anna valintasi: ')
    # Tarkastellaan valintaa ja toimitaan valinnan mukaan:
    if(Valinta != '0' and Valinta != '1' and Valinta != '2' and Valinta != '3'): ## Jos käyttäjä antaa jonkun muun kuin '0' '1' '2' '3' ilmoitetaan virheestä 
        print("Tuntematon valinta, yritä uudestaan.")
    elif(Valinta == '1'):           
        print("Syötä tiedot")
        Numero1 = int(input("Anna luku 1: ")) # Kirjataan käyttäjän antamat numerot suoraan kokonaislukuina muuttujiin
        Numero2 = int(input("Anna luku 2: ")) # Kirjataan käyttäjän antamat numerot suoraan kokonaislukuina muuttujiin
    elif(Valinta == '2'):
        print("Laske")
        Summa = Numero1 + Numero2           # Suoritetaan annettujen numeroiden yhteenlasku ja tallennetaan muuttujaan Summa
    elif(Valinta == '3'):
        print("Tulosta tulokset")
        print("Lukujen summa on ",Summa,'.',sep='')
    elif(Valinta == '0'):
        print("Lopetetaan.")            # Lopetetaan näin pyydettäessä
        break
    print('')  # Tulostetaan rivi joka iteraation väliin.

# Vakiolopetus:
print("\n","Kiitos ohjelman käytöstä.",sep='')
