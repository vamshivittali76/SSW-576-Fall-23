def classify_triangle(a, b, c):

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("invalid input: all inputs must be numeric")

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    if round(a**2 + b**2, 2) == round(c**2, 2) or \
       round(b**2 + c**2, 2) == round(a**2, 2) or \
       round(a**2 + c**2, 2) == round(b**2, 2):
        return 'Right'

    if a == b and b == c:
        return 'Equilateral'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'
