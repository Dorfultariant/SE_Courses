// Teemu Hiltunen; 000000000; 28.2.2023; L7T1.c
#include <string.h>
#include "OmaKirjasto.h"

void kysyNimi(char *pTiedostonimi)
{
    printf("Anna luettavan tiedoston nimi: ");
    scanf("%s", pTiedostonimi);
    getchar();
    return;
}

RIVI *lueTiedosto(char *pTiedostonimi, RIVI rivitaulu[], int *pTuontiSumma)
{
    FILE *Tiedosto;
    char aRivi[RIVIPITUUS];
    char *pSarake, *pSarake1;
    int i = 0;

    if ((Tiedosto = fopen(pTiedostonimi, "r")) == NULL)
    {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    // Otsikkorivin luku:
    fgets(aRivi, RIVIPITUUS, Tiedosto);
    while ((fgets(aRivi, RIVIPITUUS, Tiedosto)) != NULL)
    {
        RIVI luettuRivi;
        pSarake = strtok(aRivi, EROTIN);
        pSarake1 = strtok(NULL, EROTIN);
        *pTuontiSumma += atoi(pSarake1);

        luettuRivi.vuosi = atoi(pSarake);
        luettuRivi.tuontiEuroina = atoi(pSarake1);
        rivitaulu[i] = luettuRivi;
        i++;
    }

    fclose(Tiedosto);

    printf("Tiedosto '%s' luettu.\n", pTiedostonimi);

    return rivitaulu;
}

void tulostaTiedot(RIVI rivitaulu[], int *pTuontisumma)
{
    printf("Akvaariokalojen tuonti euroina:\n");

    for (int i = 0; i < RIVITAULU; i++)
    {
        printf("%d\t%d", rivitaulu[i].vuosi, rivitaulu[i].tuontiEuroina);
        puts("");
    }
    printf("Ajanjaksolla tuonti oli yhteensä %d euroa.\n", *pTuontisumma);
    return;
}