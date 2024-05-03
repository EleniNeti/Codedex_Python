#################################################################
# The following program is an implementation of the Harry Potter#
# sorting hat. The user is asked to answer three different      #
# questions and then is sorted to the revelant Hogwarts house   #
# based on a score calculated according to the answers.         #
# ###############################################################

answer_1 = int(input("Q1) Do you like Dawn or Dusk? \n   1) Dawn \n   2) Dusk \n"))
answer_2 = int(input("Q2) When I'm dead, I want people to remember me as: \n  1) The Good \n  2) The Great \n  3) The Wise \n  4) The Bold \n"))
answer_3 = int(input("Q3) Which kind of instrument most pleases your ear? \n  1) The violin \n  2) The trumpet \n  3) The piano \n  4) The drum \n "))

gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

if answer_1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif answer_1 == 2:
  slytherin = slytherin + 1
  hufflepuff = hufflepuff + 1
else:
  print("Wrong input.")

if answer_2 == 1:
  hufflepuff = hufflepuff + 2
elif answer_2 == 2:
  slytherin = slytherin + 2
elif answer_2 == 3:
  ravenclaw = ravenclaw + 2
elif answer_2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong input.")

if answer_3 == 1:
  slytherin = slytherin + 4
elif answer_3 == 2:
  hufflepuff = hufflepuff + 4
elif answer_3 == 3:
  ravenclaw = ravenclaw + 4
elif answer_3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong input.")

print(f"Total points per house \n gr: {gryffindor}, rav: {ravenclaw}, sl: {slytherin}, huff: {hufflepuff}")

if gryffindor > slytherin and hufflepuff > ravenclaw:
  if gryffindor > hufflepuff:
    print("You are a gryffindor! 🦁")
  else:
    print("You are a hufflepuff! 🦡")
elif gryffindor > slytherin and ravenclaw > hufflepuff:
  if gryffindor > ravenclaw:
    print("You are a gryffindor! 🦁")
  else:
    print("You are a ravenclaw! 🦅")
elif slytherin > gryffindor and hufflepuff > ravenclaw:
  if slytherin > hufflepuff:
    print("You are a slytherin! 🐍")
  else:
    print("You are a hufflepuff! 🦡")
else:
  if slytherin > ravenclaw:
    print("You are a slytherin! 🐍")
  else:
    print("You are a ravenclaw! 🦅")