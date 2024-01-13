# Makefile omakirjasto_harjoitus
omakirjasto_harjoitus: omakirjasto_harjoitus.o OmaKirjasto.o
	gcc omakirjasto_harjoitus.o OmaKirjasto.o -o omakirjasto_harjoitus

omakirjasto_harjoitus.o: omakirjasto_harjoitus.c OmaKirjasto.h
	gcc omakirjasto_harjoitus.c -c -std=c99 -Wall -pedantic

OmaKirjasto.o: OmaKirjasto.c OmaKirjasto.h
	gcc OmaKirjasto.c -c -std=c99 -Wall -pedantic
	