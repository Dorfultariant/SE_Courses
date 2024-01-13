print('Selvitetään tuotteen alennusprosentti ja myyntihinta.')
ListPrice = float(input('Mikä on tuotteen listahinta: '))
print('Lasketaanko hinta','\n','1) yhdellä monihaaraisella valintarakenteella\n','2) useilla erillisillä valintarakenteilla?',sep='')
Option = input('Anna valintasi: ')
##LoweredPrice = 0
Sale = ''
if(Option != '1' and Option != '2'):
    print('Tuntematon valinta. Tuotteen alennus on 0% ja hinnaksi jää ',format(ListPrice,'.2f'),'e.',sep='')

# a.
if(Option == '1'):
    print('Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:')
    if(ListPrice >= 300): ## i
        ListPrice = ListPrice * 0.7
        print('Tuotteen alennus on 30% ja hinnaksi jää ',format(ListPrice,'.2f'),'e.',sep='')
    elif(ListPrice >= 200): ## ii
        ListPrice = ListPrice * 0.8
        print('Tuotteen alennus on 20% ja hinnaksi jää ',format(ListPrice,'.2f'),'e.',sep='')
    elif(ListPrice >= 100): ## iii
        ListPrice = ListPrice * 0.9
        print('Tuotteen alennus on 10% ja hinnaksi jää ',format(ListPrice,'.2f'),'e.',sep='')
    
# b.
if(Option == '2'):
    print('Monella erillisellä valintarakenteella tulokset ovat seuraavat:')
    if(ListPrice >= 300): ## i
        ListPrice = ListPrice * 0.7
        Sale = '30%'
    if(ListPrice >= 200): ## ii
        ListPrice = ListPrice * 0.8
        Sale = '20%'
    if(ListPrice >= 100): ## iii
        ListPrice = ListPrice * 0.9
        Sale = '10%'
    print('Tuotteen alennus on ',Sale,' ja hinnaksi jää ',format(ListPrice,'.2f'),'e.',sep='')

print('Kiitos ohjelman käytöstä.')
