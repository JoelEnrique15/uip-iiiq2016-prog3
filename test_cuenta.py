from unittest import TestCase
from Cuenta import Cuenta


class TestCuenta(TestCase):
    def test_depositar(self):
        c= Cuenta("Joel sanchez", "364792",200.00)
        self.assertEqual(c.depositar(200.00),400.00)

    def test_retirar(self):
        c= Cuenta("Joel sanchez", "364792",200.00)
        self.assertEqual(c.retirar(150.00),50.00)
