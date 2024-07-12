

import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Rusia", 50, "Ruperto", 3, 1.2)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 6.0)  # 1.2 * 5

if __name__ == '__main__':
    unittest.main()
