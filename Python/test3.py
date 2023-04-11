# Higher order functions

# Map/transform - Apply operation towards every values in list
def sq(x):
    return x**2

L = [i for i in range(0,5)]

map(sq, L)



# Filter - Takes out value that doesn't apply to list bool
filter((lambda x: x>0), [-4,3,1,-2,3,-5,1,9,0])


# Reduce - Similar to Foldr/Foldl, base not necessary
from functools import reduce
reduce(min, [-1,-2,-3,-4,-5])

# use base
reduce(min, [-1,-2,-3,-4,-5]), 0

# Histo using HOF
def histo4(sentence):
    get_tuple = lambda c: (c, sentence.count(c))
    output = map(get_tuple, sentence)
    return sorted(list(set(output)), key = lambda t:t[1], reverse=True)

# re-implement game scores using HOF

# get score from each log in the data using get_score function and map use get score as helper that takes a log and return the score
def game_scores3(games, opponent):
    get_score = lambda log: log.get(opponent)
    remove_none = lambda x: x is not None
    return list(filter (remove_none, map(get_score, games.values())))

