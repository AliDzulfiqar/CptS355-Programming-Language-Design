import unittest
from HW3 import *

class P6_HW3tests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.input1 = "12(3((4(56()))(7)8)9)0"
        self.input2 = "Py(((th(o))n)(HW))3"
        
    #--- Problem 6----------------------------------
    def test_split_at_parenthesis1(self):
        output = ['1', '2', ['3', [['4', ['5', '6', []]], ['7'], '8'], '9'], '0']
        self.assertListEqual(split_at_parenthesis(self.input1),output )

    def test_split_at_parenthesis2(self):
        output = ['P', 'y', [[['t', 'h', ['o']], 'n'], ['H', 'W']], '3']
        self.assertListEqual(split_at_parenthesis(self.input2),output )


if __name__ == '__main__':
    unittest.main(verbosity=2)

