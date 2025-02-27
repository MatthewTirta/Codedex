# Write code below 💖

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x]

def max_price(a, b):
  return stock_prices[max(a, b)]

def min_price(a, b):
  return stock_prices[min(a,b)]

x = int(input("Input Which Date To See (number only 0-30): "))

print(f"Price Stock at {x} Jan 2023: {price_at(x)}")
print(f"Max Stock between 1 to 10 Jan 2023: {max_price(1, 10)} ")
print(f"Min Stock between 1 to 10 Jan 2023: {min_price(1, 10)} ")
