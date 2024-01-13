/*
 * Teemu Hiltunen; 000000000; 06.02.2023; L4T1.c
 *
 *
 * Yksinkertaisen ohjelman tarkoitus on kysyä käyttäjältä jonkin kappaleen tietoja ja sitten tulostaa tiedot käyttäjälle.
 *     Harjoittaa tietueen käyttöä staattisella tavalla.
 */

#include <stdio.h>
#include <string.h>

#define JONOPITUUS 50

struct Kappale
{
    char aNimi[JONOPITUUS];
    char aEsittaja[JONOPITUUS];
    char aKesto[JONOPITUUS];
    int iJulkaisuvuosi;
};

int main()
{
    char aNimi[JONOPITUUS];
    char aEsittaja[JONOPITUUS];
    char aKesto[JONOPITUUS];
    int iJulkaisuvuosi;

    struct Kappale kappale1;

    printf("Anna kappaleen nimi: ");
    fgets(aNimi, JONOPITUUS, stdin);
    aNimi[strlen(aNimi) - 1] = '\0';

    printf("Anna kappaleen esittäjä: ");
    fgets(aEsittaja, JONOPITUUS, stdin);
    aEsittaja[strlen(aEsittaja) - 1] = '\0';

    printf("Anna kappaleen pituus: ");
    fgets(aKesto, JONOPITUUS, stdin);
    aKesto[strlen(aKesto) - 1] = '\0';

    printf("Anna kappaleen julkaisuvuosi: ");
    scanf("%d", &iJulkaisuvuosi);

    strcpy(kappale1.aNimi, aNimi);
    strcpy(kappale1.aEsittaja, aEsittaja);
    strcpy(kappale1.aKesto, aKesto);
    kappale1.iJulkaisuvuosi = iJulkaisuvuosi;

    printf("Kappaleen nimi on '%s' ja esittäjä '%s'.\n", kappale1.aNimi, kappale1.aEsittaja);
    printf("Kappale on %s minuuttia pitkä ja julkaistu vuonna %d.\n", kappale1.aKesto, kappale1.iJulkaisuvuosi);

    printf("Kiitos ohjelman käytöstä.\n");
    return (0);
}

// End of File