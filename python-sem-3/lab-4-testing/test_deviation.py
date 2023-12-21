from main import deviation
#python -m test_deviation -v

def test_deviation():
  assert deviation(*[1,5,3], precision = '0.01')==1.63, "Should be 1.63"

def test_deviation_float():
  assert deviation(*[1.1234,5.1234,3.1234], precision = '0.0001')==1.6330, "Should be 1.63"

def type_dev():
  assert type(deviation(*[1,2,3], precision = '0.01'))==float, "Type should be float"


if __name__=="__main__":
  test_deviation()
  type_dev()

  print('Everything passed')