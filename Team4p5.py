import random
team_name = 'Team 4'
strategy_name = 'Maronne Suck Strat'
strategy_description = 'With the Glasses.'
    
def move(my_history, their_history, my_score, their_score):
    number = random.randint(1,100)
    if number%2 == 0:
            return 'c'
    if number%2 == 1:
            return 'b'