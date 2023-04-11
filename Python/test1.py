# List creation


myList = [3,1,2*2,1,10/2,10-1]
print(myList)

# List querying
# single element
print(myList[0])

# sublist 
print(myList[:])
print(myList[0:2])

# append
myList.append(2)

# extend
myList2 = myList
myList.extend(myList2)
print(myList)

# insert(i, x) - insert item x before position i
myList.insert(2, 3)
print(myList)

# list replacement
print(myList[:1])