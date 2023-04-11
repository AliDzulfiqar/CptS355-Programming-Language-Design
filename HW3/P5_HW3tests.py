import unittest
from HW3 import *

class P5_HW3tests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.input1 = [1,2,3,4,5,6,7,8,9,10]
        self.input2 = list("CptS322355")
            
    #--- Problem 5 ----------------------------------
    def test_roll1(self):
        output = [1, 2, 3, 4, 5, 8, 9, 10, 6, 7]
        self.assertListEqual( roll(self.input1,5,3),output )

    def test_roll2(self):
        output = [1, 2, 3, 4, 5, 9, 10, 6, 7, 8]
        self.assertListEqual( roll(self.input1,5,-3),output )

    def test_roll3(self):
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertListEqual( roll(self.input1,5,-5),output )

    def test_roll4(self):
        output = list("CptS355322")
        self.assertListEqual( roll(self.input2,6,3),output )

if __name__ == '__main__':
    unittest.main(verbosity=2)

