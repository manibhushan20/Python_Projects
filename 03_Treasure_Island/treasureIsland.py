print("Welcome to Treasure Island. Your mission is to find the treasure!!")
c1 = input("Choose left or right: ")

if c1 != "left":
  print("Fall into a hole. \nGame Over!")

else:
  c2 = input("Choose swim or wait: ")

  if c2!="wait":
    print("Attacked by trout. \nGame Over!")
  
  else:
    color = input("Choose Red, Yellow and Blue: ")

    if color=="blue":
      print("Eaten by beasts. \nGame Over!")
    elif color=="red":
      print("Burned by fire. \nGame Over!")
    elif color=="yellow":
      print("You Win!")
    else:
      print("Game Over!")




    