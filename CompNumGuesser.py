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
