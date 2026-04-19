from art import logo

print("               WELCOME TO CALCULATOR PROJECT             ")

print(logo)

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b


op={
"+" : add,
"-": subtract,
"*":multiply,
"/": divide
}


def calculator():

  a = int(input("\nEnter the first number: "))
  b = int(input("Ener the second number: "))
  for symbols in op:
    print(symbols)

  opr = input("Enter the operations from given symbols: ")

  print(f"Result: {op[opr](a, b)}\n")

  ok = input("Do you want to continue 'Y' for yes and 'N' for no: ")

  if ok == 'N':
    return
  else:
    calculator()
  
calculator()

print("\nYour journey ends here!")