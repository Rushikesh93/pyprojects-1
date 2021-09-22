import random
def guess(x):
    computer = random.randint(1, x)
    guess = 0
    while guess != computer:
        guess = int(input(f"guess the number : "))
        if guess<computer:
            print("guess is too low")
        elif guess> computer:
            print("guess is too high")
    print("congrates your guess is right")


guess(10)