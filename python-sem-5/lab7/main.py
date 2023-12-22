import json
import time
import requests
from xml.etree import ElementTree as ET
import pandas as pd


class BaseCurrenciesList:

  def get_currencies(self, currencies_ids_lst: list) -> dict:
    pass


class CurrenciesList(BaseCurrenciesList):
  """
    ConcreteComponent
    """

  def __init__(self):
    self.state = False  # function was called?
    self.t = time.time()
    self.rates = None
    print('Creating object of CurrenciesList...')

  def __str__(self):
    return str(self.get_currencies()) 

  def __repr__(self):
    return self.get_currencies()

  def get_currencies(self, currencies_ids_lst=None) -> dict:
    """The function returns a dict-object with exchange rates

      Keyword arguments:
      currencies_ids_lst --- list of currencies to 
        get the exchange rate
                """
    t = time.time()
    result = {}

    if self.state:
      result = self.rates
    if not self.state or (t - self.t >= 1):
      # one request per second
      print(f'get_currencies() call status: {self.state}. New request...')
      if currencies_ids_lst is None:
        currencies_ids_lst = [
          'R01239', 'R01235', 'R01035', 'R01815', 'R01585F', 'R01589',
          'R01625', 'R01670', 'R01700J', 'R01710A'
        ]
      res = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
      cur_res_str = res.text

      root = ET.fromstring(cur_res_str)

      valutes = root.findall("Valute")

      for _v in valutes:
        valute_id = _v.get('ID')

        if str(valute_id) in currencies_ids_lst:
          valute_cur_val = _v.find('Value').text
          valute_cur_name = _v.find('Name').text

          result[valute_id] = (valute_cur_val, valute_cur_name)

      print(result)

      self.state = True
      print(f'get_currencies() call status: {self.state}')
      self.rates = result

    return result


class Decorator(BaseCurrenciesList):
  """
    Decorator
    """

  __wrapped_object: BaseCurrenciesList = None

  def __init__(self, currencies_lst: BaseCurrenciesList):
    self.__wrapped_object = currencies_lst

  @property
  def wrapped_object(self) -> str:
    return self.__wrapped_object

  def get_currencies(self, currencies_ids_lst: list) -> dict:
    return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):
  """ConcreteDecoratorA"""

  def __str__(self):  # JSON
    return str(json.dumps(self.wrapped_object.get_currencies(self), indent=4, ensure_ascii=False))


class ConcreteDecoratorCSV(Decorator):
  """ConcreteDecoratorB"""

  def __str__(self):
    json_info = json.dumps(
      self.wrapped_object.get_currencies(self),
      indent=4,
      ensure_ascii=False)
    print('ConcreteDecoratorCSV: ')
    return str(pd.read_json(json_info).to_csv(sep='\t'))


def show_currencies(currencies_ids_lst):
  #print(currencies.__str__(currencies_ids_lst))
  print(currencies_ids_lst)


# def write_json_file(self, currencies_ids_lst: list = None):
#         print('Currency list also in result.json')
#         with open("result.json", 'w', encoding='utf8') as file:
#             json.dump(self.wrapped_object.get_currencies(currencies_ids_lst), file, ensure_ascii=False)

if __name__ == "__main__":
  curlist = CurrenciesList()
  wrapped_curlist = Decorator(curlist)
  wrapped_curlist_json = ConcreteDecoratorJSON(curlist)
  wrapped_curlist_csv = ConcreteDecoratorCSV(curlist)

  show_currencies(curlist)
  show_currencies(wrapped_curlist_json)
  show_currencies(wrapped_curlist_csv)
