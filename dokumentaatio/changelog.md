# Changelog

## Viikko 3
### Uusia ominaisuuksia:
- Käyttäjä näkee listan invoke -tehtävistä ja pystyy käyttämään niitä
- Käyttäjä pystyy ajamaan ohjelman, ja tietokoneen näppäimiä painamalla soittamaan sawtooth-aallon.
### Uusia osia ohjelman rakenteessa:
- Lisätty kaikki luokat, jotka ovat välttämättömiä tälle toiminnallisuudelle, eli 
	- Synthesizer, joka vastaa sovelluksen ison kuvan organisoinnista
	- Synthengine, joka vastaa inputtina saamiensa nuottien prosessoimisesta ääneksi
		- Voice, joka vastaa yhden tietyllä hetkellä soivan sävelen muuttamisesta audioksi
			- Oscillator, joka vastaa yhden Voicen äänen pohjana toimivien ääniaaltojen generoimisesta
	- Playbackdevice, joka vastaa synthenginen generoiman audion soittamisesta tietokoneen kaiuttimista
	- Ui, joka tällä hetkellä vain lukee PyGamen avulla näppäimistön syötettä soittamista varten

### Muita huomioita:
Windows-koneelta linux-koneelle siirtyessä huomasin, että alunperin käyttämäni audiokirjasto PyAudio ei toimi ilman riippuvuuksia, joten tällä hetkellä äänenlaatu on huono, ja asialle toivottavasti onnistutaan tekemään jotakin tulevaisuudessa.

## Viikko 4:
### Uusia ominaisuuksia:
- Käyttäjä pystyy soittamaan eri säveliä käyttäen tietokoneen näppäimistöä pianon koskettimien tavoin, terminaaliin tulostuvan ohjeen mukaan.

### Muita huomioita:
Nyt audio toimii linuxilla pygamen audio-ominaisuutta käyttäen. Ääni saattaa hieman pätkiä joillain laitteilla tai ohjelman käynnistyskerroilla. Tämän korjaaminen vaatisi kuitenkin luultavasti niin suurta optimointia, että tyydyn nyt tähän tilanteeseen tämän kurssin osalta. Audiossa on myös pieni viive, johon voi vaikuttaa audiobufferin kokoa muuttamalla. Pätkintä kuitenkin pahenee bufferin kokoa pienentäessä, joten näiden asioiden välillä on tasapainoiltava. Käyttäjälle voitaisiin antaa vaihtoehto käynnistäessä valita bufferin koko muutamasta vaihtoehdosta.

## Viikko 5
### Uusia ominaisuuksia:
- Käyttäjä pystyy valitsemaan oskillaattorin aaltomuodon graafista käyttöliittymää käyttäen sahalaita-aallon ('sawtooth wave') ja 'kanttiaallon' ('squarewave') väliltä 
- Käyttäjä pystyy graafisen käyttöliittymän avulla säätämään äänenvoimakkuutta 
- Käyttäjä pystyy graafisen käyttöliittymän avulla valitsemaan onko soitin moniääninen vai yksiääninen.
