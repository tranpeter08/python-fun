items = [1, 5, 9]

def add4(num):
  return num + 4

new_items = list(map(add4, items))

print(new_items)

# lambda functions



print(list(map(lambda num: num + 4, items)))