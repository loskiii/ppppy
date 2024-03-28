import itertools

games = 17
outcomes = ['1', 'X', '2']

for possibility in itertools.product(outcomes, repeat=games):
    print(possibility)
 