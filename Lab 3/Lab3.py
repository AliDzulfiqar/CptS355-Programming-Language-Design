# CptS 355 - Fall 2022 - Lab 3
# Muhammad Ali Dzulfiqar

from functools import reduce


debugging = False
def debug(*s): 
     if debugging: 
          print(*s)


# 1. getNumCases(data,counties,months)  
# Assume that you work for a “Healthcare Data Analytics” company and you write scripts to process 
# various dataset. In your analysis, you use the CDC’s COVID-19 dataset. For example, the following 
# dataset reports the monthly new COVID cases in year 2020 for some counties in WA.  

# CDCdata = {'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},  
# 'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266},  
# 'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811},  
# 'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751},  
# 'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} } 
 
# The keys of the dictionary are the county names, and the values are the dictionaries which include 
# the monthly new COVID cases. Note that some counties may not have any new cases in some 
# months.  
# Define a function, getNumCases, which calculates the total number of new cases for a given list 
# of counties during a given list of months. For example: 
 
# getNumCases(CDCdata,['Whitman'],['Apr','May','Jun']) returns 31, and  
# getNumCases(CDCdata,['King','Pierce'],['July','Aug']) returns 13587. 
 
# (Important note: Your function should not hardcode the county names and the month 
# abbreviations. It should simply iterate over the keys that appear in the given dictionary. You will be 
# deducted points if you hardcode any keys. )  
 
# You can start with the following code: 

# def getNumCases(data,counties,months):
#     num_cases = []
#     for county in counties:
#         for month in months:
#             num_cases.append(data.get(county, {}).get(month, None))
#     return sum(num_cases)

def getNumCases(data,counties,months):
    numCases = []
    for county in counties:
        for month in months:
            numCases.append(data.get(county).get(month))
    return sum(numCases)

# print(getNumCases(CDCdata, ['Whitman'], ['Apr', 'May', 'Jun']))

# 2. getMonthlyCases(data)  
# Assume, your supervisor asks you to reformat the data and create a dictionary that includes the 
# number of cases for each county, organized by months. For example, when you reformat the above 
# dictionary you will get the following.  
# {'Mar':{'King':2706,'Pierce':460,'Snohomish':1301,'Spokane':147}, 
# 'Apr':{'King':3620,'Pierce':965,'Snohomish':1145,'Spokane':222,'Whitman':7}, 
# 'May':{'King':1860,'Pierce':522,'Snohomish':532,'Spokane':233,'Whitman':5}, 
# 'Jun':{'King':2157,'Pierce':647,'Snohomish':568,'Spokane':794,'Whitman':19}, 
# 'July':{'King':5014,'Pierce':2470,'Snohomish':1540,'Spokane':2412,'Whitman':51}, 
# 'Aug':{'King':4327,'Pierce':1776,'Snohomish':1134,'Spokane':1530,'Whitman':514}, 
# 'Sep':{'King':2843,'Pierce':1266,'Snohomish':811,'Spokane':1751,'Whitman':732}, 
# 'Oct':{'Whitman':278}} 
 
# Define a function getMonthlyCases that reformats the CDC data as described above. Your 
# function should not hardcode the county names and the month abbreviations. 
# (The items in the output dictionary can have arbitrary order.) 

def getMonthlyCases(data):
    dictionary = {}
    for county, log in data.items():
        for month, cases in log.items():
            if month not in dictionary.keys():
                dictionary[month] = {}
            dictionary[month][county] = cases  
    return dictionary

# print(getMonthlyCases(CDCdata))

# 3. mostCases(data)  
# Assume, you would like to find the month that had the maximum total number of new cases in all 
# counties. For example: 
# mostCases(CDCdata) returns ('July', 11487)  
# #i.e., July has the max number of total new cases, which is 11487.  
# Your function definition should not use loops or recursion but use the Python map and reduce 
# functions. You should also use the getMonthlyCases function you defined in part(b). You may 
# define and call helper (or anonymous) functions, however your helper functions should not use 
# loops or recursion. 


def mostCases(data):
    monthly_cases = getMonthlyCases(data)
    sum_log = lambda log: reduce(lambda x, y : x + y, log.values())
    map_helper = lambda t : (t[0], sum_log(t[1]))
    reduce_helper = lambda x,y:x if x[1] >= y[1] else y

    map_result = list(map(map_helper, monthly_cases.items()))
    return reduce(reduce_helper, map_result)
    

# print(mostCases(CDCdata)) 
# 4. Dictionaries and Lists 
# a)  searchDicts(L,k)– 5% 
# Write a function searchDicts that takes a list of dictionaries L and a key k as input and checks 
# each dictionary in L starting from the end of the list. If k appears in a dictionary, searchDicts 
# returns the value for key k. If k appears in more than one dictionary, it will return the one that it 
# finds first (closer to the end of the list). 
# For example: 
# L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}] 
 
# searchDicts(L1,"x") returns 2 
# searchDicts(L1,"y") returns False 
# searchDicts(L1,"z") returns "found" 
# searchDicts(L1,"t") returns None 
 
# You can start with the following code:  
def searchDicts(L,k):  
    for dictionary in reversed(L):
        if k in dictionary:
            return dictionary[k]
    return None

# print(searchDicts(L1,"z"))
# print(searchDicts(L1,"t"))
# print(searchDicts(L1,"x"))

# b)  searchDicts2(tL,k) – 10% 
# Write a function searchDicts2 that takes a list of tuples (tL) and a key k as input. Each tuple in 
# the input list includes an integer index value and a dictionary. The index in each tuple represent a 
# link to another tuple in the list (e.g. index 3 refers to the 4th tuple, i.e., the tuple at index 3 in the list)  
# searchDicts2 checks the dictionary in each tuple in tL starting from the end of the list and 
# following the indexes specified in the tuples.  
# For example, assume the following: 
# [(0,d0),(0,d1),(0,d2),(1,d3),(2,d4),(3,d5),(5,d6)] 
#    0       1      2      3      4      5      6 
# The searchDicts2 function will check the dictionaries d6,d5,d3,d1,d0 in order (it will skip 
# over d4 and d2) The tuple in the beginning of the list will always have index 0.  
#  It will return the first value found for key k. If k is couldn’t be found in any dictionary, then it will 
# return None.  
 
# For example:  
L2 = [(0,{"x":0,"y":True,"z":"zero"}),       
     (0,{"x":1}), 
     (1,{"y":False}), 
     (1,{"x":3, "z":"three"}), 
     (2,{})]
  
# searchDicts2 (L2,"x") returns 1 
# searchDicts2 (L2,"y") returns False 
# searchDicts2 (L2,"z") returns "zero" 
# searchDicts2 (L2,"t") returns None 

# (Note: I suggest you to provide a recursive solution to this problem.  
# Hint: Define a helper function with an additional parameter that hold the list index which will be 
# searched in the next recursive call.)  
# You can start with the following code: 
 


def searchDicts2helper(tL, k, ind):
    # check the dictionary at tL[ind]
    if k in tL[ind][1]:
        return tL[ind][1][k]
    # else reach beginning of list
    elif ind == 0:
        return None
    # else make recursive call for index tL[ind][0]
    else:
        return searchDicts2helper(tL, k, tL[ind][0])

def searchDicts2(L,k):
    return searchDicts2helper(L, k, len(L)-1)


# 5. getLongest(L) – 10% 

# Write a function, getLongest, which takes an arbitrarily nested list of strings (L) and it returns the 
# longest string in L. Note that the longest string can be found at any nesting level, so your function should 
# recursively check all sublists. You should not assume a max depth for the nesting. If there are more than 
# one string that have the max length, you should return the one that appears earlier in the list.  
# For example: 
# getLongest(['1',['22',['333',['4444','55555',['666666']],'7777777'],'4444'],'22']) 
# returns '7777777' 
# getLongest([['cat',['dog','horse'],['bird',['bunny','fish']]]])  
# returns 'horse' 
# You can start with the following code: 

def getLongest (L): 
    # define helper get_longer which will return longet of the given two strings
    def getLonger(input1, input2):
        pass
    longest = ''
    for item in L:
        pass
    # if item is a list make a recursive call on item and then compare the value recursive call returns
    if isinstance (item, list):
        longest = getLonger(longest, getLongest(item))
    else:
        pass
    return longest


# 6. Iterators 
# apply2nextN()– 20% 
# Create an iterator that represents the aggregated sequence of values from an input iterator. The iterator 
# will be initialized with a combining function (op), an integer value (n) , and an input iterator (input).  
# When the iterator’s __next__() method is called, it will combine the next “n” values in the “input“  
# by applying the “op” function and it will return the combined value. The iterator should stop when it 
# reaches the end of the input sequence. If the input sequence is infinite, the apply2nextN will return an 
# infinite sequence as well.  
# For example:    
 
# iSequence = apply2nextN(lambda a,b:a+b, 3, iter(range(1,32))) 
# # iSequence represents the sequence [6, 15, 24, 33, 42, 51, 60, 69, 78, 87, 31] 
 
# iSequence.__next__()   # returns 6 
# iSequence.__next__()   # returns 15 
# iSequence.__next__()   # returns 24 
# rest = [] 
# for item in iSequence: 
#    rest.append(item)  
# # rest is [33, 42, 51, 60, 69, 78, 87, 31] 
 
# strIter =iter('aaaabbbbccccddddeeeeffffgggghhhhjjjjkkkkllllmmmm') 
# iSequence = apply2nextN(lambda a,b:a+b, 4, strIter) 
# iSequence.__next__()   # returns 'aaaa' 
# iSequence.__next__()   # returns 'bbbb' 
# iSequence.__next__()   # returns 'cccc' 
# rest = [] 
# for item in iSequence: 
#     rest.append(item) 
# # rest is ['dddd','eeee','ffff','gggg','hhhh','jjjj','kkkk','llll','mmmm'] 
# You can start with the following code: 
 
class applyNextN(object):
    def __init__(self, op, n, input):
        self.input = input
        self.op = op
        self.current = self._getNextInput()

    def _getNextInput(self):
        try:
            self.current = self.input.__next__()
        except:
            self.current = None
        return self.current

    def __next__(self):
        localN = self.n
        if self.current is None:
            raise StopIteration
        total = self.current
        self.current = self._getNextInput()
        while(localN > 1):
            if self.current is not None:
                total = self.op(total, self.current)
            else:
                break
            localN -= 1
            self.current = self._getNextInput()
        return total


    def __iter__(self):
        return self