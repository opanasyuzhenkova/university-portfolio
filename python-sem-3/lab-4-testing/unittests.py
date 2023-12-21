import unittest
from main import calculate
from main import deviation
from main import convert_precision
from main import two_sum

#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase

#python -m unittest unittests -v
class test_calculate(unittest.TestCase):

  def test_norm_results(self): 
      self.assertEqual(calculate(4, 7,'+','0.0'), 11)
      self.assertEqual(calculate(3, 2,'-','0.0'), 1)
      self.assertEqual(calculate(3.1, 2.1,'-','0.1'), 1.0)
      self.assertEqual(calculate(3.2, 2.2,'*','0.1'), 7.0)
      self.assertEqual(calculate(3.2, 2,'**','0.1'), 10.2)
      self.assertEqual(calculate(4.2, 2,'/','0.1'), 2.1)
      self.assertEqual(calculate(6, 2,'%','0.1'), 0.0)
      self.assertEqual(calculate(6.5, 2,'//','0.1'), 3)
     #self.assertRaises(ZeroDivisionError, calculate, 5.1,0,'/',0.1)
     #self.assertRaises(ZeroDivisionError, calculate, 5.1,0,'//',0.1)
     #self.assertRaises(ZeroDivisionError, calculate, 5.1,0,'%',0.1)

  def test_type_error_raises(self):
        with self.assertRaisesRegex(ZeroDivisionError, 'Вы пытаетесь разделить на 0!'):
            calculate(5.1,0,'/',0.1)


class test_deviation(unittest.TestCase):

  def test_norm_results(self):  
     self.assertEqual(deviation(*[1.1234,5.1234,3.1234],precision = '0.0001'), 1.6330)
     self.assertEqual(deviation(*[1,5,3],precision = '0.01'), 1.63)


class test_convert_precision(unittest.TestCase):

  def test_convert_precision_str(self):  
     self.assertEqual(convert_precision('0.0001'), 4)
     self.assertEqual(convert_precision('1e-05'), 5)

  def test_convert_precision_float(self):
        self.assertEqual(convert_precision(0.001), 3)
  
  def test_type_error_raises(self):
        with self.assertRaisesRegex(AssertionError, 'Неверный тип точности!'):
            convert_precision('0.000001a')
    

class test_two_sum(unittest.TestCase):

  def test_two_sum(self):  
     self.assertEqual(two_sum([1,2,3,4,5,6,7,8,9], 8),(0,6))
     self.assertEqual(two_sum([9,1,3,4,5,7,6,8,2], 8), (1,5))
     self.assertEqual(two_sum([1,1,2,4,5,3,6,9,7,8],8),(0,8))
  
# Executing the tests in the above test case class
if __name__ == '__main__':
    unittest.main(verbosity=1)  # запуск тестов
