//
/**
 * Teemu Hiltunen; 000000000; 21.02.2023; L6T1.c
 *
 * Jatkoa linkitetylle listalle, varaa, lukee, tallentaa, tulostaa ja vapauttaa
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TIEDOSTO 30
#define TEHTAVA 5
#define EROTIN ";"

typedef struct rivi
{
    char aTehtava[TEHTAVA];
    int iMaara;
    struct rivi *pSeuraava;
} RIVI;

void muistiVaraus(RIVI **pUusi);
void kysyNimi(char *pNimi);
RIVI *lueTiedosto(char *pNimi);
void tulostaTiedot(RIVI *pAlku);
void muistiVapaus(RIVI *pAlku);

int main()
{
    char aTiedostonimi[TIEDOSTO];
    RIVI *pAlku = NULL;

    kysyNimi(aTiedostonimi);
    pAlku = lueTiedosto(aTiedostonimi);
    tulostaTiedot(pAlku);
    muistiVapaus(pAlku);

    printf("Kiitos ohjelman käytöstä.\n");
    return (0);
}

void muistiVaraus(RIVI **pUusi)
{
    if ((*pUusi = (RIVI *)malloc(sizeof(RIVI))) == NULL)
    {
        perror("Muistin varaus epäonnistui");
        exit(1);
    }
    return;
}

void kysyNimi(char *pNimi)
{
    printf("Anna luettavan tiedoston nimi: ");
    scanf("%s", pNimi);
    return;
}

RIVI *lueTiedosto(char *pNimi)
{
    char aRivi[TIEDOSTO];
    char *pSarake, *pSarake1;

    RIVI *pAlku = NULL, *pLoppu = NULL;

    FILE *Tiedosto;

    if ((Tiedosto = fopen(pNimi, "r")) == NULL)
    {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }

    while (fgets(aRivi, TIEDOSTO, Tiedosto) != NULL)
    {
        RIVI *pUusi;
        muistiVaraus(&pUusi);
        pSarake = strtok(aRivi, EROTIN);
        pSarake1 = strtok(NULL, EROTIN);

        strcpy(pUusi->aTehtava, pSarake);
        pUusi->iMaara = atoi(pSarake1);
        pUusi->pSeuraava = NULL;

        // Linkitetyn listan täytön tarkastelua:
        if (pAlku == NULL)
        { // Mikäli ensimmäistä alkiota ei ole vielä asetettu niin suoritetaan tämä
            pAlku = pUusi;
            pLoppu = pUusi;
        }
        else
        { // Muussa tapauksessa lisätään uusi tietue linkitetyn listan loppuun
            pLoppu->pSeuraava = pUusi;
            pLoppu = pUusi;
        }
    }

    printf("Tiedosto '%s' luettu linkitettyyn listaan.\n", pNimi);
    fclose(Tiedosto);
    return (pAlku);
}

void tulostaTiedot(RIVI *pAlku)
{
    RIVI *ptr;
    ptr = pAlku;
    printf("Tehtäviä tehtiin seuraavasti:\n");
    while (ptr != NULL)
    {
        printf("Tehtävän %s teki %d opiskelijaa.\n", ptr->aTehtava, ptr->iMaara);
        ptr = ptr->pSeuraava;
    }
    return;
}

void muistiVapaus(RIVI *pAlku)
{
    RIVI *ptr;
    ptr = pAlku;
    while (ptr != NULL)
    {
        pAlku = ptr->pSeuraava; // Otetaan talteen seuraavan tietueen osoite
        free(ptr);              // Vapautetaan nykyinen
        ptr = pAlku;            // Asetetaan seuraavan tietueen osoite nykyiseksi
    }
    puts("");
    printf("Muisti vapautettu.\n");
    return;
}

// End of File
