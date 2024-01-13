/**
 * Teemu Hiltunen; 000000000; 28.2.2023; L7T1.c
 *
 * Oman kirjaston käyttöharjoitus
 */

#include <stdio.h>
#include "OmaKirjasto.h"

int main()
{
    char aTiedostonimi[TIEDOSTONIMI];
    RIVI rivitaulu[RIVITAULU];
    RIVI *pRivitaulu = rivitaulu;
    int iTuontiSumma = 0;

    kysyNimi(aTiedostonimi);
    pRivitaulu = lueTiedosto(aTiedostonimi, rivitaulu, &iTuontiSumma);

    tulostaTiedot(rivitaulu, &iTuontiSumma);

    puts("");
    printf("Kiitos ohjelman käytöstä.\n");
    return 0;
}
