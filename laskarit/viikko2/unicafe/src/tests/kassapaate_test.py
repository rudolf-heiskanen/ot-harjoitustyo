import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_alustus_toimii(self):
        self.assertNotEqual(self.paate, None)
    
        rahaakassassa = self.paate.kassassa_rahaa
        myytyjaedullisia = self.paate.edulliset
        myytyjamaukkaita = self.paate.maukkaat

        self.assertEqual(rahaakassassa, 100000)
        self.assertEqual((myytyjaedullisia, myytyjamaukkaita), (0,0))
    
    def test_kateisosto_toimii(self):
        vaihtoraha_edullinen = self.paate.syo_edullisesti_kateisella(600)
        vaihtoraha_maukas = self.paate.syo_maukkaasti_kateisella(600)
        self.assertEqual(vaihtoraha_edullinen, 360)
        self.assertEqual(vaihtoraha_maukas, 200)
        
        rahaakassassa = self.paate.kassassa_rahaa
        maukkaat, edulliset = self.paate.maukkaat, self.paate.edulliset
        self.assertEqual(rahaakassassa, 100640)
        self.assertEqual((maukkaat, edulliset), (1,1))
    
    def test_kateisosto_liian_vahalla_rahalla_toimii(self):
        vaihtoraha_edullinen = self.paate.syo_edullisesti_kateisella(200)
        vaihtoraha_maukas = self.paate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha_edullinen, 200)
        self.assertEqual(vaihtoraha_maukas, 300)
        
        
        rahaakassassa = self.paate.kassassa_rahaa
        maukkaat, edulliset = self.paate.maukkaat, self.paate.edulliset
        self.assertEqual(rahaakassassa, 100000)
        self.assertEqual((maukkaat, edulliset), (0,0))
    
    def test_kortilla_ostaminen_toimii(self):
        edullinen = self.paate.syo_edullisesti_kortilla(self.kortti)
        maukas = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((edullinen, maukas), (True, True))
        
        rahaakassassa = self.paate.kassassa_rahaa
        maukkaat, edulliset = self.paate.maukkaat, self.paate.edulliset
        self.assertEqual(rahaakassassa, 100000)
        self.assertEqual((maukkaat, edulliset), (1,1))
         
    def test_kortilla_ostaminen_vahalla_rahalla_toimii(self):
        kortti = Maksukortti(100)
        edullinen = self.paate.syo_edullisesti_kortilla(kortti)
        maukas = self.paate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((edullinen, maukas), (False, False))
        
        rahaakassassa = self.paate.kassassa_rahaa
        maukkaat, edulliset = self.paate.maukkaat, self.paate.edulliset
        self.assertEqual(rahaakassassa, 100000)
        self.assertEqual((maukkaat, edulliset), (0,0))
    
    def test_rahan_lataaminen_toimii(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.paate.lataa_rahaa_kortille(self.kortti, -200)
        kassa = self.paate.kassassa_rahaa
        kortti = self.kortti.saldo
        
        self.assertEqual(kassa, 100100)
        self.assertEqual(kortti, 1100)
