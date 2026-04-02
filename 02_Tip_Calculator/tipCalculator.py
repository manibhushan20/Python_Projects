print("Welcome to the Tip Calculator!!")

# float() allows for decimals, like 150.50
bill = float(input("What was the total bill?\n$")) 

# Removed the print() from inside the input()
tipPercent = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
peoples = int(input("How many people to split the bill?\n"))

cost = bill * (1 + tipPercent / 100)
split = cost / peoples

# The :.2f forces the result to always show exactly 2 decimal places
print(f"Each person should pay: ${split:.2f}")