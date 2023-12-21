import unittest
from main import load_params

#python -m unittest test_load_params -v

class TestLoadParams(unittest.TestCase):  # создаем свой класс для тестов

    #ТЕСТ 1 - ПРОВЕРКА на поднятие исключения при создании файла для стандартных настроек

    
    def test_loading_params(self):
        settings_file = '/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/params.ini'
        self.assertRaises(PermissionError,
                          load_params,
                          file=settings_file)


    '''def test_loading_params_with_desc(self):
        settings_file = '/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/params.ini'
        # f'Ошибка записи в файл {file_new}. Записать не удалось.'
        
        regex_text = f'Ошибка чтения файла. Не удалось записать настройки.'
        with self.assertRaisesRegex(PermissionError, regex_text) as cm:
            load_params(file=settings_file)
        # the_exception = cm.exception'''


if __name__ == '__main__':
    unittest.main(verbosity=1)  # запуск тестов


    #verbosity=1