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
---'    ____)____
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

# print("Rock:", rock)
# print("Paper:", paper)
# print("Scissors:", scissors)
opponent = int(input("type 0 for rock, 1 for scissors or 2 for paper "))
me = [rock,paper,scissors]
meRandomChoice = random.choice(me)

if opponent == 0:
  opponent = rock
elif opponent == 1:
  opponent = scissors
else:
  opponent = paper

if opponent == rock and meRandomChoice == paper:
  print("you lose", paper)
elif opponent == rock and meRandomChoice == scissors:
  print(scissors, "you win")
elif opponent == rock and meRandomChoice == rock:
  print(rock, "draw")
elif opponent == paper and meRandomChoice == scissors:
  print("you lose", scissors)
elif opponent == paper and meRandomChoice == rock:
  print(rock, "you win")
elif opponent == paper and meRandomChoice == paper:
  print(rock, "draw")
elif opponent == scissors and meRandomChoice == rock:
  print("you lose", rock)
elif opponent == scissors and meRandomChoice == paper:
  print(rock, "you win")
elif opponent == scissors and meRandomChoice == scissors:
  print(rock, "draw")
