import unittest
from main import load_params


class TestLoadParams(unittest.TestCase):  # создаем свой класс для тестов

    #ТЕСТ 1 - ПРОВЕРКА на поднятие исключения при создании файла для стандартных настроек
    def test_creating_file_exception(self):
        settings_file = '/workspaces/university-portfolio/python-sem-3/lab-6-tables/params.ini'

        self.assertRaises(Exception,
                          load_params,
                          file=settings_file)


    def test_creating_file_exception_with_desc(self):
        settings_file = '/workspaces/university-portfolio/python-sem-3/lab-6-tables/params.ini'
        # f'Ошибка записи в файл {file_new}. Записать не удалось.'
        
        regex_text = 'Ошибка чтения файла'
        with self.assertRaisesRegex(Exception, regex_text) as cm:
            load_params(file=settings_file)
        # the_exception = cm.exception


if __name__ == '__main__':
    unittest.main(verbosity=1)  # запуск тестов
