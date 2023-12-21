import unittest
from main import write_log
from main import calculate
#python -m unittest test_write_log -v


class TestSomeFunc(unittest.TestCase):  # создаем свой класс для тестов
    def test_creating_file_exception(self):
        args = [1, 2, 3, 4, 5]
        log_file = '/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/history.csv'
        res = calculate(*(1,2,3,4,5), '-')
        self.assertRaises(PermissionError,
                          write_log,
                          *args,
                          action = '-',result = res,
                          file=log_file)

    def test_creating_file_exception_with_descr(self):
        args = [1, 2, 3, 4, 5]
        log_file = '/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/history.csv'
        # f'Ошибка записи в файл {file_new}. Записать не удалось.'
        
        regex_text = f'Ошибка записи в файл history_new.csv. Записать не удалось.'
        res = calculate(*(1,2,3,4,5), '-')
        with self.assertRaisesRegex(PermissionError, regex_text) as cm:
            write_log(*args, action='sum',result=res, file=log_file)
        

if __name__ == '__main__':
    unittest.main(verbosity=1)  # запуск тестов