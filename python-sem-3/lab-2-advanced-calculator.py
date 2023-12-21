#Лабораторная работа 2 Панасюженкова О.Д. 2-ИВТ-1
# Среднее квадратическое отклонение - deviation()- произвольное число аргументов!
# Настройки. Точность. convert_precision()



settings = {'precision': '0.000001'}

#ввод операндов, точности, действия
def main():
    act = input("Введите действие:")
    if act == 'D':
      operands_list = []
      while True:
        op = (input('Введите аргумент: '))
        if op !='':
          operands_list.append(float(op))
        else:
          break 
      pr = input("Введите точность:")

      if (pr == ''):
        print('Используется стандартная точность = 0.000001')
        print("Элементы выборки: ", *operands_list)
        result = deviation(*operands_list,precision = settings.get('precision'))
        print("Среднее квадратическое отклонение: ", result)

      else:
        print('\n')
        print("Элементы выборки: ", *operands_list)
        result = deviation(*operands_list,precision = pr)
        print("Среднее квадратическое отклонение: ", result)

    else:
      op1 = float(input("Введите операнд 1:"))
      op2 = float(input("Введите операнд 2:"))
      pr = input("Введите точность:")
      if (pr == -1):
        print("Результат: ", 0)
      if (pr == ''):
        print('Используется стандартная точность = 0.000001')
        res = calculate(op1, op2, act, settings.get('precision'))
        print("Результат: ", res)
      else:
        res = calculate(op1, op2, act,pr)
        print("Результат: ", res)


#ТОЧНОСТЬ ВЫЧИСЛЕНИЙ
def convert_precision(precision):
 
  """
  _________
  Функция преобразует точность вычислений и возвращает переменную [i] - это количество цифр после запятой
  _________
  : param 'precision' - precision (0.01, 0.001, 0.00001...)

  >>> convert_precision('0.0001')
  4
  >>> convert_precision('0.001')
  3
  
  """

  #проверяем вводимую точность на тип, преобразуем к 16f для работы с экспоненциальными значениями 1e-005 и больше

  if type(precision) is not float:
    try:
      precision = "{:.16f}".format(float(precision))
      for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
          return i
    except ValueError:
      i=-1
      print('Неверный тип точности!')
      return i
  else:
    precision = "{:.16f}".format(precision)
    for i in range(len(str(precision))):
      if float(precision) * 10**i >= 1:
        return i
#help(convert_precision)
#print(convert_precision('0.0000001'))


# ВЫЧИСЛЕНИЯ С ЗАДАННОЙ ТОЧНОСТЬЮ

def calculate(op1, op2, act, precision):
  #документация docstring + несколько doctest (запуск из __name__==__main__)
    """
    _________
    Функция выполняет основные арифметические операции над числами
    _________
    : 'op1','op2' - операнды
    : 'act' - арифметическая операция
    : 'precision' - точность вычисления [0.01, 0.001, 0.0001...]
    _________
    Возможные арифметические операции:
    _________
    : [+] --> сумма
    : [-] --> разность
    : [*] --> произведение
    : [/] --> деление
    : [**] --> возведение в степень
    : [%] --> остаток от деления
    : [//] --> целочисленное деление
    : [D] --> среднее квадратическое отклонение

    >>> calculate(1.1, 4, "+", '0.1') 
    5.1
    >>> calculate(4.1, 1, "-", '0.1') 
    3.1
    >>> calculate(4.1, 1, "*", '0.1') 
    4.1
    >>> calculate(4.1, 0, "**", '0.1') 
    1.0
    >>> calculate(4.1, 1, "%", '0.1') 
    0.1
    >>> calculate(5, 2, "//", '0.0') 
    2
    
    """
    if act == '+':  # сумма
        res = op1 + op2
    elif act == '-':  # разность
        if op2 < 0:
            res = op1 + op2
        else:
            res = op1 - op2
    elif act == '*':  # умножение
        res = op1 * op2
    elif act == '/':  # деление
      try:
        res=op1 / op2
      except ZeroDivisionError:
        res = 0
        print("Вы пытаетесь разделить на 0!")
    elif act == '**':  # возведение в степень
        res = op1**op2
    elif act == '%':  # остаток от деления
        try:
          res=op1 % op2
        except ZeroDivisionError:
          res = 0
          print("Вы пытаетесь разделить на 0!")
  
    elif act == '//':  # целочисленное деление
      try:
        res=op1 // op2
      except ZeroDivisionError:
        res = 0
        print("Вы пытаетесь разделить на 0!")

    else:
        print('Данная операция отсутствует')

    if precision:
        ndigits = convert_precision(precision)
        res = round(res, ndigits)
    return res   
#help(calculate)


def deviation(*args,precision):
  """
  _________
  Функция вычисляет среднее квадратическое отклонение
  _________
  : 'args' - массив значений
  : 'precision' - точность вычисления

  >>> deviation(*[1,2,3],precision = '0.001' ) 
  0.816

  """
  from math import sqrt
  #assert len(args)!=0, 'Последовательность не может быть пустой!'
  n = len(args)
  x_sr = sum(args) / n
  res_sum = 0
  for x in args:
    res_sum += (x - x_sr)**2
  res = sqrt((1 / n) * res_sum)

  if precision:
    ndigits = convert_precision(precision)
  else:
    ndigits = settings.get('precision')
    print('Вы пропустили точность вычисления. Используется стандартная = 0.000001')
  res = round(res, ndigits) #convert_precision()
  return res

#help(deviation)


main()
if __name__ =='__main__':
  import doctest
  doctest.testmod()