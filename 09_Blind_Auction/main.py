from logo import logo

print("       **************Welcome to the Blind Auction!*************")

print(logo)

flag=True
mp={}

while flag:
  name =  input("Enter your name: ")
  price= int(input("Enter your bidding price: "))
  mp[name]=price
  more =  input("Anyother person wants to bid? Say 'yes' or 'no': ")
  if(more=="no"):
    flag=False
  else:
    print(8*'\n')


person=""
bid=0
for name in mp:
  if mp[name] > bid:
    bid=mp[name]
    person=name


print(f"\nThe highest bid is raised by '{person}' of '{bid}$'.")



