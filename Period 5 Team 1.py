####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E4'
strategy_name = 'Use early history'
strategy_description = '''\
Collude first round. Compare all rounds to the previous round and 
assume opponent will behave the same as the first time the previous 
round's result occurred. If the previous round's result never has 
happened, collude except after being severly punished.'''
    

    '''
def ipd4(my_score, enemy_score, my_history, enemy_history):  
    if my_score - enemy_score >=2000:
        collude()
    else:
        betray()
def collude():
    print 'c'
def betray():
    print 'b'