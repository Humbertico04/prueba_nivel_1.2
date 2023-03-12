import unittest
import database as db

class TestPolinomio(unittest.TestCase):

    def setUp(self):
        self.p1 = db.Polinomio()
        db.Polinomio.agregar_termino(self.p1, 1, 5)
        db.Polinomio.agregar_termino(self.p1, 2, 2)
        self.p2 = db.Polinomio()
        db.Polinomio.agregar_termino(self.p2, 1, 4)
        db.Polinomio.agregar_termino(self.p2, 3, 6)
        self.p3 = db.Polinomio()

    def test_agregar_termino(self):
        db.Polinomio.agregar_termino(self.p3, 3, -1)
        db.Polinomio.agregar_termino(self.p3, 2, 2)
        db.Polinomio.agregar_termino(self.p3, 1, 4)
        self.assertEqual(db.Polinomio.mostrar(self.p3), "-1x^3+2x^2+4x^1")

    def test_modificar_termino(self):
        db.Polinomio.modificar_termino(self.p1, 1, 7)
        self.assertEqual(db.Polinomio.mostrar(self.p1), "+2x^2+7x^1")

    def test_obtener_valor(self):
        self.assertEqual(db.Polinomio.obtener_valor(self.p2, 1), 4)
        self.assertEqual(db.Polinomio.obtener_valor(self.p2, 3), 6)

    def test_eliminar_termino(self):
        db.Polinomio.eliminar_termino(self.p1, 1)
        self.assertEqual(db.Polinomio.mostrar(self.p1), "+2x^2")

    def test_existe_termino(self):
        self.assertTrue(db.Polinomio.existe_termino(self.p1, 1))
        self.assertFalse(db.Polinomio.existe_termino(self.p2, 2))

    def test_sumar(self):
        p4 = db.Polinomio.sumar(self.p1, self.p2)
        self.assertEqual(db.Polinomio.mostrar(p4), "+6x^3+2x^2+9x^1")

    def test_restar(self):
        p5 = db.Polinomio.restar(self.p1, self.p2)
        self.assertEqual(db.Polinomio.mostrar(p5), "-6x^3+2x^2+1x^1")

if __name__ == '__main__':
    unittest.main()
