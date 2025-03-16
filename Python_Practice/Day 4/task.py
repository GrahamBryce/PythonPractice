# print("Hi Welcome to the roller coaster")
# height = int(input("How tall are you"))

# bill = 0

# if height >= 120:
#   print("congrats")
#   age=int(input("What is your age? "))
#   if age <= 18:
#     print("you only have to pay 7")
#     bill = 7
#   elif age <= 12:
#     print("$5")
#     bill = 5
#   else:
#     print("20 bucks")
#     bill = 20
#   wantsPicture = input("do you want a photo? y for yes, n for no")
#   if wantsPicture == "y":
#     bill+= 3
#     print(f"your bill is {bill}")
# else:
#   print("You too short")

import random

# randomInteger = random.randint( 1, 10)
# print(randomInteger)

family = ['wendy', 'lotus', 'honey', 'dean', 'christian']

randomNum = random.randint(0, 4)

if randomNum == 0:
  print(family[0])
elif randomNum == 1:
  print(family[1])
elif randomNum == 2:
  print(family[2])
elif randomNum == 3:
  print(family[3])
else:
  print(family[4])
  # or
# print(random.choice(family))