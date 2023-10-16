import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testvalidtriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', "Expect Right")

    def testvalidtriangle2(self):
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral', "Expect Equilateral")

    def testvalidtriangle3(self):
        self.assertEqual(classifyTriangle(3, 3, 2), 'Isosceles', "Expect Isosceles")

    def testvalidtriangle4(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', "Expect Scalene")

    def testinvalidtriangle1(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', "Expect Not a Triangle")

    def testinvalidtriangle2(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', "Expect Invalid Input")

    def testinvalidtriangle3(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', "Expect Invalid Input")

    def testinvalidtriangle4(self):
        self.assertEqual(classifyTriangle(200, 300, 500), 'InvalidInput', "Expect Invalid Input")

    def testnonnumericinput(self):
        with self.assertRaises(ValueError):
            classifyTriangle("a", "b", "c")

    def testvalidtriangle5(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', "Expect Right")

    def testvalidtriangle6(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right', "Expect Right")

    def testvalidtriangle7(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', "Expect Right")

    def testvalidtriangle8(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', "Expect Right")

    def testvalidtriangle9(self):
        self.assertEqual(classifyTriangle(7, 24, 25), 'Right', "Expect Right")

    def testvalidtriangle10(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', "Expect Isosceles")

    def testvalidtriangle11(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles', "Expect Isosceles")

    def testvalidtriangle12(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', "Expect Right")

    def testvalidtriangle13(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral', "Expect Equilateral")

    def testvalidtriangle15(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', "Expect Equilateral")

    def testinvalidtriangle5(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', "Expect Not a Triangle")

#... (You can continue to add more cases as needed)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
