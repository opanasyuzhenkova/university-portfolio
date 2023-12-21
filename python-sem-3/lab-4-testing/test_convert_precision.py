from main import convert_precision
#python -m test_convert_precision -v

def res_precision():
  assert convert_precision('0.0001') == 4, "Should be 4"
  assert convert_precision('1e-05') == 5,'Should be 5'

def type_precision():
  assert type(convert_precision('0.0001'))==int,"Type should be int"

if __name__=="__main__":
  res_precision()
  type_precision()
  print("Everything passed")