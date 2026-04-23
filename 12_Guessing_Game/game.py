from art import logo
import random


print(logo)
print('\n')

print("                 ********** Guess the Number between 1 and 100 ***********               ")

print('\n')

original = random.randint(1, 100);

level = input("Choose the level :-  'easy' or 'hard':  ")
chances = 10

if level=='hard':
  chances=5

flag = True

while chances>0 and flag:
  print(f"You have {chances} chances remaining!!")
  guess  = int(input("Guess the number: "))
  if guess==original:
    print(f"You won!!")
    flag=False
  elif guess > original:
    chances-=1
    print("Too high number!")
  else:
    chances-=1
    print("Too low number!")


if flag==True:
  print("You Lost!!")
  
