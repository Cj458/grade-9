import random

player1 = input('Select Rock, Paper or Scissor: ').lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()



time = 0

while True:

    print(f'Computer has selected: {computer}')

    if player1 == 'rock' and computer == 'paper':
        print('Computer won')

    elif player1 == 'paper' and computer == 'scissor':
        print('Computer won')

    elif player1 == 'scissor' and computer == 'rock':
        print('Computer won')

    elif player1 == computer:
        print('Tie')

    else:
        print('You Won')

    res = input("Again...?").lower()

    if res == 'n':
        break

    