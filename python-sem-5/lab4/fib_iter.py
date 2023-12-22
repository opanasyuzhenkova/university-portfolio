# ЗАДАНИЕ 3

from itertools import takewhile
import fib

def fib_iter(iterable_object):
  n = len(iterable_object)
  li = []
  for i in takewhile(lambda x: x < n, fib.fib(n)):
      li.append(i)
  return li