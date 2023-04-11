import unittest
from HW3 import *

class P4_HW3tests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.prerequisites = {
            "CptS122" : "CptS121",
            "CptS132" : "CptS131",
            "CptS223" : "CptS122",
            "CptS233" : "CptS132",
            "CptS260" : "CptS121",
            "CptS317" : "CptS223",
            "CptS321" : "CptS223",
            "CptS322" : "CptS223",
            "CptS355" : "CptS223",
            "CptS360" : "CptS317",
            "CptS370" : "CptS233",
            "CptS315" : "CptS233",
            "CptS460" : "CptS360",
            "CptS451" : "CptS223",
            "CptS475" : "CptS122",
            "CptS423" : "CptS322"
        }

    #--- Problem 4----------------------------------
    def test_all_prerequisites1(self):
        output = sorted(['CptS121', 'CptS122', 'CptS223', 'CptS322'])
        self.assertListEqual(sorted(all_prerequisites(self.prerequisites,'CptS423')),output)

    def test_all_prerequisites2(self):
        output = sorted(['CptS121', 'CptS122', 'CptS223', 'CptS317', 'CptS360'])
        self.assertListEqual(sorted(all_prerequisites(self.prerequisites,'CptS460')),output)

    def test_all_prerequisites3(self):
        output = sorted([])
        self.assertListEqual(sorted(all_prerequisites(self.prerequisites,'CptS302')),output)

if __name__ == '__main__':
    unittest.main(verbosity=2)

