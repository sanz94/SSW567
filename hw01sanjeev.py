
"""
Triangle Classification
@author: Sanjeev Rajasekaran
"""

import unittest

def classifyTriangle(a, b, c):
    """

    takes three sides of the triangle as input

    """

    if a+b < c or a+c < b or b+c < a:
        return "Not a Triangle"
    RightTriangle = "Not Right Triangle"
    if (pow(a, 2) + pow(b, 2) == pow(c, 2)) or (pow(a, 2) + pow(c, 2) == pow(b, 2)) or (pow(c, 2) + pow(b, 2) == pow(a, 2)):
        RightTriangle = "Right Triangle"
    if a == b == c:
        return 'Equilateral' + " " + RightTriangle
    elif a == b or a == c or b == c:
        return 'Isoceles' + " " + RightTriangle
    else:
        return 'Scalene' + " " + RightTriangle


def runClassifyTriangle(a, b, c):
    """ call classifytriangle """
    print(classifyTriangle(a, b, c))


class TestTriangles(unittest.TestCase):

    def testSet1(self):  # test invalid inputs

        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene Right Triangle')
        self.assertEqual(classifyTriangle(3, 4, 12), 'Not a Triangle')

    def testMyTestSet2(self):

        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral Not Right Triangle')
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isoceles Right Triangle')
        self.assertEqual(classifyTriangle(10, 15, 30), 'Scalene Not Right Triangle')


if __name__ == '__main__':

    runClassifyTriangle(1, 2, 3)
    runClassifyTriangle(1, 1, 1)

    unittest.main(exit=False)




