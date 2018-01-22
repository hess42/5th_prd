####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'f' or 'd'
####

team_name = 'E2'
strategy_name = 'Alternate'
strategy_description = 'Foreshadowing, then different.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (f or d) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[1]
    The most recent round is my_history[0] and their_history[0]
    
    Returns 'f' or 'd' for collude or betray.
    '''
    # This player colludes on even numbered rounds (first round is round #0).
    if len(my_history)%8 == 0:
        return 'f'
    else:
        return 'd'
    