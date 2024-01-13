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
/* Tehtävä Harjoitustyö perustaso, tiedoston nimi HTPerusKirjasto.h */


#ifndef HTPERUSKIRJASTO_H
#define HTPERUSKIRJASTO_H


// C kirjastot:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Vakiot:
#define TIEDOSTOPITUUS 30       // Luettavan ja kirjoitettavan tiedostonimien maksimipituus (29)
#define RIVIPITUUS 100          // lueTiedosto -funktion luettujen rivien maksimipituus (99)
#define SANAPITUUS 50           // tiedostosta luettujen yksittäisten sanojen maksimipituus (49)
#define SANALUOKKIA 10          // sanaluokkien määrä, käytetään SANALUOKKA tietuelistan määrittelyssä
#define EROTIN ";"              // luettavan tiedoston rivien erotinmerkki, normaalisti ";"


// Tietueet:

//  Tiedoston rivit luetaan tähän linkitetyn listan periaatteella
typedef struct rivitiedot {
    char sana[SANAPITUUS];
    int luokkaSana;
    struct rivitiedot *pSeuraava;
} RIVITIEDOT;

//  Datasta luotu tilastoanalyysi tallennetaan tähän
typedef struct tilasto {
    int alkioMaara;
    float sanaPituusKA;
    char aLyhyinSana[SANAPITUUS];
    char aPisinSana[SANAPITUUS];
    char aAakkosissaEka[SANAPITUUS];
    char aAakkosissaVika[SANAPITUUS];
} TILASTO;

//  Datasta lasketut sanat luokittain tallennetaan tämän tietueen taulukkoon
typedef struct sanaluokka {
    int luokkaNumero;
    int sanojenMaara;
} SANALUOKKA;



// Funktioiden esittelyt:
int valikko();
void kysyTiedosto(char *pTiedostonimi);

RIVITIEDOT *varaaMuisti(RIVITIEDOT *pVaraus);

RIVITIEDOT *lueTiedosto(char *pTiedostonimi, RIVITIEDOT *pAlku);

TILASTO *analysoiTilasto(RIVITIEDOT *pAlku, TILASTO *pTilasto);
SANALUOKKA *analysoiSanaluokat(RIVITIEDOT *pAlku, SANALUOKKA *pSanaluokitus);

void tiedostoOperaatiot(char *pTiedostonimi, TILASTO *pTilasto, SANALUOKKA *pSanaluokitus);
void kirjoitaTietovirtaan(FILE *Tiedosto, TILASTO *pTilasto, SANALUOKKA *pSanaluokitus);

RIVITIEDOT *muistiVapaus(RIVITIEDOT *pVapaus);



#endif // HTPERUSKIRJASTO_H

// End of File