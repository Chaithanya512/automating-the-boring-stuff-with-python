import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'heads'
if toss == 1:
    toss = 'tails'

if toss == guess:
    print('You got it right!')
else:
    print('Nope! guess again:')
    guess = input()
    if toss == guess:
        print('you got it right!')
    else:
        print('nooo,you suck at this game :)')
