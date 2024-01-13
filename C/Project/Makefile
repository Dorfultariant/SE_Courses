# Makefile HT Teemu Hiltunen 02.03.2023
HT: HT.o HTPerusKirjasto.o
	gcc HTPerustaso.o HTPerusKirjasto.o -o HT
	rm -f *.o

HT.o: HTPerustaso.c HTPerusKirjasto.h
	gcc HTPerustaso.c -c -std=c99 -Wall -pedantic
	
HTPerusKirjasto.o: HTPerusKirjasto.c HTPerusKirjasto.h
	gcc HTPerusKirjasto.c -c -std=c99 -Wall -pedantic
