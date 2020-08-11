import unittest
import LibreríaNumerosComplejos
import math

class TestLibreriaNumerosComplejos(unittest.TestCase):
    
    def test_suma(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(LibreríaNumerosComplejos.suma(c1,c2), (4,6))

    def test_resta(self):
        c1 = [3,4]
        c2 = [1,2]
        self.assertEqual(LibreríaNumerosComplejos.resta(c1,c2), (2,2))

    def test_producto(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(LibreríaNumerosComplejos.producto(c1,c2), (-5,10))

    def test_division(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(LibreríaNumerosComplejos.division(c1,c2), [0.44,0.08])

    def test_modulo(self):
        c1 = [1,2]
        self.assertEqual(LibreríaNumerosComplejos.modulo(c1), math.sqrt(5))

    def test_cart_pol(self):
        c1 = [1,1]
        self.assertEqual(LibreríaNumerosComplejos.conversionComplejoPolar(c1),[1.4142135623730951, 0.7853981633974483])

    def test_pol_cart(self):
        c1 = [1.4142135623730951, 0.7853981633974483]
        self.assertEqual(LibreríaNumerosComplejos.conversionPolarComplejo(c1),[1,1])

    def test_fase(self):
        c1 = [1,2]
        self.assertEqual(LibreríaNumerosComplejos.faseNumeroComplejo(c1),1.1071487177940904)
        
if __name__ == '__main__':
    unittest.main()
