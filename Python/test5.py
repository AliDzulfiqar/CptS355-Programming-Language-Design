wsu_games = {
    2020: {"USC": (13,38), "UTAH": (28,45)},
    2021: {"ARIZ": (44,18), "WASH": (40,13), "CMU": (21,24)}
}

from copy import copy
from unittest import result
def update_dict2(games):
    temp = copy(games)
    del temp[2020]
    temp[2021]["UCLA"] = (20, 40)
    return None

print(wsu_games)
update_dict2(wsu_games)
print(wsu_games)

s = "CptS355"
def f():
    global s
    print(s)
    s = "CptS322"

f()
print(s)

z = 1
def g():
    z = 4
    def h(a):
        z = 10
        return z
    return z + h(19)

result = g()
print("Example 1 - z in main", z)

def demo2():
    L = ['a', 'b', 'c']
    return L

L = [1,2]
print(f"L is {L}")
result = demo2()
print(f"L is {result}")