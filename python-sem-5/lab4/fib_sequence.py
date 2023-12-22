# ЗАДАНИЕ 4

def fib_sequence():
  a = 0
  b = 1
  yield a
  while True:
    yield b
    a, b = b, a + b


g = fib_sequence()

li = []
while True:
  el = next(g)
  li.append(el)
  if el > 50:
    break

#print(li)
