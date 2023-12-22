"""
Разработать фрагмент программы, позволяющий получать данные о текущих курсах валют с сайта Центробанка РФ с использованием сервиса, который они предоставляют.

https://cbr.ru/development/
http://www.cbr.ru/scripts/XML_daily.asp

https://digitology.tech/docs/python_3/tutorial/floatingpoint.html
"""

# res = get_currencies(['R01035', 'R01335', 'R01700J'])

import requests

tracked_currencies = []


class Currency:
    """Класс для получения и возвращения валют"""

    def __init__(self, id):
        """Конструктор"""
        self.id = id

    def get_currency(self, id):
        """Геттер: получение одной валюты"""
        if id == 'R9999':
            result = {id: None}
            print(result)
        else:
            # print(f'вызван getter одной валюты id {id}')
            from xml.etree import ElementTree as ET
            cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
            # result = []
            root = ET.fromstring(cur_res_str.content)
            valutes = root.findall("Valute")
            # print(valute)
            valute = {}
            for _v in valutes:
                valute_id = _v.get('ID')
                if (str(valute_id) == id):
                    valute_name, valute_val = _v.find('Name').text, _v.find('Value').text
                    valute_charcode = _v.find('CharCode').text
                    valute[valute_charcode] = (valute_name, valute_val)
            print(valute)

    def set_currency(self, id) -> list:
        """Сеттер: добавление новой валюты в список отслеживаемых валют"""
        # проверить, есть ли валюта в списке отслеживаемых, если нет - добавить
        tracked_currencies.append(id)
        return tracked_currencies

    def get_currencies(currencies_ids_lst: list) -> list:
        """Геттер: получение всех валют"""
        import requests
        from xml.etree import ElementTree as ET

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        result = []

        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if (str(valute_id) in currencies_ids_lst):
                valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find(
                    'Value').text
                valute_charcode = _v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                result.append(valute)

        return result

    def __del__(self):
        """Деструктор"""
        print("Вызван деструктор")


if __name__ == '__main__':
    valute_pounds = Currency('R01035')
    valute_lyre = Currency('R01700J')
    valute_tenge = Currency('R01335')

    new_val = Currency('R9999')
    new_val.get_currency('R9999')

    valute_pounds.get_currency('R01035')

    valute_lyre.set_currency('R01700J')
    valute_pounds.set_currency('R01035')

    list_val = valute_pounds.set_currency('R01335')
    print(list_val)
    print(Currency.get_currencies(list_val))

    list_of_vals = ['R01035', 'R01700J', 'R01335']
    print(Currency.get_currencies(list_of_vals))
    # list_of_vals.get_currencies