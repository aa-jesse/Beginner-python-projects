import random

def guess(x):
    randomNumber=random.randint(1,X)
    guess=0
    while guess !=randomNumber:
        guess = int(input(f'guesss a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Sorry, try again your guess was low')
        elif guess > randomNumber:
            print('Try again, your guess was above the number')
    print('Congrats, your guess was right')




