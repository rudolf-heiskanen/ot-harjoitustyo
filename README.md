# SyntsaSyntikka

Tämä ohjelma on softasyntetisaattori, siis äänisynteesiä hyödyntävä soitin joka on toteutettu ohjelmallisesti. Syntetisaattoria voi soittaa tietokoneen näppäimistöllä, ja syntetisaattorin ääntä voi muokata käyttöliittymän parametreilla. 

Koska Pythonille ei ole laadittu erityisen vakiintuneita tai helppokäyttöisiä audiokirjastoja reaaliaikaiseen audioprosessointiin ja koska kokemukseni audio-ohjelmoinnista ei ole suurta, joillakin käynnistyskerroilla ääni pätkii enemmän kuin toisilla. Jos pätkintä on vakavaa, ohjelman uudelleenkäynnistäminen usein auttaa.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Tyoaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikaaviot](./dokumentaatio/arkkitehtuuri.md)

## Ensitoimenpiteet

Ohjelman voi ladata [github-releasesta](https://github.com/rudolf-heiskanen/rudolf-ohjelmistotekniikka/releases/tag/viikko5).
.
Ohjelman käyttämiseksi tulee ensin asentaa riippuvuudet komennolla
```bash
poetry install
```
Komento tulee suorittaa juurihakemistossa.

## Komentorivikäskyt

### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla
```bash
poetry run invoke start
```
### Ohjelman testaus ja testikattavuus
Ohjelmalle kirjoitetut testit voi suorittaa komennolla 
```bash 
poetry run invoke test
```
ja html-testikattavuusraportin voi luoda komennolla 
```bash
poetry run invoke coverage-report
```

Näin luotu testikattavuusraportti ilmestyy kansioon "htmlcov".

### Koodin laadun tarkistaminen
Ohjelman koodin laatutarkistuksen voi suorittaa komennolla
```bash
poetry run invoke lint
```
