import unittest
from HW3 import *

class P2_HW3tests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.prog_languages = {
            "CptS121" : ["C"],
            "CptS122" : ["C++"],
            "CptS131" : ["Java"],
            "CptS132" : ["Java"],
            "CptS223" : ["C++"],
            "CptS233" : ["Java"],
            "CptS321" : ["C#"],
            "CptS322" : ["Python","JavaScript"],
            "CptS355" : ["Haskell", "Python", "PostScript", "Java"],
            "CptS451" : ["Python", "C#", "SQL"],     
            "CptS360" : ["C"],
            "CptS370" : ["Java"],
            "CptS315" : ["Python"],
            "CptS411" : ["C", "C++"],
            "CptS475" : ["Python", "R"],
            "CptS423" : []
        }

    #--- Problem 2 ----------------------------------
    def test_find_courses1(self):
        output = sorted(['CptS322', 'CptS355', 'CptS451', 'CptS315', 'CptS475'])
        self.assertListEqual(sorted(find_courses(self.prog_languages,'Python')),output)

    def test_find_courses2(self):
        output = sorted(['CptS122', 'CptS223', 'CptS411'])
        self.assertListEqual(sorted(find_courses(self.prog_languages,'C++')),output)

    def test_find_courses3(self):
        output = sorted([])
        self.assertListEqual(sorted(find_courses(self.prog_languages,'Rust')),output)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)

