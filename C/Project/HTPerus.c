/*************************************************************************/
/* CT60A2500 C-ohjelmoinnin perusteet
* Tekijä: Teemu Hiltunen
* Opiskelijanumero: 000393597
* Päivämäärä: 25.2.2023
* Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
* lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:

* Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
* tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
* vaikuttaneet siihen yllä mainituilla tavoilla.
*/
/*************************************************************************/
/* Tehtävä Harjoitustyö perustaso, tiedoston nimi HTPerus.c */

// Kirjastot:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Omat kirjastot:

// Vakiot:
#define TIEDOSTOPITUUS 30       // Luettavan ja kirjoitettavan tiedostonimien maksimipituus (29)
#define RIVIPITUUS 100          // lueTiedosto -funktion luettujen rivien maksimipituus (99)
#define SANAPITUUS 50           // tiedostosta luettujen yksittäisten sanojen maksimipituus (49)
#define SANALUOKKIA 10          // sanaluokkien määrä, käytetään SANALUOKKA tietuelistan määrittelyssä
#define EROTIN ";"              // luettavan tiedoston rivien erotinmerkki, normaalisti ";"


// Tietueet:
typedef struct rivitiedot { // Linkitetty lista muodostetaan tästä tietueesta
    char sana[SANAPITUUS];
    int luokkaSana;
    struct rivitiedot *pSeuraava;
} RIVITIEDOT;


typedef struct tilasto {
    int alkioMaara;
    float sanaPituusKA;
    char aLyhyinSana[SANAPITUUS];
    char aPisinSana[SANAPITUUS];
    char aAakkosissaEka[SANAPITUUS];
    char aAakkosissaVika[SANAPITUUS];
} TILASTO;


typedef struct sanaluokka {
    int luokkaNumero;
    int sanojenMaara;
} SANALUOKKA;


int valikko();
void kysyTiedosto();

RIVITIEDOT *varaaMuisti(RIVITIEDOT *pVaraus);

RIVITIEDOT *lueTiedosto(char *pTiedostonimi, RIVITIEDOT *pAlku);

TILASTO *analysoiTilasto(RIVITIEDOT *pAlku, TILASTO *pTilasto);
SANALUOKKA *analysoiSanaluokat(RIVITIEDOT *pAlku, SANALUOKKA sanaluokitus[]);

void tiedostoOperaatiot(char *pTiedostonimi, TILASTO *pTilasto, SANALUOKKA sanaluokitus[]);
void kirjoitaTiedostoon(FILE *Tiedosto, TILASTO *pTilasto, SANALUOKKA sanaluokitus[]);

RIVITIEDOT *muistiVapaus(RIVITIEDOT *pVapaus);



// Mains:
int main(void) {
    int iValinta;
    char aTiedostonimi[TIEDOSTOPITUUS];

    RIVITIEDOT *pAlku = NULL;
    SANALUOKKA sanaluokitus[SANALUOKKIA];
    SANALUOKKA *ptrSanaluokitus = sanaluokitus;
    TILASTO tilasto;
    TILASTO *ptrTilasto = &tilasto;
    // Alustetaan 
    tilasto.alkioMaara = 0;
    
    do {
        iValinta = valikko();
        if (iValinta == 1) {
            // Tyhjennetään edellisen analyysin tiedot linkitetystä listasta:
            if(pAlku != NULL) {
                pAlku = muistiVapaus(pAlku);
            }

            kysyTiedosto(&aTiedostonimi);
            pAlku = lueTiedosto(aTiedostonimi, pAlku);
        }

        else if (iValinta == 2) {
            if(pAlku == NULL) {
                printf("Ei analysoitavaa, lue tiedosto ennen analyysia.\n");
            } else {
                ptrTilasto = analysoiTilasto(pAlku, ptrTilasto);
                ptrSanaluokitus = analysoiSanaluokat(pAlku, ptrSanaluokitus);
                
            }
        } 
        else if (iValinta == 3) {
            if(tilasto.alkioMaara == 0) {   // Ainakin toistaiseksi käytettävä tarkastusehto
                printf("Ei kirjoitettavia tietoja, analysoi tiedot ennen tallennusta.\n");
            } else {
                kysyTiedosto(&aTiedostonimi);
                tiedostoOperaatiot(aTiedostonimi, &tilasto, sanaluokitus);
            }
            
        }
        else if (iValinta == 0) {
            printf("Lopetetaan\n");
        }
        else {
            printf("Tuntematon valinta, yritä uudestaan.\n");
        }
        printf("\n");
    } while (iValinta != 0);


    // Muistin vapautus:
    pAlku = muistiVapaus(pAlku);
    
    printf("Kiitos ohjelman käytöstä.\n");
    return(0);
}

// TOIMII
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

// TOIMII
void kysyTiedosto(char *pTiedostonimi) {
    printf("Anna tiedoston nimi: ");
    scanf("%s",pTiedostonimi);
    return;
}

// TOIMII
RIVITIEDOT *varaaMuisti(RIVITIEDOT *pVaraus) {
    if((pVaraus = (RIVITIEDOT *)malloc(sizeof(RIVITIEDOT))) == NULL) {
        perror("Muistin varaaminen epäonnistui, lopetetaan");
        exit(0);
    }
    return pVaraus;
}

// TOIMII
RIVITIEDOT *lueTiedosto(char *pTiedostonimi, RIVITIEDOT *pAlku) {
    RIVITIEDOT *pLoppu = NULL;
    char aRivi[RIVIPITUUS];
    char *pSarake, *pSarake1;
    FILE *Tiedosto;

    if((Tiedosto = fopen(pTiedostonimi, "r")) == NULL) {
        perror("Tiedoston käsittelyssä virhe, lopetetaan");
        exit(0);
    }
    // Ohitetaan otsikkorivi:
    fgets(aRivi, RIVIPITUUS, Tiedosto);

    // Luetaan dataa:
    while(fgets(aRivi, RIVIPITUUS, Tiedosto) != NULL) {
        // Luodaan osoitin uuteen tietueeseen ja varataan sille muisti:
        RIVITIEDOT *pUusi;
        pUusi = varaaMuisti(pUusi);

        // Pilkotaan rivi sarakkeisiin vakio EROTIN :n mukaan:
        if((pSarake = strtok(aRivi, EROTIN)) == NULL) {
            printf("strtok virhe\n");
        }
        if((pSarake1 = strtok(NULL, EROTIN)) == NULL) {
            printf("strtok virhe\n");
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

// TOIMII
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
        if(iAakkosVertaus == 1) {
            strcpy(pTilasto->aAakkosissaEka, ptr->sana);
        }
        iAakkosVertaus = strcmp(pTilasto->aAakkosissaVika, ptr->sana);
        if(iAakkosVertaus == -1) {
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

        // Sanojen KA laskua varten:
        fSanaPituusSumma += strlen(ptr->sana);

        // Analysoitujen sanojen lukumäärä:
        pTilasto->alkioMaara += 1;

        ptr = ptr->pSeuraava;
    }
    // Sanojen pituuden keskiarvon laskeminen:
    pTilasto->sanaPituusKA = fSanaPituusSumma / pTilasto->alkioMaara;
    
    printf("Analysoitu %d sanaa.\n",pTilasto->alkioMaara);
    
    return pTilasto;
}

// TOIMII
SANALUOKKA *analysoiSanaluokat(RIVITIEDOT *pAlku, SANALUOKKA sanaluokitus[]) {
    RIVITIEDOT *ptr;
    //SANALUOKKA *ptrSanaluokka;
    int i = 0;

    // Sanaluokka-tietuelistan alustus:
    for (i = 0; i < SANALUOKKIA; i++) {
        SANALUOKKA uusiSanaluokka;
        uusiSanaluokka.luokkaNumero = i + 1;
        uusiSanaluokka.sanojenMaara = 0;
        sanaluokitus[i] = uusiSanaluokka;
    }
    
    // Käydään linkitetty lista läpi ja analysoidaan sen sisältämä tieto sanaluokka tietuelistaan:
    ptr = pAlku;
    while(ptr != NULL) {
        sanaluokitus[ptr->luokkaSana-1].luokkaNumero = ptr->luokkaSana;
        sanaluokitus[ptr->luokkaSana-1].sanojenMaara += 1;

        ptr = ptr->pSeuraava;
    }

    printf("Sanaluokittaiset lukumäärät analysoitu.\n");
    return sanaluokitus;
}

// Toimii
void tiedostoOperaatiot(char *pTiedostonimi, TILASTO *pTilasto, SANALUOKKA sanaluokitus[]) {

    FILE *Tiedosto;

    if((Tiedosto = fopen(pTiedostonimi, "w")) == NULL) {
        perror("Tiedoston käsittelyssä virhe, lopetetaan");
        exit(0);
    }

    kirjoitaTiedostoon(Tiedosto, pTilasto, sanaluokitus);


    fclose(Tiedosto);

    printf("Tiedosto '%s' kirjoitettu.\n", pTiedostonimi);
    return;
}

// Toimii
void kirjoitaTiedostoon(FILE *Tiedosto, TILASTO *pTilasto, SANALUOKKA sanaluokitus[]) {
    
    // Tulostus päätteeseen:
    printf("Tilastotiedot %d sanasta:\n", pTilasto->alkioMaara);
    printf("Keskimääräinen sanan pituus on %.1f merkkiä.\n", pTilasto->sanaPituusKA);
    printf("Pisin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aPisinSana, strlen(pTilasto->aPisinSana));
    printf("Lyhyin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aLyhyinSana, strlen(pTilasto->aLyhyinSana));
    printf("Aakkosjärjestyksessä ensimmäinen sana on '%s'.\n", pTilasto->aAakkosissaEka);
    printf("Aakkosjärjestyksessä viimeinen sana on '%s'.\n", pTilasto->aAakkosissaVika);
    puts("");

    printf("Sanaluokka;Lkm\n");
    for(int i = 0; i < SANALUOKKIA; i++) {
        printf("Luokka %d;%d\n",sanaluokitus[i].luokkaNumero,sanaluokitus[i].sanojenMaara);
    }

    // Tulostus Tiedostoon:
    fprintf(Tiedosto, "Tilastotiedot %d sanasta:\n", pTilasto->alkioMaara);
    fprintf(Tiedosto, "Keskimääräinen sanan pituus on %.1f merkkiä.\n", pTilasto->sanaPituusKA);
    fprintf(Tiedosto, "Pisin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aPisinSana, strlen(pTilasto->aPisinSana));
    fprintf(Tiedosto, "Lyhyin sana '%s' on %ld merkkiä pitkä.\n", pTilasto->aLyhyinSana, strlen(pTilasto->aLyhyinSana));
    fprintf(Tiedosto, "Aakkosjärjestyksessä ensimmäinen sana on '%s'.\n", pTilasto->aAakkosissaEka);
    fprintf(Tiedosto, "Aakkosjärjestyksessä viimeinen sana on '%s'.\n", pTilasto->aAakkosissaVika);
    fputs("\n",Tiedosto);
    
    fprintf(Tiedosto, "Sanaluokka;Lkm\n");
    for(int i = 0; i < SANALUOKKIA; i++) {
        fprintf(Tiedosto, "Luokka %d;%d\n",sanaluokitus[i].luokkaNumero,sanaluokitus[i].sanojenMaara);
    }

    return;
}

// TOIMII, VAPAUTTAA KAIKEN LINKITETYSTÄ LISTASTA
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

/* End of File */