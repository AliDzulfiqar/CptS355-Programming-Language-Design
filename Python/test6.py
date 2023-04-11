# python generators

def letters(start, finish):
    current = start
    while current <= finish:
        print("before yield")
        yield current
        print("after yield")
        current = chr(ord(current) + 1)

gLetters = letters("a", "d")
print(gLetters.__next__())

for a in gLetters:
    print(a)
list(gLetters)

# use fo iterators
def getCourse(it):
    course = ""
    for c in it:
        if c=='-':
            return course
        else:
            course += c
    return course

i = iter("CptS355-CptS322-CptS321")
course1 = getCourse(i)
course2 = getCourse(i)
course3 = getCourse(i)
print(course1, course2, course3)

# streams
