# User input of the first part:
LongWord = input('Anna sana: ')

# Outputs of first part:
print('Antamasi sanan kolme ensimmäistä kirjainta ovat ',LongWord[0:3],sep='')
print('Sanan neljä viimeistä kirjainta ovat ',LongWord[-4:],sep='')
print('Kirjaimet 3, 4, 5 ja 6 ovat ',LongWord[2:6],sep='')
print('\n','Sanan joka kolmas kirjain alkaen ensimmäisestä kirjaimesta: ',LongWord[0::3],sep='')
print('\n','Antamasi sana \'',LongWord,'\' ','on takaperin \'',LongWord[::-1],'\'.','\n',sep='')

# User input of the second part, also the conversion from char to int:
StartPoint = input('Anna aloituspaikka: ')
EndPoint = input('Anna lopetuspaikka: ')
Displacement = input('Anna siirtymä: ')
StartPointInt = int(StartPoint)
EndPointInt = int(EndPoint)
DisplacementInt = int(Displacement)

# Outputs of last part:
print('Antamillasi asetuksilla sana ',LongWord,' tulostuu näin: ',LongWord[StartPointInt:EndPointInt:DisplacementInt],sep='')
print('\n','Antamasi sanan pituus oli ',len(LongWord),' merkkiä.',sep='')
print('Kiitos ohjelman käytöstä.')
