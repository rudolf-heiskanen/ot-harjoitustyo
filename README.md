# SyntsaSyntikka

Tämä ohjelma on softasyntetisaattori, siis äänisynteesiä hyödyntävä soitin joka on toteutettu ohjelmallisesti. Syntetisaattoria voi soittaa tietokoneen näppäimistöllä, ja syntetisaattorin ääntä voi muokata käyttöliittymän parametreilla. 

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Tyoaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Ensitoimenpiteet

Ohjelman käyttämiseksi tulee ensin asentaa riippuvuudet komennolla
```bash
poetry install
```

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
Ohjelman koodin laatutarkitsuksen voi suorittaa komennolla
```bash
poetry run invoke lint
```
