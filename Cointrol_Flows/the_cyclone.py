# Write code below 💖

height = int(input('Input your Height (cm): '))
credits = int(input('Input your Credits: '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print('You dont have enough credits.')
else:
  print('You did not met either requirement')