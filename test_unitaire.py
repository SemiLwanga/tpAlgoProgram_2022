from question_7 import*
import unittest

"""
Cette class permet de tester les resultats 
des methodes de calcul du perimètre 
et de la surface pour les differentes formes géométriques entre autres:
             --- Rectangle
             --- Carré
             --- Cercle
             --- Triangle
             --- Triangle rectangle
"""


class Testing(unittest.TestCase):

    """ Class Rectangle"""
    def test_perimetre_rectangle(self):
        rect = Rectangle(1, 8).perimetre()
        result = 18
        self.assertEqual(rect, result)
    def test_surface_rectangle(self):
        rect = Rectangle(5, 8).surface()
        result = 40
        self.assertEqual(rect, result)

    # ClassMethode Carré
    def test_perimetre_carre(self):
        car = Rectangle.Carre(-5).perimetre()
        result = 20
        self.assertEqual(car, result)

    def test_surface_carre(self):
        car = Rectangle.Carre(-5).surface()
        result = 25
        self.assertEqual(car, result)
    
     # Classe Triangle
    def test_perimetre_triangle(self):
        tri = Triangle(-2,5,4).perimetre()
        result = 11
        self.assertEqual(tri, result)

    def test_surface_triangle(self):
        tri = Triangle(-2,5,4).surface()
        result = 3.799671038392666
        self.assertAlmostEqual(tri, result)

    # ClassMethode Triangle rectangle
    def test_perimetre_triangle_rectangle(self):
        tri = Triangle.Rectangle(3, 4).perimetre()
        result = 12
        self.assertEqual(tri, result)

    def test_surface_triangle_rectangle(self):
        tri = Triangle.Rectangle(3, 4).surface()
        result = 6
        self.assertEqual(tri, result)

    
    
    # Classe Cercle
    def test_perimetre_cercle(self):
        cer = Cercle(5).perimetre()
        result = 31.41592653589793
        self.assertAlmostEqual(cer, result)

    def test_surface_cercle(self):
        cer = Cercle(5).surface()
        result = 78.53981633974483
        self.assertAlmostEqual(cer, result)

if __name__ == '__main__':
    unittest.main()
