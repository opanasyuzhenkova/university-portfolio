from package import calculate as cl

def test_sum():
  assert cl.calculate(1, 4, "+", '0.01') == 5, "Should be 5"

  
def test_sum_2():
  assert cl.calculate(1, 3, "+", '0.01') == 4, "Should be 4"

  
def test_subtraction():
  assert cl.calculate(3, 2, "-", '0.01') == 1, "Should be 1"

  
def test_multipl():
  assert cl.calculate(2, 3, "*", '0.01') == 6, "Should be 6"

  
def test_power():
  assert cl.calculate(2, 1, "**", '0.01') == 2, "Should be 2"

  
def test_div():
  assert cl.calculate(16, 8, "/", '0.01') == 2, "Should be 2"

  
def test_ost():
  assert cl.calculate(16, 9, "%", '0.01') == 7, "Should be 7"

  
def test_int_div():
  assert cl.calculate(16, 9, "//", '0.01') == 1, "Should be 1"

  
def type_operands():
  assert type(cl.calculate(16.01,9.01,'+','0.01' ))== float,"Type should be int"

def all_tests():
  test_sum()
  test_sum_2()
  test_subtraction()
  test_multipl()
  test_power()
  test_div()
  test_ost()
  test_int_div()
  type_operands()