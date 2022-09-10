import math

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0

  def deposit(self, amount = 0, description = ''):
    deposit_data = {'amount': amount, 'description': description}
    self.balance += amount
    self.ledger.append(deposit_data)

  def withdraw(self, amount = 0, description = ''):
    has_funds = self.check_funds(amount)
    if not has_funds:
      return False

    deposit_data = {'amount': amount * -1, 'description': description}
    self.ledger.append(deposit_data)
    self.balance -= amount

    return True
    
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction['amount']

    return balance    

  def transfer(self, amount, Budget):
    has_funds = self.check_funds(amount)

    if not has_funds:
      return False

    trx = {'amount': amount * -1, 'description': f'Transfer to {Budget.category}'}
    Budget.deposit(amount, f'Transfer from {self.category}')
    self.ledger.append(trx)

    return True

  def check_funds(self, amount = 0):
    balance = self.get_balance()

    if (amount > balance):
      return False
    
    return True

  def __str__(self):
    length = len(self.category)
    star_count = 30 - length
    left_count = star_count // 2
    right_count = star_count - left_count
    left_stars = '*' * left_count
    right_stars = '*' * right_count

    def format_amount(amt):
      return  "{:.2f}".format(amt)

    def create_trx_string(trx): 
      amt = format_amount(trx['amount'])
      descr = trx['description']
      space_count = 1
      amt_len = len(amt)
      char_count = 29 - amt_len

      if char_count < len(descr):
        descr = descr[:char_count]
      
      descr_len = len(descr)

      if char_count > descr_len:
        space_count += char_count - descr_len

      space = ' ' * space_count

      return descr + space + amt
        
    formatted_total = format_amount(self.get_balance())

    trxs = []

    for trx in self.ledger:
      print(trx)
      trxs.append(create_trx_string(trx))

    header = f'{left_stars}{self.category}{right_stars}\n'
    mid = '\n'.join(trxs)
    total = f'\nTotal: {formatted_total}'

    return header + mid + total


def create_spend_chart(categories = []):
  chart = 'Percentage spent by category\n'
  chart_arr = []
  total_withdrawals = 0
  category_withdrawals = []
  category_percentages = [] 
  max_label_length = 0
  label_arr = []

  # figure out % of each category
  # collect category labels
  for category in categories:
    # calculate category withdrawals
    withdrawals = 0
    for trx in category.ledger:
      if (trx['amount'] < 0):
        withdrawals += trx['amount']
    total_withdrawals += withdrawals
    category_withdrawals.append(withdrawals)

    #determine max category label length
    label = category.category
    label_length = len(label)

    if (label_length > max_label_length):
      max_label_length = label_length

  # get total withdrawls and divide by each category withdrawls
  # round to nearest tens
  for withdrawal in category_withdrawals:
    percent = int(math.floor(withdrawal / total_withdrawals * 10) * 10)
    category_percentages.append(percent)

  for i in range(10, -1, -1):
    vertical_axis_value = i * 10

    # calculate left offset for vertical axis labels
    offset_count = 3 - len(str(vertical_axis_value))
    offset = ' ' * offset_count

    chart_row = ''

    # determine fill or no fill for cell content
    for percent in category_percentages:
      content = ' '
      
      if vertical_axis_value <= percent:
        content = 'o'

      chart_row += f'{content}  '

    chart_arr.append(f'{offset}{vertical_axis_value}| {chart_row}')
  
  chart += '\n'.join(chart_arr)

  # calculate divider width by amount of categories
  divider_width = len(categories) * 3 + 1

  # offset divider by 4 spaces
  divider = ' ' * 4 + '-' * divider_width
  chart += '\n' + divider

# iterate through index
  for i in range(0, max_label_length):
    # start with left offset 
    row = ' ' * 5

    # determine fill cell content with letter or space
    for category in categories:
      content = ' '
      label = category.category
      label_length = len(label)

      # check for out of bound index
      if i < label_length:
        content = label[i]
      
      row += f'{content}  '

    label_arr.append(row)

  chart += '\n' + '\n'.join(label_arr)
  # print(chart)
  return chart

cat = Category('cat')
cat.deposit(10, 'food')
cat.withdraw(5, 'socks')
cat.withdraw(1.50, 'x'*23 + 'y')

dog = Category('dog')
dog.deposit(5, 'initial')
dog.withdraw(2)
dog.withdraw(1.50)
result = cat.transfer(3, dog)

mouse = Category('mouse')
mouse.deposit(7)
mouse.withdraw(4)
mouse.withdraw(2.75)

result = create_spend_chart([cat, dog, mouse])

print(result)

p = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

print(p)

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

result = create_spend_chart([business, food, entertainment])

print(result)