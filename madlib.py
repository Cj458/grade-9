
age = int(input('How old are you?: '))
game = input('what game do you like to play?: ')
character = input('Enter a character name: ')
adj1 = input('Enter an adjective: ')
name = input('What is your name?: ')




madlib = f"""Once upon a time, there was a {age*2}-year-old coder called {name} who was really interested in {game}.
He wanted to create a new character but the {game} game didn't allow him to.
he then decided to make his own clone of {game} so that he can create his own character named {character}.
the game was really {adj1}, but to play it, you had to be really good, because he had decided to add
extra level of difficulty."""

print(madlib)