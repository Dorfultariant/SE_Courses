print('Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.')
print('Valitse haluamasi toiminto:')
print('1) Tulosta merkkijono etuperin')
print("2) Tulosta merkkijono takaperin")
print("3) Tulosta merkkijonon pituus")
print("0) Lopeta")

Option = input('Anna valintasi: ')

if(Option != '0' and Option != '1' and Option != '2' and Option != '3'):
    print('Tuntematon valinta.')

elif(Option == '0'):
    print('Lopetetaan')
else:
    CharLine = input('Anna merkkijono: ')
    
    if(Option == '1'):
        print('Merkkijono on etuperin \'',CharLine,'\'.',sep='')

    if(Option == '2'):
        print('Merkkijono on takaperin \'',CharLine[::-1],'\'.',sep='')

    if(Option == '3'):
        print('Merkkijonon pituus on ',len(CharLine),'.',sep='')

print('Kiitos ohjelman käytöstä.')
