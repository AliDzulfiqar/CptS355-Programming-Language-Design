import unittest
from HW3 import *
class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.prog_languages = {
            "Cpts111" : ["Python"],
            "CptS121" : ["C"],
            "CptS122" : ["C","C++"],
            "CptS131" : ["Java"],
            "CptS132" : ["Java"],
            "CptS223" : ["C++"],
            "CptS233" : ["Java"],
            "CptS321" : ["C#"],
            "CptS322" : ["Python","JavaScript"],
            "CptS350" : ["Python"],
            "CptS355" : ["Haskell", "Python", "PostScript", "Java"],
            "CptS451" : ["Python", "C#", "SQL"],     
            "CptS360" : ["C"],
            "CptS370" : ["Java"],
            "CptS315" : ["Python"],
            "CptS411" : ["C", "C++"],
            "CptS475" : ["Python", "R"],
            "CptS423" : [],
            "CptS575" : ["Python", "R"]
        }
        self.prerequisites = {
            "Math103" : "Math100",
            "Math105" : "Math103",
            "Math106" : "Math103",
            "Math108" : "Math106",
            "Math140" : "Math108",
            "Math171" : "Math108",
            "Math172" : "Math171",
            "Math201" : "Math103",
            "Math202" : "Math201",
            "Math216" : "Math108",
            "Math220" : "Math171",
            "Math273" : "Math172"
        }
        self.input1 = [1,2,3,4,5,6,7,8,9,10]
        self.input2 = "()(13)(12331)()()21213190912(012(12313))"
        self.input3 = '011001010000'
        self.machine1 = {'S1':{'0':('S2','+'), '1':('S3','%')},
                         'S2':{'0':('S1','-'), '1':('S2','/')}, 
                         'S3':{'0':('S3','+'), '1':('S4','*')}, 
                         'S4':{'0':('S5','+'), '1':('S1','*')},
                         'S5':{} }

    def sort_values(self,d):
        return dict(map(lambda t: (t[0],list(sorted(t[1]))), d.items()))
    
    #--- Problem 1----------------------------------
    
    
    def test_create_lang_dict(self):
        output = {'Python': ['Cpts111', 'CptS322', 'CptS350', 'CptS355', 'CptS451', 'CptS315', 'CptS475', 'CptS575'], 'C': ['CptS121', 'CptS122', 'CptS360', 'CptS411'], 'C++': ['CptS122', 'CptS223', 'CptS411'], 'Java': ['CptS131', 'CptS132', 'CptS233', 'CptS355', 'CptS370'], 'C#': ['CptS321', 'CptS451'], 'JavaScript': ['CptS322'], 'Haskell': ['CptS355'], 'PostScript': ['CptS355'], 'SQL': ['CptS451'], 'R': ['CptS475', 'CptS575']}

        self.assertDictEqual(self.sort_values(create_lang_dict(self.prog_languages)),self.sort_values(output))
    
    #--- Problem 2----------------------------------
    def test_find_courses(self):
        output = sorted([])
        
        self.assertListEqual(sorted(find_courses(self.prog_languages,'Golang')),output)

    #--- Problem 3 ----------------------------------
    def test_get_by_level(self):
        output = sorted(['Python', 'R'])

        self.assertListEqual(sorted(get_by_level(self.prog_languages,5)),output)
        
    #--- Problem 4----------------------------------
    def test_all_prerequisites(self):
        output = sorted(['Math100', 'Math103', 'Math106', 'Math108', 'Math171', 'Math172'])
        
        self.assertListEqual(sorted(all_prerequisites(self.prerequisites,"Math273")), output)
            
    #--- Problem 5 ----------------------------------
    def test_roll(self):
        output = [1, 2, 3, 9, 10, 4, 5, 6, 7, 8]
        self.assertListEqual(roll(self.input1,7,-5),output)
        
    #--- Problem 6----------------------------------
    def test_split_at_parenthesis(self):
        output = [[], ['1', '3'], ['1', '2', '3', '3', '1'], [], [], '2', '1', '2', '1', '3', '1', '9', '0', '9', '1', '2', ['0', '1', '2', ['1', '2', '3', '1', '3']]]
        self.assertListEqual(split_at_parenthesis(self.input2),output )
    
    #--- Problem 7----------------------------------
    def test_state_machine(self):
        out = []
        program = state_machine(self.machine1,iter(self.input3), ('S1',None))
        self.assertEqual(program.__next__(), ('S1', None))  # skip over first output
        for t in program:  
            out.append(t)
        state_output = [('S2', '+'), ('S2', '/'), ('S2', '/'), ('S1', '-'), ('S2', '+'), ('S2', '/'), ('S1', '-'), ('S3', '%'), ('S3', '+'), ('S3', '+'), ('S3', '+'), ('S3', '+')]
        str_output = "+//-+/-%++++"
        self.assertListEqual(out,state_output)
        self.assertEqual(''.join(list(map(lambda t: t[1],out))),str_output)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
