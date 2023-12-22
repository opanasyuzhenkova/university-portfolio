from fib import fib

def test_fib_1():
    assert fib(1) == [0, 1], "Тривиальный случай n = 1, список [0, 1]"


def test_fib_2():
    assert fib(4) == [0, 1, 1, 2, 3], "fib(4) должно быть [0, 1, 1, 2, 3]"

if __name__ == '__main__':
    test_fib_1()
    test_fib_2()