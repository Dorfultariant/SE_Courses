print('Tämä ohjelma laskee risteilyhintoja.')
CabinC = round(79)
CabinB = round(CabinC * 1.1)
CabinA = round(CabinC * 1.6)

UseCabin = 0.0
SeasonAdd = 0.0
SalePrice = 0.0
RegCustomerAdd = 0.9

Cabin = input('Minkälainen hytti on kyseessä - A, B vai C-hytti: ')
SeasonTime = input('Onko sesonkiaika (k/e): ')
RegCustomer = input('Onko kanta-asiakas (k/e): ')

## Definition for calculations:
if(Cabin == 'A'):
    UseCabin = CabinA
    SeasonAdd = 2.75
elif(Cabin == 'B'):
    UseCabin = CabinB
    SeasonAdd = 1.75
elif(Cabin == 'C'):
    UseCabin = CabinC
    SeasonAdd = 1.5

## Normal price outside of season time without regular customer sale:
if(SeasonTime != 'K' and SeasonTime != 'k' and RegCustomer != 'K' and RegCustomer != 'k'):
    print(Cabin,'-hytti maksaa ',round(float(UseCabin),2),' euroa.',sep='')

## Sale price:
if(SeasonTime == 'K' or SeasonTime == 'k'):
    if(RegCustomer == 'K' or RegCustomer == 'k'): ## Regular Customer Sale during season
        SalePrice = round(UseCabin * SeasonAdd * RegCustomerAdd,2)
        print(Cabin,'-hytti maksaa ',SalePrice,' euroa.',sep='')
    else: ## Non regular customer price during season:
        SalePrice = round(UseCabin * SeasonAdd,2)
        print(Cabin,'-hytti maksaa ',SalePrice,' euroa.',sep='')
else: ## Regular Customer outside of season time:
    if(RegCustomer == 'K' or RegCustomer == 'k'):
        SalePrice = round(UseCabin * RegCustomerAdd,2)
        print(Cabin,'-hytti maksaa ',SalePrice,' euroa.',sep='')

print('Kiitos ohjelman käytöstä.')





