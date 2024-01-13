/*************************************************************************/
/* CT60A2500 C-ohjelmoinnin perusteet
* Tekijä: Teemu Hiltunen
* Opiskelijanumero: 000393597
* Päivämäärä: 2.3.2023
* Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
* lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:

* Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
* tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
* vaikuttaneet siihen yllä mainituilla tavoilla.
*/
/*************************************************************************/
/* Tehtävä Harjoitustyö perustaso, tiedoston nimi HTPerus.c */

// Omat kirjastot:
#include "HTPerusKirjasto.h"

// Mains:
int main(void)
{
    int iValinta;
    char aTiedostonimi[TIEDOSTOPITUUS];

    RIVITIEDOT *pAlku = NULL;
    SANALUOKKA sanaluokitus[SANALUOKKIA];
    SANALUOKKA *ptrSanaluokitus = sanaluokitus;
    TILASTO tilasto;
    TILASTO *ptrTilasto = &tilasto;
    // Alustetaan tilasto -tietueen alkioMaara 0:lla jolloin tätä voidaan käyttää
    //  tarkastelussa onko tietoja analysoitu:
    tilasto.alkioMaara = 0;

    do
    {
        iValinta = valikko();
        if (iValinta == 1)
        {
            // Tyhjennetään edellisen analyysin tiedot linkitetystä listasta:
            if (pAlku != NULL)
            {
                pAlku = muistiVapaus(pAlku);
            }

            kysyTiedosto(aTiedostonimi);
            pAlku = lueTiedosto(aTiedostonimi, pAlku);
        }

        else if (iValinta == 2)
        {
            if (pAlku == NULL)
            {
                printf("Ei analysoitavaa, lue tiedosto ennen analyysiä.\n");
            }
            else
            {
                ptrTilasto = analysoiTilasto(pAlku, ptrTilasto);
                ptrSanaluokitus = analysoiSanaluokat(pAlku, ptrSanaluokitus);
            }
        }
        else if (iValinta == 3)
        {
            if (tilasto.alkioMaara == 0)
            {
                printf("Ei kirjoitettavia tietoja, analysoi tiedot ennen tallennusta.\n");
            }
            else
            {
                kysyTiedosto(aTiedostonimi);
                tiedostoOperaatiot(aTiedostonimi, ptrTilasto, ptrSanaluokitus);
            }
            /*// Alustetaan analyysin kirjoittamisen jälkeen tarkastelu,
                //  jolloin vanhoja tietoja ei kirjoiteta uuden datan lukemisen jälkeen
                //  mikäli käyttäjä ei analysoikkaan tietoja lukemisen jälkeen.
                tilasto.alkioMaara = 0;
            */
        }
        else if (iValinta == 0)
        {
            printf("Lopetetaan.\n");
        }
        else
        {
            printf("Tuntematon valinta, yritä uudestaan.\n");
        }
        printf("\n");
    } while (iValinta != 0);

    // Muistin vapautus:
    pAlku = muistiVapaus(pAlku);

    printf("Kiitos ohjelman käytöstä.\n");
    return (0);
}

// End of File