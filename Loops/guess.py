# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries += 1

if guess != 6:
  print("You Ran Out Of Tries")
else:
  print("You got it!")