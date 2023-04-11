import unittest
from HW3 import *

class P7_HW3tests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.machine1 = {'S1':{'0':('S2','-'), '1':('S3','G')},
                         'S2':{'0':('S2','-'), '1':('S1','>')}, 
                         'S3':{'0':('S3','-'), '1':('S4','O')}, 
                         'S4':{} 
                }
        self.machine2 = {'Q1':{'0':('Q1','*'), '1':('Q2','1')},
                         'Q2':{'0':('Q1','@'), '1':('Q3','2')}, 
                         'Q3':{'0':('Q1','$'), '1':('Q4','3')}, 
                         'Q4':{'0':('Q1','#'), '1':('Q5','4')}, 
                         'Q5':{}  
                }
        self.input1 = '000010000010001000110000000000'
        self.input2 = '000010000010001000110000000000100000000000011000100'



    #--- Problem 7----------------------------------
    def test_state_machine1(self):
        #test1 - consumes all input before reaching a halting state. 
        out = []
        program = state_machine(self.machine1,iter(self.input1), ('S1',None))
        self.assertEqual(program.__next__(), ('S1', None))  # skip over first output
        for t in program:  
            out.append(t)
        state_output = [('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S3', 'G'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-')]
        str_output = "---->----->--->--->G----------"
        self.assertListEqual(out,state_output)
        self.assertEqual(''.join(list(map(lambda t: t[1],out))),str_output)

    def test_state_machine2(self):
        #test2 - iterator terminates when it reaches a halting state. 
        out = []
        program = state_machine(self.machine1,iter(self.input2), ('S1',None))
        self.assertEqual(program.__next__(), ('S1', None))  # skip over first output
        for t in program:  
            out.append(t)
        state_output = [('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S2', '-'), ('S2', '-'), ('S2', '-'), ('S1', '>'), ('S3', 'G'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S3', '-'), ('S4', 'O')]
        str_output = "---->----->--->--->G----------O"
        self.assertListEqual(out,state_output)
        self.assertEqual(''.join(list(map(lambda t: t[1],out))),str_output)
   
    def bits_stream(self,first):
        """Generator that creates an infinite string of alternating 0's and 1's (three 0's , three 1's)"""
        bits = {'0':'1', '1':'0'}
        current = first
        n = 3 
        while True:
            yield current
            n -= 1
            if n == 0:
                current = bits[current]
                n = 3

    def test_state_machine3(self):
        #test3 - input is infinite 
        # (iterator that produces an infinite stream of 1's and 0's ; doesn't include 4 consecutive 1's). 
        # state_machine iterator never terminates.    
        out = []
        program = state_machine(self.machine2,self.bits_stream('0'), ('Q1',None))
        self.assertEqual(program.__next__(), ('Q1', None))  # skip over first output

        count = 27
        for t in program:  
            if count > 0:
                out.append(t)
                count -= 1
            else: break
        state_output = [('Q1', '*'), ('Q1', '*'), ('Q1', '*'), ('Q2', '1'), ('Q3', '2'), ('Q4', '3'), ('Q1', '#'), ('Q1', '*'), ('Q1', '*'), ('Q2', '1'), ('Q3', '2'), ('Q4', '3'), ('Q1', '#'), ('Q1', '*'), ('Q1', '*'), ('Q2', '1'), ('Q3', '2'), ('Q4', '3'), ('Q1', '#'), ('Q1', '*'), ('Q1', '*'), ('Q2', '1'), ('Q3', '2'), ('Q4', '3'), ('Q1', '#'), ('Q1', '*'), ('Q1', '*')]
        str_output = "***123#**123#**123#**123#**"
        self.assertListEqual(out,state_output)
        self.assertEqual(''.join(list(map(lambda t: t[1],out))),str_output)

if __name__ == '__main__':
    unittest.main(verbosity=2)

