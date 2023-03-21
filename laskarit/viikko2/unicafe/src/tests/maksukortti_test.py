import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortilla_on_oikea_saldo(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        
    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(1000)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
        
    def test_rahan_ottaminen_toimii(self):
        a = self.maksukortti.ota_rahaa(600)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.00 euroa")
        b = self.maksukortti.ota_rahaa(600)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.00 euroa")
        c = self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")
        
        self.assertEqual((a,c), (True, True))
        self.assertEqual(b, False)
