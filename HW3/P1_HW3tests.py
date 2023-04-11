import unittest
from HW3 import *

class P1_HW3tests(unittest.TestCase):
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
    def sort_values(self,d):
        return dict(map(lambda t: (t[0],list(sorted(t[1]))), d.items()))

    #--- Problem 1----------------------------------
    def test_create_lang_dict(self):
        output = {'C': ['CptS121', 'CptS360', 'CptS411'], 
                'C++': ['CptS122', 'CptS223', 'CptS411'], 
               'Java': ['CptS131', 'CptS132', 'CptS233', 'CptS355', 'CptS370'], 
                 'C#': ['CptS321', 'CptS451'], 
             'Python': ['CptS315', 'CptS322', 'CptS355', 'CptS451', 'CptS475'], 
         'JavaScript': ['CptS322'], 
            'Haskell': ['CptS355'], 
                'SQL': ['CptS451'], 
         'PostScript': ['CptS355'],                 
                  'R': ['CptS475']  }

        self.assertDictEqual(self.sort_values(create_lang_dict(self.prog_languages)),self.sort_values(output))
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
