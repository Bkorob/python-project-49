

from random import randint


a =(1, 2, 3, 4, 5, 6, 7, 'вы выиграли в лотырею')

def rand_tuple(a):
  tupl_index = randint(0, len(a) - 1)
  result = a[tupl_index]
  if result != a[-1]:
    print(rand_tuple(a))

  return result

rand_tuple(a)kkk