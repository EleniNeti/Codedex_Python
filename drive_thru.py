menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

# create the welcome menu

def welcome():
  print(f"Welcome at Mac n' Cheese! Take a look at our dishes: \n #1 {menu[0]} 5.5$ \n #2 {menu[1]} 3$ \n #3 {menu[2]} 1.5$ \n #4 {menu[3]} 2$ \n #5 {menu[4]} 1$")


# create the order process

def get_item(order):
  if order == len(menu) - 4:
    print(f"We received your order! Your {menu[0]} will be ready in a few minutes.")
  elif order == len(menu) - 3:
    print(f"We received your order! Your {menu[1]} will be ready in a few minutes.")
  elif order == len(menu) - 2:
    print(f"We received your order! Your {menu[2]} will be ready in a few minutes.")
  elif order == len(menu) - 1:
    print(f"We received your order! Your {menu[3]} will be ready in a few minutes.")
  elif order == len(menu):
    print(f"We received your order! Your {menu[4]} will be ready in a few minutes.")
  else:
    print(f"Wrong input. The item doesn't exist in the menu.")


welcome()

order = int(input("Order your meal here by typing its menu number: "))

get_item(order)