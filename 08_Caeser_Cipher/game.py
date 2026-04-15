from art import logo

print(logo)



def encrypt(original_text, shift_amount):
    str=""
    extra=""
    for i in range(len(original_text)):
      idx = ord(original_text[i]) - ord('a')

      if idx<0 or idx>25:
         extra+=original_text[i]
      else:
        idx = (idx+shift_amount)%26
        str+= chr(ord('a') + idx)

    print(f"Your decrypted message: {str+extra}")

def decrypt(original_text, shift_amount):
    str=""
    extra=""
    for i in range(len(original_text)):
      idx = ord(original_text[i]) - ord('a')
      if idx<0 or idx>25:
         extra+=original_text[i]
      else:
         idx = (idx-shift_amount)%26
         str+= chr(ord('a') + idx)

    print(f"Your decrypted message: {str+extra}")



def caeser(func, text, shift):
  if(func=="encode"):
    encrypt(text, shift)
  else:
    decrypt(text, shift)


flag=True
while(flag):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(direction, text, shift)
  next=input("Type 'yes' if you want to go again. Otherwise, type 'no': ")
  if(next=="no"):
     flag=False
     
   

  







# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.



