from bs4 import BeautifulSoup
import requests
tracked_currencies = []

class Currency():
    """Class for receiving and returning currencies"""

    def __init__(self):
        """Constructor"""
        self.url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def __del__(self):
        """Destructor"""
        print("Destructor called")

    def get_currency(self): # receive one currency
        return self.get_rate()[self._v_id]

    def  get_currencies(self): # receive list of currencies
        return self.get_rate()

    def set_currency(self, id): # adding a new currency to the list of tracked currencies
          self._v_id = id
          if id == 'R9999':
            return {id: None}
            

    def get_rate(self):
        page = requests.get(self.url)
        print('Status Code:', page.status_code) 
        soup = BeautifulSoup(page.content, "xml")
        #print(soup)
        result = {}
        vals = soup.find_all('Valute')
        for item in vals:
            v_id = item['ID']
            v_name = item.find('Name').text
            v_char_code = item.find('CharCode').text
            v_nom = item.find('Nominal').text
            value = item.find('Value').text.replace(',', '.')
            # result.append(valute)

            result[v_id] = {
                'char_code': v_char_code,
                'name': v_name,
                'nom': v_nom,
                'value': "%.2f" % float(value)
            }
        return result


def input_data(Currency):
  print('1 - all currencies, 2 - one currency')
  inp = int(input('1/2:'))
  if inp == 1:
      print('All current currencies:')
      c = Currency()
      for item in (val := c.get_currencies()):
        print(f'{item}', val[item]['char_code'], val[item]['nom'], val[item]['name'], val[item]['value'], '₽')
  elif inp == 2:
      c = Currency()
      for item in (val := c.get_currencies()):
        print(f'ID = {item},', val[item]['name'])
      selected_currency = Currency()
      id_cur = input('Enter id of currency: ')
      try:
    
        selected_currency.set_currency(id_cur)
        for item in (val := selected_currency.get_currency()):
            print({val[item]}, end = ' ')
      except KeyError:
          print(f"{id_cur} is WRONG:", {f'{id_cur}': None})


if __name__ == '__main__':
  input_data(Currency)
   
    
    
    
    

  


  
   
