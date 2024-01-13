/**
 * Teemu Hiltunen; 000000000; 08.02.2023; L4T3.c
 */

#include <stdio.h>
#include <stdlib.h>

#define TIEDOSTOPITUUS 30 // Määritellään suurin sallittu merkkimäärä (-1) tiedostonimelle
#define TAULUKKO 30       // Tietuetaulukon maximi koko

typedef struct lasku
{
    int iLuku;
    int iLuku1;
    int iSumma;
} LASKU;

void kysyTiedostonimi(char *pTiedostonimi);
void valikko(int *pValinta);
LASKU lisaaLuku(int iKokonaisluku);
void kirjoitaHistoria(char *pTiedostonimi, int iLaskut, LASKU laskut[]);
void tulostaTiedot(char *pTiedostonimi);

int main()
{
    int iValinta, iKokonaisluku, iLaskut = 0;
    char aKirjoTiedostonimi[TIEDOSTOPITUUS];

    LASKU laskut[TAULUKKO];

    printf("Anna kokonaisluku: ");
    scanf("%d", &iKokonaisluku);
    kysyTiedostonimi(aKirjoTiedostonimi);

    do
    {
        valikko(&iValinta);

        if (iValinta == 1)
        {
            laskut[iLaskut] = lisaaLuku(iKokonaisluku);
            iKokonaisluku = laskut[iLaskut].iSumma;
            iLaskut++;
        }
        else if (iValinta == 2)
        {
            kirjoitaHistoria(aKirjoTiedostonimi, iLaskut, laskut);
        }
        else if (iValinta == 3)
        {
            tulostaTiedot(aKirjoTiedostonimi);
        }
        else if (iValinta == 0)
        {
            printf("\nLopetetaan.\n");
        }
        else
        {
            printf("\nTuntematon valinta, yritä uudestaan.\n");
        }
    } while (iValinta != 0);

    printf("\nKiitos ohjelman käytöstä.\n");
    return (0);
}

void kysyTiedostonimi(char *pTiedostonimi)
{
    printf("Anna kirjoitettavan tiedoston nimi: ");
    scanf("%s", pTiedostonimi);
    return;
}

/**
 * Valikko aliohjelma jossa suoritetaan myös käyttäjän antaman virheellisen syötteen
 * virheenkäsittely (eli käytännössä hallitusti kaadetaan ohjelma).
 */

void valikko(int *pValinta)
{
    printf("\nValitse haluamasi toiminto:\n");
    printf("1) Lisää lukuun\n");
    printf("2) Kirjoita historia tiedostoon\n");
    printf("3) Lue historia tiedostosta\n");
    printf("0) Lopeta\n");
    printf("Anna valintasi: ");
    if ((scanf("%d", pValinta)) != 1)
    {
        perror("Virheellinen valinta, lopetetaan");
        exit(0);
    }
    return;
}

/**
 * Aliohjelmassa suoritetaan laskentaa ja laskun tekijöiden tallennus tietueeseen,
 *  joka menee tietuelistaan pääohjelmassa.
 * Lisättävä luku kysytään joka kutsun yhteydessä ja luku johon lisätään päivitetään pääohjelmassa.
 */

LASKU lisaaLuku(int iKokonaisluku)
{
    LASKU lasku;

    printf("\nAnna lukuun lisättävä kokonaisluku: ");
    scanf("%d", &lasku.iLuku1);

    lasku.iLuku = iKokonaisluku;
    lasku.iSumma = lasku.iLuku + lasku.iLuku1;

    printf("%d+%d=%d\n", lasku.iLuku, lasku.iLuku1, lasku.iSumma);
    return (lasku);
}

/**
 * Laskujen kirjoitus (lisäys, a = append) tiedostoon, iLaskut sisältää käytännössä tietuelistan koon ja sitä tulee päivittää jokaisen
 * lisätyn tietueen yhteydessä. Tämä tapahtuu pääohjelmassa.
 */

void kirjoitaHistoria(char *pTiedostonimi, int iLaskut, LASKU laskut[])
{
    FILE *Tiedosto;

    if ((Tiedosto = fopen(pTiedostonimi, "a")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    else
    {
        for (int i = 0; i < iLaskut; i++)
        {
            fprintf(Tiedosto, "%d+%d=%d\n", laskut[i].iLuku, laskut[i].iLuku1, laskut[i].iSumma);
        }
        printf("\nTiedosto '%s' kirjoitettu.\n", pTiedostonimi);
    }

    fclose(Tiedosto);
    return;
}

/**
 * Jokainen merkki tulostetaan tiedostosta, eli myös vanhat tiedot tulostuvat ruudulle.
 * Hyödynnetään fgetc, koska tällöin ei tarvita erillistä aRivi[] merkkijonoa jolle varata muistia.
 *
 */

void tulostaTiedot(char *pTiedostonimi)
{
    int ch;
    FILE *Tiedosto;

    if ((Tiedosto = fopen(pTiedostonimi, "r")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    else
    {
        printf("\nTiedostossa oleva laskuhistoria:\n");
        while ((ch = fgetc(Tiedosto)) != EOF)
        {
            printf("%c", ch);
        }
        printf("Tiedosto '%s' luettu ja tulostettu.\n", pTiedostonimi);
    }

    fclose(Tiedosto);
    return;
}

// End of File
