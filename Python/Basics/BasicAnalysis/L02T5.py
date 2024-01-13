# Constants:
KgIsInPounds = 1/0.4536
FeetInMeter = 0.3048
FeetInInch = 12

# Preliminary output of software:
print('Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.')
# Input of weight
WeightKg = input('Anna paino kiloina: ')
# and conversion
WeightInKgFloat = float(WeightKg)
WeightInPound = WeightInKgFloat * KgIsInPounds

# Output of weight:
print('Paino on ',round(WeightInKgFloat,1),' kg eli ',round(WeightInPound,1),' naulaa.','\n',sep='')

# Input of height
HeightCm = input('Anna pituus sentteinä: ')

# Conversion of height:
HeightCmFloat = float(HeightCm)
HeightInMeter = HeightCmFloat / 100
HeightInFeetFloat = HeightInMeter / FeetInMeter
HeightInFeet = HeightInFeetFloat - (HeightInFeetFloat - int(HeightInFeetFloat)) # Hey, as long as it works, right!?
RemainderHeightInInch = (HeightInFeetFloat - HeightInFeet) * FeetInInch

# Printing output of height
print('Pituus on',round(HeightInMeter,2),'metriä ',end='')
print('eli amerikkalaisittain',round(HeightInFeet,1),'jalkaa',end='')
print(' ja ',round(RemainderHeightInInch,1),' tuumaa.',sep='')
print('Kiitos ohjelman käytöstä.')
