import unittest
from main import Currency


class TestCurrency(unittest.TestCase):
  
  def setUp(self):
    self.currency = Currency()

  def test_set_currency(self):
    self.assertEqual(self.currency.set_currency('R9999'), {'R9999': None})

    

if __name__ == '__main__':
    unittest.main()