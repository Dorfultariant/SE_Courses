// Teemu Hiltunen; 000000000; 28.2.2023; L7T1.c

#ifndef OMAKIRJASTO_H
#define OMAKIRJASTO_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TIEDOSTONIMI 30
#define RIVITAULU 10
#define RIVIPITUUS 50
#define EROTIN ";"

typedef struct rivi
{
    int vuosi;
    int tuontiEuroina;
} RIVI;

void kysyNimi(char *pTiedostonimi);
RIVI *lueTiedosto(char *pTiedostonimi, RIVI rivitaulu[], int *pTuontiSumma);
void tulostaTiedot(RIVI rivitaulu[], int *pTuontisumma);

#endif // OMAKIRJASTO_H