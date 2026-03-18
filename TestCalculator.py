import unittest
from Calculator import Calculator

class Testcalculator(unittest.TestCase):
    def setUp(self):
        self.cal=Calculator()
    def tearDown(self):
        del self.cal
    def testaddition(self):
        self.assertEqual(self.cal.addition(2,3),5)
    def testsubtraction(self):
        self.assertEqual(self.cal.subtraction(3,2),1)
    def testmultiplication(self):
        self.assertEqual(self.cal.multiplication(3,2),6)
    def testdivision(self):
        self.assertEqual(self.cal.division(6,2),3)

