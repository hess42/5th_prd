def ipd4(my_score, enemy_score, my_history, enemy_history):  
    if my_score - enemy_score >=2000:
        collude()
    else:
        betray()
def collude():
    print 'c'
def betray():
    print 'b'

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.    
        if len(my_history)==0: # It's the first round: collude
                return 'c'
            else:
                # If there was a previous round just like the last one,
                # do whatever they did in the round that followed it
                
                # Reference last round
                recent_round_them = their_history[-1]
                recent_round_me = my_history[-1]
                            
                # Look at rounds before that one
                for round in range(len(my_history)-1):
                    prior_round_them = their_history[round]
                    prior_round_me = my_history[round]
                    # If one matches
                    if (prior_round_me == recent_round_me) and \
                            (prior_round_them == recent_round_them):
                        return their_history[round]
                # No match found
                if my_history[-1]=='c' and their_history[-1]=='b':
                    return 'b' # Betray if they were severely punished last time
                else:
                    return 'c' # Otherwise collude.