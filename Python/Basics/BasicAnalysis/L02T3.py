## User input:
print('Tämä ohjelma laskee neljän tenttiarvosanan keskiarvon.')
FirstTestRating = input('Anna 1. tenttiarvosana väliltä 0-5: ')
SecondTestRating = input('Anna 2. tenttiarvosana väliltä 0-5: ')
ThirdTestRating = input('Anna 3. tenttiarvosana väliltä 0-5: ')
FourthTestRating = input('Anna 4. tenttiarvosana väliltä 0-5: ')

## Conversion:
FirstTestRatingInt = int(FirstTestRating)
SecondTestRatingInt = int(SecondTestRating)
ThirdTestRatingInt = int(ThirdTestRating)
FourthTestRatingInt = int(FourthTestRating)

## Calculations:
NofTest = 4
Sum = FirstTestRatingInt + SecondTestRatingInt + ThirdTestRatingInt + FourthTestRatingInt
Average = Sum / NofTest
RndAvg = round(Average,1)
TestAvgInt = int(RndAvg)

## Outputs:
print('\n','Antamiesi arvosanojen summa on ',Sum,'.',sep='')
print('Antamiesi arvosanojen keskiarvo on ',RndAvg,'.',sep='')
print('Keskiarvo on kokonaislukuna ',TestAvgInt,'.',sep='')
print('Kiitos ohjelman käytöstä.')
