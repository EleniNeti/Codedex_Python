import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  results = random.choices(symbols, k = 3)
  print(f" {results[0]}  | {results[1]}  | {results[2]} ")
  if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("Jackpot! 💰")
  else:
    print("Thanks for playing!")
  answer = input("Do you like to play again? Please insert 'Y' for Yes or 'N' for No: ")
  return answer

player_answer = play()

while player_answer == 'Y':
  player_answer = play()