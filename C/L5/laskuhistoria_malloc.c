/**
 * Teemu Hiltunen; 000000000; 15.02.2023; L5T3.c
 *
 * Ohjelman tarkoitus on harjoittaa tietueen ja mallocin käyttöä laskuhistorian tallentamisessa
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

void muistiVaraus(LASKU **plaskut);
void kysyTiedostonimi(char **pTiedostonimi);
void valikko(int *pValinta);
LASKU lisaaLuku(int iKokonaisluku);
void kirjoitaHistoria(char *pTiedostonimi, int iLaskut, LASKU laskut[]);
void tulostaTiedot(char *pTiedostonimi);

int main(int argc, char *argv[])
{
    if (argc > 2)
    {
        printf("Annoit liikaa parametreja.\n");
        exit(0);
    }
    else if (argc < 2)
    {
        printf("Et antanut tarpeeksi parametreja.\n");
        exit(0);
    }

    int iValinta, iKokonaisluku = atoi(argv[1]), iLaskut = 0;
    char *pTiedostonimi = NULL;

    LASKU *plaskut;
    muistiVaraus(&plaskut);

    printf("Annoit luvun %d.\n", iKokonaisluku);

    do
    {
        valikko(&iValinta);
        if (iValinta == 1)
        {
            kysyTiedostonimi(&pTiedostonimi);
        }
        else if (iValinta == 2)
        {
            plaskut[iLaskut] = lisaaLuku(iKokonaisluku);
            iKokonaisluku = plaskut[iLaskut].iSumma;
            iLaskut++;
        }
        else if (iValinta == 3)
        {
            if (iLaskut == 0)
            {
                printf("\nEi kirjoitettavia tietoja.\n");
            }
            else if (pTiedostonimi == NULL)
            {
                printf("\nEi tiedoston nimeä, anna kirjoitettavan tiedoston nimi ensin.\n");
            }
            else
            {
                kirjoitaHistoria(pTiedostonimi, iLaskut, plaskut);
            }
        }
        else if (iValinta == 4)
        {

            if (pTiedostonimi == NULL)
            {
                printf("\nEi tiedoston nimeä, anna luettavan tiedoston nimi ensin.\n");
            }
            else
            {
                tulostaTiedot(pTiedostonimi);
            }
        }
        else if (iValinta == 0)
        {
            /**
             * Asetetaan pTiedostonimen osoittimen arvo NULL:iksi,
             *  jolloin ohjelman suorituksen jälkeen muistiin ei jää tietoa.
             * Luonnollisesti palautetaan lopetuksen yhteydessä muistipaikka.
             */
            free(pTiedostonimi);
            free(plaskut);
            pTiedostonimi = NULL;
            plaskut = NULL;
            printf("\nMuisti vapautettu.\n");
            printf("Lopetetaan.\n");
        }
        else
        {
            printf("\nTuntematon valinta, yritä uudestaan.\n");
        }
        puts("");
    } while (iValinta != 0);

    printf("Kiitos ohjelman käytöstä.\n");

    return (0);
}

/**
 * Aliohjelmassa varataan tiedostonimen merkkijonolle ennalta määrätty koko dynaamisesti.
 * Eli esimakua ensiviikkoa varten tämän aliohjelman toimintaperiaate.
 */

void muistiVaraus(LASKU **plaskut)
{
    if ((*plaskut = (LASKU *)malloc(sizeof(LASKU) * TAULUKKO)) == NULL)
    {
        perror("Muistinvaraus epäonnistui");
        free(*plaskut);
        exit(0);
    }
    return;
}

void kysyTiedostonimi(char **pTiedostonimi)
{
    if ((*pTiedostonimi = (char *)malloc(sizeof(char) * TIEDOSTOPITUUS)) == NULL)
    {
        perror("Muistinvaraus epäonnistui");
        free(*pTiedostonimi);
        exit(0);
    }
    printf("\nAnna kirjoitettavan tiedoston nimi: ");
    scanf("%s", *pTiedostonimi);
    return;
}

/**
 * Valikko aliohjelma jossa suoritetaan myös käyttäjän antaman virheellisen syötteen
 * virheenkäsittely (eli käytännössä hallitusti kaadetaan ohjelma).
 */

void valikko(int *pValinta)
{
    printf("Valitse haluamasi toiminto:\n");
    printf("1) Anna tiedoston nimi\n");
    printf("2) Lisää lukuun\n");
    printf("3) Kirjoita historia tiedostoon\n");
    printf("4) Lue historia tiedostosta\n");
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

    for (int j = 0; j < iLaskut; j++)
    {
        printf("\n%d+%d=%d", laskut[j].iLuku, laskut[j].iLuku1, laskut[j].iSumma);
    }
    puts("");
    if ((Tiedosto = fopen(pTiedostonimi, "a")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        free(pTiedostonimi);
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
 */

void tulostaTiedot(char *pTiedostonimi)
{
    int ch;
    FILE *Tiedosto;

    if ((Tiedosto = fopen(pTiedostonimi, "r")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        free(pTiedostonimi);
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
