/* Teemu Hiltunen; 000000000; 07.02.2023; L4T2.c
 *
 *
 * Ohjelman ajatus on lukea tiedosto ja sitten tulostaa se käyttäjälle.
 *    ohjelman tarkoitus on harjoittaa tiedoston lukua
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX 50

int main(int argc, char *argv[])
{
    char aRivi[MAX];
    int iLaskuri = 0;

    if (argc < 3)
    {
        printf("Et antanut tarpeeksi parametreja.\n");
    }
    else if (argc > 3)
    {
        printf("Annoit liikaa parametreja.\n");
    }

    FILE *tiedosto;
    if ((tiedosto = fopen(argv[1], "r")) == NULL)
    {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    for (int i = 0; i < atoi(argv[2]); i++)
    {
        if ((fgets(aRivi, MAX, tiedosto)) == NULL)
        {
            printf("\nTiedostossa ei ole enempää rivejä luettavaksi.");
            break;
        }
        else
        {
            printf("%s", aRivi);
            iLaskuri++;
        }
    }

    fclose(tiedosto);

    printf("\nTiedostosta '%s' luettu %d riviä.\n", argv[1], iLaskuri);
    // printf("Kiitos ohjelman käytöstä.\n");

    return (0);
}

// End of File
