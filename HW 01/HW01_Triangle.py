""" 
HW 01 SSW 567 WS
AUTHOR: Vittali Vamshi Krishna

"""




import unittest
import math

def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "not real triangle"
    
    if a == b == c:
        return "equilateral"
    
    if a == b or a == c or b == c:
        return "isosceles"
    
    if a**2 + b**2 == c**2:
        return "scalene"
    
    return "scalene"

class TestClassifyTriangle(unittest.TestCase):
    def testing_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "equilateral")
    
    def testing_isosceles(self):
        self.assertEqual(classify_triangle(3, 4, 4), "isosceles")
    
    def testing_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "scalene")

    def testing_not_real_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "not real triangle")

def main():
    print(classify_triangle(4, 2, 3))
    print(classify_triangle(4, 4, 3))
    print(classify_triangle(6, 6, 4))
    print(classify_triangle(5, 5, 5))
    print(classify_triangle(1, 3, 5))
    
    unittest.main(exit=True)

if __name__ == "__main__":
    main()
