# Funny little game "Guess the number". 
# Our number is 6.
# The user has 5 tries to guess correctly the number.

guess = 0
tries = 0

while guess != 6 and tries <= 4:
  tries = tries + 1
  guess = int(input("Our number lies between 1 and 10. You have 5 tries.\n Guess the number: "))

if tries == 5:
  print("You have reached your maximum number of trials.")
else:
  if guess == 6:
    print("You got it!")
