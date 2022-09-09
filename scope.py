# Variable Scope
# LEGB: local, enclosing function, global, builtin

name = 'Peter'

def read_name(name):
  print(name)

read_name(name)

name = 'Jack'

read_name(name)

# global variables

x = 'Accountant'

print(f'x is {x}')

# local reassignment

def change_var(value):
  x = 'changed'

  print(f'local reassignment to {x}')

change_var('wooot')

# global reassignment

def change_global(value):
  global x

  x = 'changed global'

change_global('global changed')
  
print(f'x is now {x}')