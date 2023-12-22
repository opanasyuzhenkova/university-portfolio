# ЗАДАНИЕ 1

def fib(n):
  """
    Список чисел ряда Фибоначчи 
    Возвращает значения не превосходящие данное n
  """
  fib1 = 0
  fib2 = 1
  li = [fib1, fib2] 
  i = 1
  while fib1 + fib2 <= n:
    if n == 1:
      return li
    else:
      fib1, fib2 = fib2, fib1 + fib2
      li.append(fib2) 
      i += 1
    
  return li