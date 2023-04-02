# Changelog

## Viikko 3
- Käyttäjä näkee listan invoke -tehtävistä ja pystyy käyttämään niitä
- Käyttäjä pystyy ajamaan ohjelman, ja tietokoneen näppäimiä painamalla soittaa sawtooth-aallon.
- Lisätty kaikki luokat, jotka ovat välttämättömiä tälle toiminnallisuudelle, eli 
	- Synthesizer, joka vastaa sovelluksen ison kuvan organisoinnista
	- Synthengine, joka vastaa inputtina saamiensa nuottien prosessoimisesta ääneksi
		- Voice, joka vastaa yhden tietyllä hetkellä soivan sävelen muuttamisesta audioksi
			- Oscillator, joka vastaa yhden Voicen äänen pohjana toimivien ääniaaltojen generoimisesta
	- Playbackdevice, joka vastaa synthenginen generoiman audion soittamisesta tietokoneen kaiuttimista
	- Ui, joka tällä hetkellä vain lukee PyGamen avulla näppäimistön syötettä soittamista varten
