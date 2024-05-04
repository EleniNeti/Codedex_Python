stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(day):
  print (f"The stock price for day {day+1} is : {stock_prices[day]}")

price_at(0) # Remember Python is 0-indexed

def max_price(day_1, day_2):
  interval = stock_prices[day_1 : day_2 +1]
  print (f"The maximum stock price from day {day_1 + 1} to day {day_2 + 1} is: {max(interval)}")

max_price(0,9)

def min_price(day_1, day_2):
  interval = stock_prices[day_1 : day_2 +1]
  print (f"The minimum stock price from day {day_1 + 1} to day {day_2 + 1} is: {min(interval)}")

min_price(1, 6)