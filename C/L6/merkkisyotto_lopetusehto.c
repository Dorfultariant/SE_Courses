/**
 * Teemu Hiltunen; 000000000; 21.02.2023; L6T1.c
 *
 * Lukee käyttäjän antamia merkkejä linkitettyyn listaan kunnes lopetusehto annetaan
 *      ja lopuksi tulostaa merkit
 *
 * Yksinkertaisen linkitetyn listan perusperiaate.
 */

#include <stdio.h>
#include <stdlib.h>

#define LOPETA 'q'

typedef struct merkit
{
    char cMerkki;
    struct merkit *pSeuraava;
} MERKIT;

int main()
{
    char cKysytty;
    MERKIT *pAlku = NULL, *pLoppu = NULL;
    MERKIT *pUusi, *ptr;

    printf("Anna listan kirjaimet.\n");

    // Kysytään käyttäjältä arvot kunnes lopetusmerkki annetaan:
    printf("Anna kirjain, q lopettaa: ");
    cKysytty = getc(stdin);
    getchar();

    while (LOPETA != cKysytty)
    {
        if ((pUusi = (MERKIT *)malloc(sizeof(MERKIT))) == NULL)
        {
            perror("Muistin varaus epäonnistui");
            exit(1);
        }

        pUusi->cMerkki = cKysytty;
        pUusi->pSeuraava = NULL;

        if (pAlku == NULL)
        {
            pAlku = pUusi;
            pLoppu = pUusi;
        }
        else
        {
            pLoppu->pSeuraava = pUusi;
            pLoppu = pUusi;
        }
        printf("Anna kirjain, q lopettaa: ");
        cKysytty = getc(stdin);
        getchar();
    }

    printf("Listassa on seuraavat kirjaimet:\n");
    ptr = pAlku;
    while (ptr != NULL)
    {
        printf("%c ", ptr->cMerkki);
        ptr = ptr->pSeuraava;
    }

    puts("");
    puts("");

    // Vapautussilmukka:
    ptr = pAlku; // Asetetaan apuosoitin ptr:lle pAlku:n osoite
    while (ptr != NULL)
    {
        pAlku = ptr->pSeuraava; // Otetaan talteen seuraavaan tietueeseen osoittavan osoitin
        free(ptr);              // Vapautetaan nykyinen tietue-osoitin
        ptr = pAlku;            // Asetetaan nykyinen ptr osoittamaan seuraavaan tietueeseen
    }
    ptr = NULL;
    pAlku = NULL;

    printf("Muisti vapautettu.\n");
    printf("Kiitos ohjelman käytöstä.\n");

    return (0);
}

// End of File