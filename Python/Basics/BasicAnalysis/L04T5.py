## Teemu Hiltunen, 2.10.2022, L04T5
## Ohjelmalla tarkastellaan lukujen jaollisuutta 5:llä ja 7:llä annetulla lukualueella. 
## 
## Muuttujat:
## AlaRaja = muunnettu käyttäjän antama alaraja-arvo
## YlaRaja = muunnettu käyttäjän antama yläraja-arvo
## i = for lauseen iteraattori
## 
##
## Ohjelma alkaa:

# Ohjelman tehtävän tulostus:
print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")

# Käyttäjän syötteiden vastaanotto ja muunnos:
AlaRaja = int(input("Anna lukualueen alaraja: "))
YlaRaja = int(input("Anna lukualueen yläraja: "))


for i in range(AlaRaja,YlaRaja + 1):   # Määrätään i:n iteraatioalue, koska range ei ota ylärajaa mukaan i:n alueeseen, lisätään YlaRaja +1.
    if(AlaRaja % 5 != 0):               # Tarkastellaan onko AlaRaja jaollinen 5, jos on niin jakojäännökseksi tulee 0, muuten ei.
        print(AlaRaja," ei ole jaollinen viidellä, hylätään.",sep='')
    elif(AlaRaja % 7 != 0):             # Tarkastellaan onko AlaRaja jaollinen 7, jos on niin jakojäännökseksi tulee 0, muuten ei.
        print(AlaRaja," ei ole jaollinen seitsemällä, hylätään.",sep='')
    elif(AlaRaja % 5 == 0 and AlaRaja % 7 == 0):        # Tarkastellaan onko AlaRaja jaollinen 5 ja 7:llä jos on niin ohjelma tulostaa ja lopettaa.
        print("Luku ",AlaRaja," on jaollinen 5:llä ja 7:llä.",sep='')
        print("Lopetetaan etsintä.")
        break

    if(AlaRaja == YlaRaja):         # Tarkastellaan onko iteraatioalue käyty läpi, jos on niin ohjelma tulostaa ja lopettaa.
        print("Alueelta ei löytynyt sopivaa lukua.")
        break
    AlaRaja = AlaRaja + 1           # Lisätään AlaRaja:aan +1 joka kierroksen lopussa, jolloin saadaan seuraavan kierroksen uusi testattava luku. 
                                    # Suoritetaan lopussa, koska halutaan uusi luku vasta seuraavalle kierrokselle.

# Vakiotulostus ja ohjelma päättyy:
print("Kiitos ohjelman käytöstä.")
