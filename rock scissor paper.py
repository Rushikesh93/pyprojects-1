import random
def play():
    user = input(" r for rock, s for scissor , p for paper\n")
    comp = random.choice(['r','p','s'])
    print(comp)

    if user == comp :
        return "tie"
    if is_win(user,comp):
        return "you win"
    return 'you lost'


def is_win(player,opponent):
    #r>s,s>p,p>r
    if (player == 'r' and opponent == 's') or (player=='s' and opponent == 'p') or (player =='p' or opponent == 'r'):
        return True

print(play())