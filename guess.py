guess = 0
tries = 0

while guess != 6 and tries <= 4:
  tries = tries + 1
  guess = int(input("Guess the number: "))

if tries == 5:
  print("You have reached your maximum number of trials.")
else:
  if guess == 6:
    print("You got it!")