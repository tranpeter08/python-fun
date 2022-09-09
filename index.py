import random

answer = random.randint(0, 100)
# print(answer)

isCorrect = False
correct = 69

# while (isCorrect == False):
#   print('Guess a number...')
#   resp = int(input())

#   if resp == correct:
#     isCorrect = True


  # if (resp % 2) != 0:
  #   print('odd')
  # else:
  #   print('even')

# count = 0

# print(count)

# count += 200

# print(count)

hash = {}

list = [1, 2, 3, 1, 2, 3]

for num in list:
  print(hash.get(num))
  if hash.get(num) == True:
    continue

  hash[num] = True

print(hash.keys())


def read_write_files():
  try:
    f = open('sample.txt', 'a')
    with f:
      f.write('\ntest')
  except:
    print('ValueError')
  f.close()

def read_file():
  try:
    with open('sample.txt', 'r') as file:
      for line in file:
        print(line, end='') # 2nd arg set how to handle end of line, defaults to new line


  except:
    print('something went wrong')


def read_file_2():
  try:
    with open('sample.txt', 'r') as file:
      line = file.readline()
      while line:
        print(line, end='') # 2nd arg set how to handle end of line, defaults to new line
        line = file.readline()
  except:
    print('something went wrong')

read_file_2()