from synth.synthesizer import Synthesizer

synth = Synthesizer()

print()
print("Tämänhetkisessä versiossa voit soittaa")
print("syntetisaattoria tietokoneesi näppäimistöllä.")
print("Koskettimet on sijoitettu näppäimistölle seuraavaan tapaan:")
print(" W E    T Y U")
print("A S D F G H J K L")
print("jossa alempri rivi on valkoiset koskettimet")
print("ja ylempi mustat.")
print("Käytössä on siis yksi oktaavi,")
print("joka alkaa C:stä ja loppuu C:hen.")
print()
print("Voit vaihtaa graafisen käyttöliittymän kautta oskillaattorin")
print("aaltomuotoa valiten sahalaita-aallon ja kanttiaallon väliltä.")
print("Voit myös säätää äänenvoimakkuutta liukusäätimellä")
print("ja valita, onko soitin moniääninen.")
print()
print("Jos ääni pätkii, käynnistä ohjelma suosiolla uudestaan.")
print()

synth.run()
