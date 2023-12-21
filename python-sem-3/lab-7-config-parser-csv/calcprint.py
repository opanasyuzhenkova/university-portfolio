import datetime
import csv

def write_log(*args, action, result, file='/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/history.csv'):
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
    date = datetime.datetime.today()
    time = date.strftime('%H:%M:%S')

    with open('/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/history.csv', mode = 'a', encoding = 'utf-8') as w_file:
      file_writer = csv.writer(w_file, delimiter = "|", lineterminator="\r")
      file_writer.writerow([time,action,args,'=', result])

  except PermissionError:
    print(f'ОШИБКА записи в файл {file}')
    file_new = '/workspaces/university-portfolio/python-sem-3/lab-7-config-parser-csv/history_new.csv'
    print(f'ПОПЫТКА записать лог в файл с новым именем: {file_new}')
    try:
      with open(file_new, mode = 'a', errors = 'ignore', encoding = 'utf-8') as backup_file:
        file_writer = csv.writer(backup_file, delimiter = "|", lineterminator="\r")
        file_writer.writerow([time,action,args,'=', result])

    except PermissionError as e:
          error = e
    else:
      print(f'>>> Лог записан в файл {file_new}')
  else:
    print(f'>>> Лог записан в файл {file}')

  
  if error:
    raise PermissionError(
      f'Ошибка записи в файл history_new.csv. Записать не удалось.'
    )

 
  #help(write_log)