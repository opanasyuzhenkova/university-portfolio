import time
import requests
from xml.etree import ElementTree as ET


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls].get_currencies()
        return cls._instances[cls]


class CurrenciesList(metaclass=Singleton):
    def __init__(self):
        self.state = False  # function was called?
        self.t = time.time()
        self.rates = None
        print('Creating object of CurrenciesList...')

    def get_currencies(self, currencies_ids_lst=None) -> dict:
        """The function returns a dict-object with exchange rates

        Keyword arguments:
            currencies_ids_lst --- list of currencies to get 
            the exchange rate
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

    def __del__(self):
        print('Destructor is called...')


curlst = CurrenciesList()
print(type(curlst.get_currencies()))
print(id(curlst))

x = CurrenciesList()
print(id(x))

y = CurrenciesList()
print(id(y))