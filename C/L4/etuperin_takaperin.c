/**
 * Teemu Hiltunen; 000000000; 08.02.2023; L4T5.c
 *
 *
 *
 *
 * Ohjelma tulostaa parametrina annetun merkkijonon valinnan mukaan etuperin tai takaperin
 *  ohjelman tarkoitus on harjoittaa rekursiota
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int valikko();
char etuperin(char *aMerkkijono, int i);
char takaperin(char *aMerkkijono, int j);

int main(int argc, char *argv[])
{
    int iValinta, i = 0;

    if (argc < 2)
    {
        printf("Et antanut tarpeeksi parametreja.\n");
        printf("Esimerkki: ./<program> Esimerkkiteksti\n");
        exit(0);
    }
    else if (argc > 2)
    {
        printf("Annoit liikaa parametreja.\n");
        printf("Esimerkki: ./<program> Esimerkkiteksti\n");
        exit(0);
    }

    do
    {
        iValinta = valikko();

        switch (iValinta)
        {
        case 1:
            etuperin(argv[1], i);
            break;

        case 2:
            takaperin(argv[1], strlen(argv[1]));
            break;

        case 0:
            printf("Lopetetaan.\n");
            break;

        default:
            printf("Tuntematon valinta, yritä uudestaan.\n");
            break;
        }
        printf("\n");
    } while (iValinta != 0);

    printf("Kiitos ohjelman käytöstä.\n");

    return 0;
}

int valikko()
{
    int iValinta;
    printf("Valitse haluamasi toiminto:\n");
    printf("1) Tulosta merkkijono\n");
    printf("2) Tulosta merkkijono takaperin\n");
    printf("0) Lopeta\n");
    printf("Anna valintasi: ");
    if ((scanf("%d", &iValinta)) == 1)
    {
        return (iValinta);
    }
    else
    {
        perror("Virheellinen valinta, lopetetaan\n");
        exit(0);
    }
}

char etuperin(char *aMerkkijono, int i)
{
    // Kun i:n arvo vastaa merkkijonon pituutta, eli merkkijono on käyty läpi, lopetetaan rekursion suoritus:
    if (i == strlen(aMerkkijono))
    {
        return *aMerkkijono;
    }

    printf("%c\n", aMerkkijono[i]);
    return etuperin(aMerkkijono, ++i);
}

char takaperin(char *aMerkkijono, int j)
{
    // Kun j:n arvo ollaan saatu nollaan niin lopetetaan rekursion suoritus:
    if (j < 1)
    {
        return *aMerkkijono;
    }

    printf("%c\n", aMerkkijono[--j]);
    return takaperin(aMerkkijono, j);
}

// End of File
