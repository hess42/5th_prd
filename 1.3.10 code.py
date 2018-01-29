my_history = 'bc'
their_history = 'cbb'

def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'b'
    if their_history[-1]== 'b'and their_history[-2]== 'b':
        return 'c'
    if len(my_history)>0:
        return 'b'
    
move(my_history,their_history,0,0 )    