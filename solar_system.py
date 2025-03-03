# Write code below 💖

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
  r = 2440
  print(f"The Area of {random_planet} is = {4 * pi * r**2}")
elif random_planet == 'Venus':
  r = 6052
  print(f"The Area of {random_planet} is = {4 * pi * r * r}")
elif random_planet == 'Earth':
  r = 6371
  print(f"The Area of {random_planet} is = {4 * pi * r * r}")
elif random_planet == 'Mars':
  r = 3390
  print(f"The Area of {random_planet} is = {4 * pi * r * r}")
elif random_planet == 'Saturn':
  r = 58232
  print(f"The Area of {random_planet} is = {4 * pi * r * r}")
else:
  print("Oops! An error occurred.")
