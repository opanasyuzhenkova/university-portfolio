import datetime
import string

from prettytable import PrettyTable

def print_results(*inp_args):
    
    """
    _________
    Функция принимает переменное число значений и вместе
    с результатом работы калькулятора выводит
    полученные результаты в табличном виде
    _________

    : 'inp_args' - аргументы:
      последний аргумент - результат вычислений
      предпоследний - арифметическое действиео
      остальные аргументы — операнды
 

    """
    symbols={}
    # разложим входные аргументы по переменным
    mytable = PrettyTable()
    res = inp_args[-1]
    #print(res)
    act = inp_args[-2]
    #print(act)
    operands = inp_args[:-2]
    #print(operands)
    write_log(*(operands), action = act, result = res)

    _i = 0  # присваиваем аргументам значения A, B, C

    for op in operands:
      symbols[string.ascii_uppercase[_i]] = op
      _i += 1

    #print(symbols)
    #d = list(symbols.keys())
   
    '''ИСПРАВЛЕНИЕ'''

    def print_list_of_symbols(symbols):
       # 1 строка 1 ячейка
       strA=",".join(symbols.keys())
       return strA
      

    def print_sum_of_symbols(symbols):
      # 1 строка 2 ячейка
      if act=="D":
        output=f'Среднее кв.отклонение'
      else:
        output=''
        for symb in symbols.keys():
          if symb == (list(symbols.keys())[-1]):
            output+=(f'{symb}')
            break
          output+=(f'{symb}{act}')
      return output
    
    def print_values(operands):
      #2 строка 2 ячейка
      output=''
      for inp_arg in operands:
        if inp_arg == operands[-1]:
          output+=(f'{inp_arg}')
          break
        output+=(f'{inp_arg}')+' '
      return output
    
    a1_1 =  print_list_of_symbols(symbols)
    a1_2 = print_sum_of_symbols(symbols)
    a2_1 = print_values(operands)
    a2_2 = res

    mytable.field_names = [a1_1, a1_2]
    mytable.add_row([a2_1, a2_2])
    print(mytable)
    


def write_log(*args, action, result, file='/workspaces/university-portfolio/python-sem-3/lab-6-tables/history.txt'):
  
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
      f'Ошибка записи в файл {file_new}. Записать не удалось.'
    )

