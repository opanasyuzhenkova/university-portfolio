from main import two_sum
#python -m test_two_sum -v

def test_two_sum():
  assert two_sum([1,2,3,4,5,6,7,8,9], 8) == (0,6), "Should be (0,6)"
def test_two_sum_unsorted_list():
  assert two_sum([9,1,3,4,5,7,6,8,2], 8) == (1,5), "Should be (1,5)"
def test_repeated_operands():
  assert two_sum([1,1,2,4,5,3,6,9,7,8],8) == (0,8), "Should be (0,8)"
  
if __name__=="__main__":
  test_two_sum()
  test_two_sum_unsorted_list()
  test_repeated_operands()
  print('Everything passed')