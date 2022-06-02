import random
def play():
  user_input=input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizard and 'c' for spock ")
  computer=random.choice(['r','p','s','l','c'])
  if computer==user_input : 
    print('It is a tie')
#s>p, p>r, r>l, l>c, c>s, s>l,  l>p, p>c, c>r, r>s
  if is_win(user_input, computer):
    print('You Win')
  print('You Lost') 
def is_win(pl, op):
  if (pl=='r' and op=='s') or (pl=='s' and op=='p') or (pl=='p' and op=='r') or (pl=='r' and op=='l') or (pl=='l' and op=='c') or (pl== 'c' and op== 's') or (pl=='s' and op=='l') or (pl=='l' and op=='p') or (pl=='p' and op=='c') or (pl=='c' and op=='r'):
   return True
print(play())
