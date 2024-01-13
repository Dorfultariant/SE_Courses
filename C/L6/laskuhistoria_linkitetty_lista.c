/**
 * Teemu Hiltunen; 000000000; 15.02.2023; L5T3.c
 *
 * Ohjelman ideana on harjoittaa linkitetyn listan käyttöä erilaisissa tehtävissä.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TIEDOSTOPITUUS 30 // Määritellään suurin sallittu merkkimäärä (-1) tiedostonimelle
#define SUMMA "+"
#define YHTASUURUUS "="

typedef struct lasku
{
    int iLuku;
    int iLuku1;
    int iSumma;
    struct lasku *pSeuraava;
} LASKU;

void muistiVaraus(LASKU **plaskut);
void kysyTiedostonimi(char **pTiedostonimi, char *pKehote);
void valikko(int *pValinta);
LASKU *lisaaLuku(LASKU *pAlku, LASKU *pLoppu, int iKokonaisluku);
void kirjoitaHistoria(char *pTiedostonimi, LASKU *pAlku);
void tulostaTiedot(LASKU *pAlku, LASKU *pLoppu, char *pTiedostonimi);
void muistiVapaus(LASKU *pAlku);

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

    int iValinta, iKokonaisluku = atoi(argv[1]);
    char *pTiedostonimi = NULL;

    LASKU *pAlku = NULL, *pLoppu = NULL;

    printf("Annoit luvun %d.\n", iKokonaisluku);

    do
    {
        valikko(&iValinta);
        if (iValinta == 1)
        {
            pAlku = lisaaLuku(pAlku, pLoppu, iKokonaisluku);

            // iKokonaisluku = pLoppu->iSumma;
            printf("%d\n", iKokonaisluku);
            printf("Onnistui 1.\n");
        }
        else if (iValinta == 2)
        {
            if (pAlku == NULL)
            {
                printf("\nEi kirjoitettavia tietoja.\n");
            }
            else
            {
                kysyTiedostonimi(&pTiedostonimi, "kirjoitettavan");
                kirjoitaHistoria(pTiedostonimi, pAlku);
                free(pTiedostonimi);
                pTiedostonimi = NULL;
            }
        }
        else if (iValinta == 3)
        {
            kysyTiedostonimi(&pTiedostonimi, "luettavan");
            tulostaTiedot(pAlku, pLoppu, pTiedostonimi);
            free(pTiedostonimi);
            pTiedostonimi = NULL;
        }
        else if (iValinta == 0)
        {
            free(pTiedostonimi);
            puts("");
            muistiVapaus(pAlku);
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

void muistiVaraus(LASKU **pUusi)
{
    if ((*pUusi = (LASKU *)malloc(sizeof(LASKU))) == NULL)
    {
        perror("Muistinvaraus epäonnistui, lopetetaan");
        exit(0);
    }
    return;
}

void kysyTiedostonimi(char **pTiedostonimi, char *pKehote)
{
    if ((*pTiedostonimi = (char *)malloc(sizeof(char) * TIEDOSTOPITUUS)) == NULL)
    {
        perror("Muistinvaraus epäonnistui");
        free(*pTiedostonimi);
        exit(0);
    }
    printf("\nAnna %s tiedoston nimi: ", pKehote);
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
    printf("1) Lisää lukuun\n");
    printf("2) Kirjoita historia tiedostoon\n");
    printf("3) Lue historia tiedostosta\n");
    printf("0) Lopeta\n");
    printf("Anna valintasi: ");
    if ((scanf("%d", pValinta)) != 1)
    {
        printf("Virheellinen valinta, lopetetaan.\n");
        pValinta = 0;
    }
    return;
}

/**
 * Aliohjelmassa suoritetaan laskentaa ja laskun tekijöiden tallennus linkitettyyn listaan
 */

LASKU *lisaaLuku(LASKU *pAlku, LASKU *pLoppu, int iKokonaisluku)
{
    LASKU *pUusi;

    muistiVaraus(&pUusi);

    printf("\nAnna lukuun lisättävä kokonaisluku: ");
    scanf("%d", &pUusi->iLuku1);

    pUusi->iLuku = iKokonaisluku;
    pUusi->iSumma = pUusi->iLuku + pUusi->iLuku1;
    pUusi->pSeuraava = NULL;

    if (pAlku == NULL)
    { // Mikäli linkitetty lista ei sisällä vielä mitään
        pAlku = pUusi;
        pLoppu = pUusi;
    }
    else
    { // Lisätään uusi alkio linkitetyn listan loppuun
        pLoppu->pSeuraava = pUusi;
        pLoppu = pUusi;
    }

    printf("%d%s%d%s%d\n", pLoppu->iLuku, SUMMA, pLoppu->iLuku1, YHTASUURUUS, pLoppu->iSumma);

    return (pLoppu); // ->iSumma
}

/**
 * Laskujen kirjoitus (lisäys, a = append) tiedostoon, iLaskut sisältää käytännössä tietuelistan koon ja sitä tulee päivittää jokaisen
 * lisätyn tietueen yhteydessä. Tämä tapahtuu pääohjelmassa.
 */

void kirjoitaHistoria(char *pTiedostonimi, LASKU *pAlku)
{
    FILE *Tiedosto;
    LASKU *ptr;

    // Linkitetyn listan tulostus:
    ptr = pAlku;
    while (ptr != NULL)
    {
        printf("%d%s%d%s%d\n", ptr->iLuku, SUMMA, ptr->iLuku1, YHTASUURUUS, ptr->iSumma);
        ptr = ptr->pSeuraava;
    }
    puts("");

    if ((Tiedosto = fopen(pTiedostonimi, "a")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        free(pTiedostonimi);
        muistiVapaus(pAlku);
        exit(1);
    }
    else
    {
        ptr = pAlku;
        while (ptr != NULL)
        {
            fprintf(Tiedosto, "%d%s%d%s%d\n", ptr->iLuku, SUMMA, ptr->iLuku1, YHTASUURUUS, ptr->iSumma);
            ptr = ptr->pSeuraava;
        }
        printf("\nTiedosto '%s' kirjoitettu.\n", pTiedostonimi);
    }

    fclose(Tiedosto);
    return;
}

/**
 * Jokainen merkki tulostetaan tiedostosta, eli myös vanhat tiedot tulostuvat ruudulle.
 * Hyödynnetään fgetc, koska tällöin ei tarvita erillistä aRivi[] merkkijonoa jolle varata muistia.
 *      Tämä ei kuitenkaan tarkoita, että ohjelma olisi mitenkään muistin säästöä ajatellen rakennettu.
 */

void tulostaTiedot(LASKU *pAlku, LASKU *pLoppu, char *pTiedostonimi)
{
    int ch;
    char aRivi[TIEDOSTOPITUUS];
    LASKU *pUusi; // *ptr

    FILE *Tiedosto;

    if ((Tiedosto = fopen(pTiedostonimi, "r")) == NULL)
    {
        perror("\nTiedoston avaaminen epäonnistui, lopetetaan");
        free(pTiedostonimi);
        muistiVapaus(pAlku);
        exit(1);
    }
    else
    {

        while ((fgets(aRivi, TIEDOSTOPITUUS, Tiedosto)) != NULL)
        {
            muistiVaraus(&pUusi);
            pUusi->iLuku = atoi(strtok(aRivi, SUMMA));
            pUusi->iLuku1 = atoi(strtok(NULL, SUMMA));
            pUusi->iSumma = atoi(strtok(NULL, YHTASUURUUS));
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
        }

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

/**
 * Funktio vapauttaa linkitetyn listan viemän tilan.
 */

void muistiVapaus(LASKU *pAlku)
{
    LASKU *ptr;
    ptr = pAlku;
    while (ptr != NULL)
    {
        pAlku = ptr->pSeuraava;
        free(ptr);
        ptr = pAlku;
    }
    printf("Muisti vapautettu.\n");
    return;
}

// End of File
