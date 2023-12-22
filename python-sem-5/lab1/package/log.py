import datetime
import string


def write_log(*args, action, result, file='history.txt'):
    """
  _________
  Функция сохраняет историю вычислений в файле 
  history.txt в следующем виде:

  22:48:20 | -: (6.123456789, 1.0000101) = 5.12345 
  _________
  : 'args' - числа, над которыми производтся арифметическая операция
  : 'action' - арифметическая операция
  : 'result' - результат действия
  : 'file' - файл с историей вычислений

    """

    error = None
    try:
        #записываем логи в файл history.txt
        date = datetime.datetime.today()
        time = date.strftime('%H:%M:%S')
        f = open(file, mode='a', errors='ignore')
        f.write(f"{time} | {action}: {args} = {result} \n")
    except Exception:
        raise PermissionError('Ошибка записи в файл')
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f"{action}: {args} = {result} \n")
        except PermissionError as e:
            error = e
    else:
        f.close()

    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')
