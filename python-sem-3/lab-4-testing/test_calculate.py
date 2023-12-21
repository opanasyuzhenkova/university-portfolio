from main import calculate
#python -m test_calculate -v

def test_sum():
  assert calculate(1, 4, "+", '0.01') == 5, "Should be 5"
def test_sum_2():
  assert calculate(1, 3, "+", '0.01') == 5, "Should be 5"
def test_subtraction():
  assert calculate(3, 2, "-", '0.01') == 1, "Should be 1"
def test_multipl():
  assert calculate(2, 3, "*", '0.01') == 6, "Should be 6"
def test_power():
  assert calculate(2, 1, "**", '0.01') == 2, "Should be 2"
def test_div():
  assert calculate(16, 8, "/", '0.01') == 2, "Should be 2"
def test_ost():
  assert calculate(16, 9, "%", '0.01') == 7, "Should be 7"
def test_int_div():
  assert calculate(16, 9, "//", '0.01') == 1, "Should be 1"
def type_operands():
  assert type(calculate(16.01,9.01,'+','0.01' ))== float,"Type should be int"


if __name__=="__main__":
  test_sum()
  test_sum_2
  test_subtraction()
  test_multipl()
  test_power()
  test_div()
  test_ost()
  test_int_div()
  type_operands()
  print("Everything passed")