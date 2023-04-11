import unittest
from HW3 import *

class P3_HW3tests(unittest.TestCase):
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

    #--- Problem 3 ----------------------------------
    def test_get_by_level1(self):
        output = sorted(['C', 'C++', 'Java', 'Java'])
        self.assertListEqual(sorted(get_by_level(self.prog_languages,1)),output)

    def test_get_by_level2(self):
        output = sorted(['C++', 'Java'])
        self.assertListEqual(sorted(get_by_level(self.prog_languages,2)),output)

    def test_get_by_level3(self):
        output = sorted(['C#', 'Python', 'JavaScript', 'Haskell', 'Python', 'PostScript', 'Java', 'C', 'Java', 'Python'])
        self.assertListEqual(sorted(get_by_level(self.prog_languages,3)),output)

    def test_get_by_level4(self):
        output = sorted(['Python', 'C#', 'SQL', 'C', 'C++', 'Python', 'R'])
        self.assertListEqual(sorted(get_by_level(self.prog_languages,4)),output)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

