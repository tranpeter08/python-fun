number_list = [4,8,99]
continue_swap = True

def swap_item(number_list):
  acceptable_range = range(0, len(number_list) - 1)
  is_valid_input = False

  while (is_valid_input == False):
    swap_another = False

    print(f'The current list is: {number_list}')
    user_choice = input('Select an index: ')

  # validate if integer
    if (user_choice.isdigit() == False):
      print('Choose a valid integer')
      continue

    index = int(user_choice)

  # validate if in range
    if (index not in acceptable_range):
      print('Index is out of bounds')
      continue

    # get user input for value

    user_value = input(f'What should the value at {index} be replaced with? ')

    if (user_value.isdigit() == False):
      print('Choose a valid integer')
      continue
    
    number_list[index] = int(user_value)
    print(f'Your new list: {number_list}')



    is_valid_input = True

swap_item(number_list)

while (continue_swap == True):
  user_resp = input('Would you like to swap another item (y/n)? ')

  if (user_resp == 'y'):
    swap_item(number_list)
    continue

  if (user_resp == 'n'):
    print('Goodbye!')
    continue_swap = False
    continue

  print('Please enter "y" or "n"')
