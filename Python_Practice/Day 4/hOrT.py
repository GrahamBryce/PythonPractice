import random
choice = input("Pick heads or tails ")

coin = 0

randomNum = random.randint(0,1)

if randomNum == 1:
  coin = "head"
else:
  coin = "tails"

if choice == coin:
  print("congrats you win")
else:
  print("you lose. try again?")
