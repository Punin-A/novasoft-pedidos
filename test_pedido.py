import unittest
from pedido import calcular_total


class TestPedido(unittest.TestCase):
    def test_total(self):
        self.assertEqual(calcular_total(12.50, 2), 25.00)

    def test_datos_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_total(-1, 2)


if __name__ == "__main__":
    unittest.main()