# CptS 355 - Fall 2022 - Assignment 3 - Python 
# Name: Muhammad Ali Dzulfiqar
# Collaborators:  


from functools import reduce


debugging = False 
def debug(*s):  
    if debugging:  
         print(*s) 

# 1. create_lang_dict (courses) –  8% 

# The following dictionary stores the programming languages used in various WSU CptS courses.  

# prog_languages = { 
#      "CptS121" : ["C"], 
#      "CptS122" : ["C++"], 
#      "CptS131" : ["Java"], 
#      "CptS132" : ["Java"], 
#      "CptS223" : ["C++"], 
#      "CptS233" : ["Java"], 
#      "CptS321" : ["C#"], 
#      "CptS322" : ["Python", "JavaScript"], 
#      "CptS355" : ["Haskell", "Python", "PostScript", "Java"], 
#      "CptS451" : ["Python", "C#", "SQL"],      
#      "CptS360" : ["C"], 
#      "CptS370" : ["Java"], 
#      "CptS315" : ["Python"], 
#      "CptS411" : ["C", "C++"], 
#      "CptS475" : ["Python", "R"], 
#      "CptS423" : [] 
#     } 

# test
# prog_languages = {
#             "Cpts111" : ["Python"],
#             "CptS121" : ["C"],
#             "CptS122" : ["C","C++"],
#             "CptS131" : ["Java"],
#             "CptS132" : ["Java"],
#             "CptS223" : ["C++"],
#             "CptS233" : ["Java"],
#             "CptS321" : ["C#"],
#             "CptS322" : ["Python","JavaScript"],
#             "CptS350" : ["Python"],
#             "CptS355" : ["Haskell", "Python", "PostScript", "Java"],
#             "CptS451" : ["Python", "C#", "SQL"],     
#             "CptS360" : ["C"],
#             "CptS370" : ["Java"],
#             "CptS315" : ["Python"],
#             "CptS411" : ["C", "C++"],
#             "CptS475" : ["Python", "R"],
#             "CptS423" : []
#        }

# prog_languages = {
#             "Cpts111" : ["Python"],
#             "CptS121" : ["C"],
#             "CptS122" : ["C","C++"],
#             "CptS131" : ["Java"],
#             "CptS132" : ["Java"],
#             "CptS223" : ["C++"],
#             "CptS233" : ["Java"],
#             "CptS321" : ["C#"],
#             "CptS322" : ["Python","JavaScript"],
#             "CptS350" : ["Python"],
#             "CptS355" : ["Haskell", "Python", "PostScript", "Java"],
#             "CptS451" : ["Python", "C#", "SQL"],     
#             "CptS360" : ["C"],
#             "CptS370" : ["Java"],
#             "CptS315" : ["Python"],
#             "CptS411" : ["C", "C++"],
#             "CptS475" : ["Python", "R"],
#             "CptS423" : [],
#             "CptS575" : ["Python", "R"]
#         }
# Assume, you would like to rearrange this data and  create a dictionary where the keys are the programming 
# languages and the values are lists of the CptS courses that use those languages, e.g.,   
 
# {        'C': ['CptS121', 'CptS360', 'CptS411'],  
#        'C++': ['CptS122', 'CptS223', 'CptS411'],  
#       'Java': ['CptS131', 'CptS132', 'CptS233', 'CptS355', 'CptS370'],  
#         'C#': ['CptS321', 'CptS451'],  
#     'Python': ['CptS315', 'CptS322', 'CptS355', 'CptS451', 'CptS475'],  
# 'JavaScript': ['CptS322'],  
#    'Haskell': ['CptS355'],  
# 'PostScript': ['CptS355'],  
#        'SQL': ['CptS451'],  
#          'R': ['CptS475']  } 

# Write a function create_lang_dict that takes the prog_languages data as input and rearranges keys 
# as described above. You may use loops in your solution. The items in the output dictionary can have 
# arbitrary order. 

# create_lang_dict(prog_languages) returns the above dictionary.  

# Important Notes:  
# 1. Your function should not change the input dictionary value.  
# 2. You should not hardcode the keys and values (language and course names) in your solution.  
# 3. You are not allowed to import additional Python libraries we haven’t covered in class.  

def create_lang_dict(courses):
    dictionary = {}
    for course, programming_language in courses.items():
        for language in programming_language:
            if language not in dictionary.keys():
                dictionary[language] = []
            dictionary[language].append(course)
    return dictionary

# print(create_lang_dict(prog_languages))

# 2. find_courses(lang_dict,language)– 10% 
# Assume you would like to find the courses that use a given programming language. Write a function 
# “find_courses” that takes the programming languages data and a programming language name as input, 
# and it returns a list of courses that use the given language. For example,  
 
# find_courses(prog_languages,"Python") returns   
# ['CptS322','CptS355','CptS451','CptS315','CptS475'] 
 
# find_courses(prog_languages,"C++") returns  
# ['CptS122', 'CptS223', 'CptS411'] 
 
# Your function definition should not use loops or recursion but use the Python map, reduce, and/or 
# filter functions. You may define and call helper (or anonymous) functions, however your helper 
# functions should not use loops or recursion. You cannot use create_lang_dict function you defined in 
# problem 1.  You will not get any points if your solution (or helper functions) uses a loop. If you are using 
# reduce, make sure to import it from functools. 


def find_courses(lang_dict, languages):
    check_lang = filter(lambda t: languages in t[1], lang_dict.items())
    get_course = map(lambda t:t[0], check_lang)
    return list(get_course)

#find_course_helper(languages, lang_dict.values())
    

# print(find_course(prog_languages, "C++"))


# 3. get_by_level(lang_dict,level)– 15% 
# Assume you would like to find the programming languages used by the courses at a given class level. Write 
# a function “get_by_level” that takes the programming languages data and a class level (e.g., 1,2,3,or 4) 
# as input, and it returns a list of programming languages used by the courses at that level. All 100-level 
# courses are assumed to have level 1, 200-level courses are assumed to have level 2, etc.  
 
# For example,  
# get_by_level(prog_languages,1)  returns   
# ['C', 'C++', 'Java', 'Java']   
# # languages for "CptS121", "CptS122","CptS131","CptS132" 
 
# get_by_level(prog_languages,4)  returns   
# ['Python', 'C#', 'SQL', 'C', 'C++', 'Python', 'R'] 
# # languages for "CptS411", "CptS475","CptS451","CptS423" 
 
# Note that the output may include duplicates if the same language is used by more than one course at that 
# level. The output should be sorted in ascending order.  
 
# Your function definition should not use loops or recursion but use the Python map, reduce, and/or 
# filter functions. You may define and call helper (or anonymous) functions, however your helper 
# functions should not use loops or recursion.  You will not get any points if your solution (or helper 
# functions) uses a loop. If you are using reduce, make sure to import it from functools. 
# Important Notes:  
# 1. You can assume that all courses are CptS courses.  
# 2. You can assume that 4th through 7th characters in course names are the course numbers.   
# 3. You are not allowed to import additional Python libraries we haven’t covered in class.

def get_by_level(lang_dict, level):
    get_list = list(lang_dict.items())
    filter_level = filter(lambda x: level == int(x[0][4]), get_list)
    get_courses = map(lambda x: x[1], filter_level)
    flatten_list = reduce(lambda x,y: x+y, get_courses)
    return sorted(list(flatten_list))

# print(get_by_level(prog_languages, 5))

# 4. all_prerequisites(course_dict,course)– 15% 
# Consider the following dictionary that stores the prerequisite for some CptS courses at WSU. For simplicity, 
# we assume that each course has a single prerequisite course.  
 
# prerequisites ={ 
#             "CptS122" : "CptS121", 
#             "CptS132" : "CptS131", 
#             "CptS223" : "CptS122", 
#             "CptS233" : "CptS132", 
#             "CptS260" : "CptS121", 
#             "CptS317" : "CptS223", 
#             "CptS321" : "CptS223", 
#             "CptS322" : "CptS223", 
#             "CptS355" : "CptS223", 
#             "CptS360" : "CptS317", 
#             "CptS370" : "CptS233", 
#             "CptS315" : "CptS233", 
#             "CptS460" : "CptS360", 
#             "CptS451" : "CptS223", 
#             "CptS475" : "CptS122", 
#             "CptS423" : "CptS322"   } 

# prerequisites = {
#             "Math103" : "Math100",
#             "Math105" : "Math103",
#             "Math106" : "Math103",
#             "Math108" : "Math106",
#             "Math140" : "Math108",
#             "Math171" : "Math108",
#             "Math172" : "Math171",
#             "Math201" : "Math103",
#             "Math202" : "Math201",
#             "Math216" : "Math108",
#             "Math220" : "Math171",
#             "Math273" : "Math172"
#         } 
 
# Write a function all_prerequisites that takes a course dictionary (similar to prerequisites) and a 
# course name (for example "CptS423") and it returns the list of all prerequisites of the given course. Your 
# function should continue to search through the prerequisite chain backwards, until  it finds the course 
# without a prerequisite.  
# For example: 
# all_prerequisites(prerequisites,"CptS423") returns  
# ['CptS121', 'CptS122', 'CptS223', 'CptS322'] 
# The prerequisite of 'CptS423'is 'CptS322', whose prerequisite is 'CptS223' and further whose 
# prerequisite is 'CptS122' . And, finally, 'CptS122's prerequisite is 'CptS121', which doesn’t have any 
# prerequisites.  
# Important Note:  
# - The output list should be sorted – in ascending order.  
# - You are not allowed to use Python libraries we haven’t covered in class.  
# - You should not hardcode the keys ( course names) in your solution. 
# - You should not assume a max chain of prerequisites. 

def all_prerequisites(course_dict, course):
    list_of_prerequisites = []
    index = course
    while(index in course_dict.keys()):
        if index in course_dict.keys():
            list_of_prerequisites.append(course_dict[index])
            index = course_dict[index]
    return sorted(list_of_prerequisites)
            

# print(all_prerequisites(prerequisites,"Math273"))

# 5. roll(lst,n,count)– 10% 
# Write a function, roll, that will take a list (lst) , a number (n) and a count value (count) as input and it 
# rolls the last n elements of the list lst count times. If the count value is positive (>0), it rolls the list in 
# clockwise direction; otherwise it rolls it in counter clockwise direction. It returns the rolled list.  
# For example,  
# roll([1,2,3,4,5,6,7,8,9,10], 5, 3) rolls the last 5 elements of the list 3 times in clockwise direction.  
# 1st rotation: [1,2,3,4,5,10,6,7,8,9] 
# 2nd rotation: [1,2,3,4,5,9,10,6,7,8] 
# 3rd rotation: [1,2,3,4,5,8,9,10,6,7] 
# roll([1,2,3,4,5,6,7,8,9,10], 5, -3) rolls the last 5 elements of the list 3 times in counter clockwise 
# direction.  
# 1st rotation: [1,2,3,4,5,7,8,9,10,6] 
# 2nd rotation: [1,2,3,4,5,8,9,10,6,7] 
# 3rd rotation: [1,2,3,4,5,9,10,6,7,8] 

def roll(lst, n, count):
    start_list = lst[:-n]
    end_list = lst[-n:]
    helper = end_list[-count:] + end_list[:-count]
    result = start_list + helper
    return result

# print(roll([1,2,3,4,5,6,7,8,9,10], 7, -5))

# 6. split_at_parenthesis(str_input)– 14% 
# Write a recursive function, split_at_parenthesis, that will take a string including several matching 
# parenthesis characters and it will group the characters between two matching parenthesis characters in a 
# sublist. It returns a nested list ; matching the nested structure of the parenthesis in the input string.  
 
# For example,  
# split_at_parenthesis("12(3((4(56()))(7)8)9)0") returns  
# ['1', '2', ['3', [['4', ['5', '6', []]], ['7'], '8'], '9'], '0'] 
 
# split_at_parenthesis("Py(((th(o))n)(HW))3") returns  
# ['P', 'y', [[['t', 'h', ['o']], 'n'], ['H', 'W']], '3'] 
 
# Suggestions:  
# - Give a recursive solution.  
# - Convert the string to an iterator by applying the iter function. As you iterate over the characters, 
# the characters  other than '(' and ')' should be appended to a list.  
# - The iterator should be passed to the recursive call when the next character is '('. And the list 
# returned by the recursive call should be appended to the output.    
# - When the next character is ')', you should stop the recursion and return the characters collected 
# in the output.  
 
def split_at_parenthesis(str_input):
    str_iterable = iter(str_input)
    result = []
    for c in str_iterable:
        if c == '(':
            result.append(split_at_parenthesis(str_iterable))
        elif c == ')':
            break
        else:
            result.append(c)
    return result


# print(split_at_parenthesis("()(13)(12331)()()21213190912(012(12313))"))

# 7. Iterators 
# state_machine – 18% 
# Consider the following dictionary that represents a state machine illustrated in the below figure.  

# machine1 = {'S1':{'0':('S2','-'), '1':('S3','G')}, 
#             'S2':{'0':('S2','-'), '1':('S1','>')},  
#             'S3':{'0':('S3','-'), '1':('S4','O')},  
#             'S4':{}  
#            } 

# machine1 = {'S1':{'0':('S2','+'), '1':('S3','%')},
#                          'S2':{'0':('S1','-'), '1':('S2','/')}, 
#                          'S3':{'0':('S3','+'), '1':('S4','*')}, 
#                          'S4':{'0':('S5','+'), '1':('S1','*')},
#                          'S5':{} }

# input1 = '011001010000'                       
# Assume the state machine reads from an infinite stream of 0’s and 
# 1’s ; and depending on the input character value, it changes its 
# state (or stays at the current state)  and produces an output 
# character.   
# In the above state machine, when the machine is in S1, if the 
# input is '0', it will transition to S2 and produce the output '-'. If 
# the input is '1', it will transition to S3, and produce the output, 
# 'G'.  

# Create an iterator that represents a state machine initialized with: 
# - a set of states and transition rules given as a Python dictionary (similar to machine1 above) 
# - a finite or infinite string input of  0's and '1's. 
# - a starting state 
# The iterator will represent the sequence of (state,output)  tuples when the machine is run with the 
# input. At each call to  __next__(),the iterator will return such a tuple, including the next state of the 
# machine and the output character it will return.  
# Important Note: Your state_machine implementation should calculate the next (state,output) 
# tuple  as needed.  An implementation that precomputes all tuples for the given input and  dumps all tuples 
# to a list ahead of time will be worth only 5 points. 
 
# For example:    
# machine1 = {'S1':{'0':('S2','-'), '1':('S3','G')}, 
#             'S2':{'0':('S2','-'), '1':('S1','>')},  
#             'S3':{'0':('S3','-'), '1':('S4','O')},  
#             'S4':{}  
#            } 
# input1 = '000010000010001000110000000000' 
 
# #test1 - consumes all input before reaching a halting state.  
# out = [] 
# program = state_machine(machine1,iter(input1), ('S1',None)) 
# print(program.__next__()) # skip over first output 
# for t in program:   
#     out.append(t) 
 
# Out will be: 
# [('S2','-'), ('S2','-'), ('S2','-'), ('S2','-'), ('S1','>'), ('S2','-'),('S2', '-'),    
#  ('S2','-'), ('S2','-'), ('S2','-'), ('S1','>'), ('S2','-'), ('S2','-'), ('S2','-'),  
#  ('S1','>'), ('S2','-'), ('S2','-'), ('S2','-'), ('S1','>'), ('S3','G'), ('S3','-'),  
#  ('S3','-'), ('S3','-'), ('S3','-'), ('S3','-'), ('S3','-'), ('S3','-'), ('S3','-'),  
#  ('S3','-'), ('S3', '-')] 
 
# print (''.join(list(map(lambda t: t[1],out)))) 
# # will print "---->----->--->--->G----------" 
 
# Several additional tests are provided in the unittest test samples. Please note that, your iterator should 
# work with infinitely long input strings as well (see the third test in the givens sample tests.) 

class state_machine(object):
    def __init__(self, set_of_states, input, start_state):
        self.set_of_states = set_of_states
        self.input = iter(input)
        self.current = start_state

    def __next__(self):
        if self.current == None:
            raise StopIteration
        try:
            single_input = next(self.input)
        except StopIteration:
            temp = self.current
            self.current = None
            return temp
        current_state = self.set_of_states[self.current[0]]
        if single_input not in current_state:
            temp = self.current 
            self.current = None
            return temp
        temp = self.current
        self.current = current_state[single_input]
        return temp

    def __iter__(self):
        return self

# out = [] 
# program = state_machine(machine1,iter(input1), ('S1',None)) 
# print(program.__next__()) # skip over first output 
# for t in program:   
#     out.append(t) 

# print(out)
# print (''.join(list(map(lambda t: t[1],out)))) 