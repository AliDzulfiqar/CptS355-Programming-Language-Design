builtin_operator = {
    "add" : lambda x,y : x + y,
    "sub" : lambda x,y : x - y
}

name = "sub"
name in builtin_operator
print(builtin_operator[name](2,3))