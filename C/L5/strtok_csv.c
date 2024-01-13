/**
 * Teemu Hiltunen; 000000000; 15.02.2023; L5T2.c
 *
 * Ohjelman tarkoitus on harjoittaa esimerkiksi CSV tiedoston lukua strtokilla
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MERKKIJONO 30
#define RIVIPITUUS 30
#define EROTIN ";"

void kysyNimi(char *pNimi);
void lueTiedosto();

int main()
{
    char aTiedNimi[MERKKIJONO];

    kysyNimi(aTiedNimi);
    lueTiedosto(aTiedNimi);

    printf("Kiitos ohjelman käytöstä.\n");

    return (0);
}

void kysyNimi(char *pNimi)
{
    printf("Anna luettavan tiedoston nimi: ");
    scanf("%s", pNimi);
    return;
}

void lueTiedosto(char *pNimi)
{
    char aRivi[RIVIPITUUS], aAlin[RIVIPITUUS];
    int iAlin = 0, iPiste;
    char *pSarake, *pSarake1, *pAlin = aAlin;
    FILE *Tiedosto;

    if ((Tiedosto = fopen(pNimi, "r")) == NULL)
    {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }

    while (fgets(aRivi, RIVIPITUUS, Tiedosto) != NULL)
    {
        pSarake = strtok(aRivi, EROTIN);
        pSarake1 = strtok(NULL, EROTIN);
        iPiste = atoi(pSarake1);

        if (iAlin == 0)
        {
            iAlin = iPiste;
        }

        if (iPiste < iAlin)
        {
            strcpy(pAlin, pSarake);
            iAlin = iPiste;
        }
    }

    printf("Tiedosto '%s' luettu.\n", pNimi);
    printf("Pienin pistemäärä oli joukkueella '%s' %d pisteellä.\n", pAlin, iAlin);

    fclose(Tiedosto);

    return;
}

// End of File
