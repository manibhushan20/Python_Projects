import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

vec = [rock, paper, scissors]


print("Welcome to Rock, Paper, Scissors!")

user_choice  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print("You chose: ")
    print(vec[user_choice])
    print("Computer chose: ")
    print(vec[computer_choice])

if user_choice == computer_choice:
  print("It's a draw!")
elif user_choice == 0:
  if computer_choice == 1:
    print("You Lost!")
  else:
    print("You Won!")
elif user_choice == 1:
  if computer_choice == 2:
    print("You Lost!")
  else:
    print("You Won!")
elif user_choice==2: 
  if computer_choice == 0:
    print("You Lost!")
  else:
    print("You Win!")
else:
  print("Invalid Number!")



