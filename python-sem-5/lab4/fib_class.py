# ЗАДАНИЕ 2

import fib

class FibonacchiLst():
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
          try:
            res = self.instance[self.idx]
            print(res)
          except IndexError:
            raise StopIteration

            
          if res in fib.fib(len(self.instance)):
              self.idx += 1 
              return res
          else:
            self.idx += 1 