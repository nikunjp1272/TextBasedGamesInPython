import random
def comp_guess(x):
  low=1
  high=x
  feedb=''
  while feedb != 'c':
      if low!=high:
        guess=random.randint(low,high)
      else:
        guess=low
      feedb=input(f'Is the {guess} too high (H), too low (L) or correct (C)??').lower()
      if feedb=='h':
        high=guess-1
      elif feedb=='l':
        low=guess+1
  print(f'Your guessed number is {guess}')

comp_guess(10000)

#Another approach
#Uncomment the code below by removing the --> ''' symbols at the beginning and end
'''
#Importing the random library for selecting a random number
import random

#defining a function by the name of guess

def guess(x):
#choosing a number randomly from 1 to x
  random_n=random.randint(1,x)
  guess=0
#run a while loop to check if the number is equal to the guess, if not return low or high acoordingly
  while guess!=random_n:
    guess=int(input(f'Guess the n between 1 and {x}: '))
    print(guess)
    if guess < random_n:
       print('Too low')
    elif guess > random_n:
      print('Too high')
#print this after the number=guess
  print('You guessed the number correctly')
guess(100)
'''
