import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"IS {guess} too high, too low(L),or correct(c)".lower())
        if feedback == 'h':
            high = guess-1
        if feedback == 'l':
            low = guess+1

    print(f'correct guess is {guess}')


comp_guess(10)