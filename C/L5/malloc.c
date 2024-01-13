/**
 *  Teemu Hiltunen; 000000000; 13.02.2023; L5T1.c
 *
 * Ohjelman tarkoitus on varata kiinteä määrä muistia "dynaamisesti" mallocilla.
 *  Harjoittaa mallocin käyttöä ja sen virheenkäsittelyä.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MERKKIJONO 30

void muistiVaraus(char **pMerkkijono);
void kysyMerkkijono(char *pMerkkijono);

int main()
{
    char *pMerkkijono;
    muistiVaraus(&pMerkkijono);
    kysyMerkkijono(pMerkkijono);
    printf("Annoit merkkijonon '%s'.\n", pMerkkijono);
    pMerkkijono = NULL;
    free(pMerkkijono);
    printf("Muisti vapautettu.\n");
    printf("Kiitos ohjelman käytöstä.\n");
    return (0);
}

void muistiVaraus(char **pMerkkijono)
{
    *pMerkkijono = (char *)malloc(sizeof(char) * MERKKIJONO);
    if (*pMerkkijono == NULL)
    {
        perror("Muistinvaraus epäonnistui");
        free(*pMerkkijono);
        exit(0);
    }
    printf("Muisti varattu %d merkille.\n", MERKKIJONO);
    return;
}

void kysyMerkkijono(char *pMerkkijono)
{
    printf("Anna merkkijono: ");
    fgets(pMerkkijono, MERKKIJONO, stdin);
    pMerkkijono[strlen(pMerkkijono) - 1] = '\0';
    return;
}

// End of File