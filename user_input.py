

is_complete = False
number = 0

def ask_user():
  try:
    return int(input('Enter a number from 1 to 10: '))
  except: 
    print('Needs to be a valid integer!')

while (is_complete == False):
  try:
    acceptable_range = range(0, 10)
    number = int(input('Enter a number '))

    if number not in acceptable_range:
      print('Number out of range')
      continue

    is_complete = True
  
  except:
    print('Needs to be a valid integer!')



print(f'You have chosen {number}')