from fib import fib
import test_fib
import fib_class
from fib_iter import fib_iter
from fib_sequence import fib_sequence

if __name__ == '__main__':
  #print(fib(20))

  # test_fib.test_fib_1()
  # test_fib.test_fib_2()

  print(list(range(21)))
  print(list(fib_class.FibonacchiLst(range(21))))

  #print(fib_iter(range(9)))

  #g = fib_sequence()
