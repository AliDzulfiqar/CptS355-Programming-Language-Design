# Class exercise

# loop solution, sort second value using lambda
def histo(sentence):
    d = {}
    for c in sentence:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    return sorted(list(d.items()), key = lambda t:t[1], reverse=True)

# loop solution with get
def histo2(sentence):
    d = {}
    for c in sentence:
        d[c] = d.get(c, 0)+1
    return sorted(list(d.items()))

# insert every i value form string as a member of list
lst = [i for i in "implemented"]

# list comprehension solution for histo, use set to eliminate dupes
def histo3(sentence):
    output = [(c, sentence.count(c)) for c in sentence]
    return sorted(list(set(output)), key= lambda t:t[1], reverse=True)


# game scores 
def game_scores(games, opponent):
    scores = []
    # iterate over game logs for each year
    for log in games.values():
        # iterate over team, score pairs
        for team, score in log.items():
            # if the team is same as the given opponent team, add the score to output
            if (team == opponent):
                scores.append(score)
    return scores

# other implementation
def game_scores2(games, opponent):
    scores = []
    # iterate over game logs for each year
    for log in games.values():
        # iterate over team, score pairs
        for team in log:
            # if the team is same as the given opponent team, add the score to output
            if (team == opponent):
                scores.append(log[team])
    return scores