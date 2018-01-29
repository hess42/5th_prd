def ipd4(my_score, enemy_score, my_history, enemy_history):  
    if my_score - enemy_score >=2000:
        collude()
    else:
        betray()
def collude():
    print 'c'
def betray():
    print 'b'