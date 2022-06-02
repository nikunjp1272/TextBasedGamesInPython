import random
print('Hello, What is your name?')
try:
  name=input()
  print(str(name)+', can you guess the number of the alphabet I am thinking of?')

  secretAlphabet = random.randint(1,27)
  for guessesTaken in range(1,10):
    print('Can you guess it?')
    guess=int(input())
    if guess < secretAlphabet:
        print('Your guess is lower than the number')
    elif guess > secretAlphabet:
        print('Your guess is higher than the number')
    else:
        break
except:
  print('Please enter a number: ')
if guess == secretAlphabet:
    print('You nailed it '+ str(name)+'. It took you '+str(guessesTaken)+' tries to beat the challenge')
else:
    print('Sorry, the number was '+str(secretAlphabet))
print('You took '+str(guessesTaken)+ ' guesses.')
