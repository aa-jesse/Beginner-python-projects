import random  # used to import the random module in python


def is_win(player, Ai):  # used define the is win function
    if (player == 'r' and Ai == 's') or (player == 's' and Ai == 'p') \
            or (player == 'p' and Ai == 'r'):
        return True


def play():
    user = input(' r for rock, s for scissor and p for paper:\n ')
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return 'We have a tie'

    if is_win(user, computer):
        return 'You won!!!'

    return 'You lost!'


print(play())
