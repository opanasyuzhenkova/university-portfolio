import unittest
from main import write_log
from main import calculate

class TestSomeFunc(unittest.TestCase):  # создаем свой класс для тестов
    def test_creating_file_exception(self):
        args = [1, 2, 3, 4, 5]
        log_file = 'newoutput.txt'

        self.assertRaises(Exception,
                          write_log,
                          *args,
                          action='sum',
                          file=log_file)

    def test_creating_file_exception_with_descr(self):
        args = [1, 2, 3, 4, 5]
        log_file = 'newoutput.txt'
        # f'Ошибка записи в файл {file_new}. Записать не удалось.'
        regex_text = 'Ошибка записи в файл'
        res = calculate()


        with self.assertRaisesRegex(Exception, regex_text) as cm:
            write_log(*(args), action='+', result = res, file=log_file)
        # the_exception = cm.exception
        


if __name__ == '__main__':
    unittest.main(verbosity=1)  # запуск тестов