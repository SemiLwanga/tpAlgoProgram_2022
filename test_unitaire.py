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
