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
/* Tehtävä Harjoitustyö perustaso, tiedoston nimi HTPerusKirjasto.c */


// Omat kirjastot:
#include "HTPerusKirjasto.h"


// Funktio tulostaa valikon:
int valikko() {
    int iValinta;
    printf("Valitse haluamasi toiminto:\n");
    printf("1) Lue tiedosto\n");
    printf("2) Analysoi tiedot\n");
    printf("3) Kirjoita tulokset\n");
    printf("0) Lopeta\n");
    printf("Anna valintasi: ");
    scanf("%d",&iValinta);
    getchar();
    return(iValinta);
}

// Funktiolla kysytään käyttäjältä tiedostonimi:
void kysyTiedosto(char *pTiedostonimi) {
    printf("Anna tiedoston nimi: ");
    scanf("%s",pTiedostonimi);
    return;
}

// Funktio varaa dynaamisesti muistia linkitetylle listalle:
RIVITIEDOT *varaaMuisti(RIVITIEDOT *pVaraus) {
    if((pVaraus = (RIVITIEDOT *)malloc(sizeof(RIVITIEDOT))) == NULL) {
        perror("Muistin varaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    return pVaraus;
}

// Funktio lukee tiedostosta rivit ja jakaa riveiltä löytyneet sanat 
//  ja niiden luokat linkitettyyn listaan tietueisiin:
RIVITIEDOT *lueTiedosto(char *pTiedostonimi, RIVITIEDOT *pAlku) {
    RIVITIEDOT *pLoppu = NULL;
    char aRivi[RIVIPITUUS];
    char *pSarake, *pSarake1;
    FILE *Tiedosto;

    if((Tiedosto = fopen(pTiedostonimi, "r")) == NULL) {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    // Luetaan otsikkorivi:
    fgets(aRivi, RIVIPITUUS, Tiedosto);

    // Luetaan dataa:
    while(fgets(aRivi, RIVIPITUUS, Tiedosto) != NULL) {
        // Luodaan osoitin uuteen tietueeseen ja varataan sille muisti:
        RIVITIEDOT *pUusi;
        pUusi = varaaMuisti(pUusi);

        // Pilkotaan rivi sarakkeisiin vakio EROTIN :n mukaan:
        if((pSarake = strtok(aRivi, EROTIN)) == NULL) {
            printf("Merkkijonon '%s' pilkkominen epäonnistui.\n", aRivi);
            exit(0);
        }
        if((pSarake1 = strtok(NULL, EROTIN)) == NULL) {
            printf("Merkkijonon '%s' pilkkominen epäonnistui.\n", aRivi);
            exit(0);
        }
 
        // Asetetaan tietueen jäsenmuuttujat sarakkeen tiedoilla:
        strcpy(pUusi->sana, pSarake);
        pUusi->luokkaSana = atoi(pSarake1);
        pUusi->pSeuraava = NULL;

        // Lisätään tietue linkitettyyn listaan:
        if(pAlku == NULL) {
            pAlku = pUusi;
            pLoppu = pUusi;
        } else {
            pLoppu->pSeuraava = pUusi;
            pLoppu = pUusi;
        }
    }

    printf("Tiedosto '%s' luettu.\n",pTiedostonimi);
    fclose(Tiedosto);
    return(pAlku);
}

// Funktio analysoi tiedostosta luetusta datasta tunnuksia:
TILASTO *analysoiTilasto(RIVITIEDOT *pAlku, TILASTO *pTilasto) {
    RIVITIEDOT *ptr;
    int iAakkosVertaus;
    float fSanaPituusSumma = 0;
    

    // Tilasto -tietueen jäsenmuuttujien alustus:
    ptr = pAlku;
    strcpy(pTilasto->aAakkosissaEka, ptr->sana);
    strcpy(pTilasto->aAakkosissaVika, ptr->sana);
    strcpy(pTilasto->aLyhyinSana, ptr->sana);
    strcpy(pTilasto->aPisinSana, ptr->sana);
    pTilasto->alkioMaara = 0;
    pTilasto->sanaPituusKA = 0.0;


    // Analysointiosuus:
    while (ptr != NULL) {
        // Aakkosten ensimmäinen ja viimeinen sana -vertaus:
        iAakkosVertaus = strcmp(pTilasto->aAakkosissaEka, ptr->sana);
        if(iAakkosVertaus > 0) {
            strcpy(pTilasto->aAakkosissaEka, ptr->sana);
        }
        iAakkosVertaus = strcmp(pTilasto->aAakkosissaVika, ptr->sana);
        if(iAakkosVertaus < 0) {
            strcpy(pTilasto->aAakkosissaVika, ptr->sana);
        }

        // Lyhimmän sanan vertaus:
        if((strlen(pTilasto->aLyhyinSana)) > (strlen(ptr->sana))) {
            strcpy(pTilasto->aLyhyinSana, ptr->sana);
        }
        // Pisimmän sanan vertaus:
        if((strlen(pTilasto->aPisinSana)) < (strlen(ptr->sana))) {
            strcpy(pTilasto->aPisinSana, ptr->sana);
        }

        // Lasketaan summa kaikkien sanojen pituuksista:
        fSanaPituusSumma += strlen(ptr->sana);

        // Analysoitujen sanojen lukumäärä:
        pTilasto->alkioMaara += 1;

        ptr = ptr->pSeuraava;
    }

    // Sanojen pituuden keskiarvon laskeminen:
    if(pTilasto->alkioMaara != 0) {
        pTilasto->sanaPituusKA = fSanaPituusSumma / pTilasto->alkioMaara;
    }

    printf("Analysoitu %d sanaa.\n",pTilasto->alkioMaara);
    
    return pTilasto;
}

// Funktio laskee eri sanaluokkiin kuuluvien sanojen määrät:
SANALUOKKA *analysoiSanaluokat(RIVITIEDOT *pAlku, SANALUOKKA *pSanaluokitus) {
    RIVITIEDOT *ptr;
    int i = 0;

    // Sanaluokka-tietuelistan alustus:
    for (i = 0; i < SANALUOKKIA; i++) {
        SANALUOKKA uusiSanaluokka;
        uusiSanaluokka.luokkaNumero = i + 1;
        uusiSanaluokka.sanojenMaara = 0;
        pSanaluokitus[i] = uusiSanaluokka;
    }
    
    // Käydään linkitetty lista läpi ja analysoidaan sen sisältämä tieto sanaluokka tietuelistaan:
    ptr = pAlku;
    while(ptr != NULL) {
        pSanaluokitus[ptr->luokkaSana-1].luokkaNumero = ptr->luokkaSana;
        pSanaluokitus[ptr->luokkaSana-1].sanojenMaara += 1;

        ptr = ptr->pSeuraava;
    }

    printf("Sanaluokittaiset lukumäärät analysoitu.\n");
    return pSanaluokitus;
}

// Funktio käsittelee tiedoston avaamisen ja sulkemisen kirjoitettaessa:
void tiedostoOperaatiot(char *pTiedostonimi, TILASTO *pTilasto, SANALUOKKA *pSanaluokitus) {
    FILE *Tiedosto;

    // Tulostetaan päätteeseen:
    kirjoitaTietovirtaan(stdout, pTilasto, pSanaluokitus);

    // Kirjoitetaan tiedostoon:
    if((Tiedosto = fopen(pTiedostonimi, "w")) == NULL) {
        perror("Tiedoston avaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    kirjoitaTietovirtaan(Tiedosto, pTilasto, pSanaluokitus);

    fclose(Tiedosto);

    printf("Tiedosto '%s' kirjoitettu.\n", pTiedostonimi);
    return;
}

// Funktio kirjoittaa annettuun tietovirtaan (stdout / tiedosto):
void kirjoitaTietovirtaan(FILE *Tiedosto, TILASTO *pTilasto, SANALUOKKA *pSanaluokitus) {
    
    // Tulostus tietovirtaan:
    fprintf(Tiedosto, "Tilastotiedot %d sanasta:\n", pTilasto->alkioMaara);
    fprintf(Tiedosto, "Keskimääräinen sanan pituus on %.1f merkkiä.\n", pTilasto->sanaPituusKA);
    fprintf(Tiedosto, "Pisin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aPisinSana, strlen(pTilasto->aPisinSana));
    fprintf(Tiedosto, "Lyhyin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aLyhyinSana, strlen(pTilasto->aLyhyinSana));
    fprintf(Tiedosto, "Aakkosjärjestyksessä ensimmäinen sana on '%s'.\n", pTilasto->aAakkosissaEka);
    fprintf(Tiedosto, "Aakkosjärjestyksessä viimeinen sana on '%s'.\n", pTilasto->aAakkosissaVika);
    fputs("\n",Tiedosto);
    
    fprintf(Tiedosto, "Sanaluokka;Lkm\n");
    for(int i = 0; i < SANALUOKKIA; i++) {
        fprintf(Tiedosto, "Luokka %d;%d\n",pSanaluokitus[i].luokkaNumero,pSanaluokitus[i].sanojenMaara);
    }

    return;
}

// Funktio vapauttaa linkitetyn listan alkiot:
RIVITIEDOT *muistiVapaus(RIVITIEDOT *pVapaus) {
    RIVITIEDOT *ptr;
    ptr = pVapaus;
    while(ptr != NULL) {
        pVapaus = ptr->pSeuraava;
        free(ptr);
        ptr = pVapaus;
    }
    pVapaus = NULL;
    return pVapaus;
}



// End of File