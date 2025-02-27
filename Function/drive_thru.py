# Write code below 💖

def get_item(x):
  food = ['Cheeseburger', 'Fries', 'Soda', 'Ice Cream', 'Cookie']
  if x == 1:
    return food[0]
  elif x == 2:
    return food[1]
  elif x == 3:
    return food[2]
  elif x == 4:
    return food[3]
  elif x == 5:
    return food[4]
  else:
    return "Error"

def welcome():
  print("Welcome to Matt Fast Food Pick Your Food")
  print("1. Cheeseburger")
  print("2. Fries")
  print("3. Soda")
  print("4. Ice Cream")
  print("5. Cookie")

welcome()
num = int(input("What would you like to order [1-5]: "))
print(get_item(num))
