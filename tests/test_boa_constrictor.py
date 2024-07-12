

import unittest
from models.boa_constrictor import BoaConstrictor

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = BoaConstrictor("Brasil", 100, "Marina", 10, 5.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 50.0)  # 5.0 * 10

    def test_comer_raton_exitoso(self):
        self.boa.comer_raton()
        self.assertEqual(self.boa.dar_ratones_comidos(), 1)

    def test_comer_raton_demasiados(self):
        for _ in range(10):
            self.boa.comer_raton()
        with self.assertRaises(ValueError):
            self.boa.comer_raton()
        self.assertEqual(self.boa.dar_ratones_comidos(), 20)