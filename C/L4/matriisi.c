/**
 * Teemu Hiltunen; 000000000; 08.02.2023; L4T4.c
 *
 *
 * Ohjelman kysyy kokonaislukuja vakiokokoiseen taulukkoon lisättäväksi ja tulostaa matriisin transpoosin
 *  Ohjelman tarkoitus on harjoittaa taulukon määrittelyä ja käsittelyä
 */

#include <stdio.h>
#include <stdlib.h>

#define RIVI 3
#define SARAKE 3
#define TIEDOSTOKEHOTEPITUUS 30

void kysyNimi(char *pTiedostonimi);
void tulostaMatriisi(char *pTiedostonimi, int aMatriisi[RIVI][SARAKE], char *pKehote); //

int main()
{
    int aMatriisi[RIVI][SARAKE], aTransMatriisi[SARAKE][RIVI];
    char aTiedostonimi[TIEDOSTOKEHOTEPITUUS];

    kysyNimi(aTiedostonimi);

    // Kysytään käyttäjältä matriisin arvot:
    printf("Anna arvot lähtömatriisille: \n");
    for (int i = 0; i < RIVI; i++)
    {
        for (int j = 0; j < SARAKE; j++)
        {
            printf("Rivi %d, alkio %d: ", i + 1, j + 1);
            scanf("%d", &aMatriisi[i][j]);
        }
    }

    // Transpoosi:
    for (int k = 0; k < RIVI; k++)
    {
        for (int m = 0; m < SARAKE; m++)
        {
            aTransMatriisi[m][k] = aMatriisi[k][m];
        }
    }

    tulostaMatriisi(aTiedostonimi, aMatriisi, "Lähtömatriisi: ");
    tulostaMatriisi(aTiedostonimi, aTransMatriisi, "Lähtömatriisin transpoosi: ");
    printf("\nTiedosto '%s' kirjoitettu.\n", aTiedostonimi);

    printf("Kiitos ohjelman käytöstä.\n");
    return 0;
}

void kysyNimi(char *pTiedostonimi)
{
    printf("Anna kirjoitettavan tiedoston nimi: ");
    scanf("%s", pTiedostonimi);
    return;
}

void tulostaMatriisi(char *pTiedostonimi, int aMatriisi[RIVI][SARAKE], char *pKehote)
{
    FILE *Tiedosto;

    if ((Tiedosto = fopen(pTiedostonimi, "a")) == NULL)
    {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }

    // Kirjoitus (lisäys) tiedostoon:
    fprintf(Tiedosto, "%s", pKehote);
    for (int i = 0; i < RIVI; i++)
    {
        fputs("\n", Tiedosto);
        for (int j = 0; j < SARAKE; j++)
        {
            fprintf(Tiedosto, "%4d ", aMatriisi[i][j]);
        }
    }
    fputs("\n\n", Tiedosto);
    fclose(Tiedosto);

    // Tulostus komentoriville:
    printf("\n%s\n", pKehote);
    for (int k = 0; k < RIVI; k++)
    {
        for (int m = 0; m < SARAKE; m++)
        {
            printf("%4d ", aMatriisi[k][m]);
        }
        printf("\n");
    }
    return;
}

// End of File
