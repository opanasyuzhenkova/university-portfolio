# Лабораторная работа 5. Панасюженкова О.Д 2-ИВТ-1
# Загрузка параметров из файла load_params() в глобальную переменную PARAMS и далее вычисления с использованием данных настроек + запись истории вычислений в history.txt

from calcprint import write_log
#глобальная переменная PARAMS - храним настройки
PARAMS = {
   
    'precision': None,
    'output_type': None,
    'possible_types': None,
    'dest': None
}

def load_params(file="/workspaces/university-portfolio/python-sem-3/lab-5-files/params.ini"):
    """
    _________
    Функция загружает параметры для калькулятора 
    из созданного пользователем файла load_params.ini
    _________

    : 'file' - файл с настройками калькулятора
    _________

    Пример содержимого файла:

    precision='0.00000001' - желаемая точность вычислений
    output_type=float - тип результата
    possible_types=float - возможные типы 
    dest=history.txt - файл для записи истории вычислений
    _________

    """
    global PARAMS
    f = open(file, mode='r', errors='ignore')
    lines = f.readlines()
    for l in lines:
        param = l.split('=')  # param[0], param[1]
        param[1] = param[1].strip('\n')

        if param[0] == 'precision':
            param[1] = eval(param[1])
        if param[0] == 'output_type':
            if param[1] == 'float':
                param[1] = float
            if param[1] == 'int':
                param[1] = int
        if param[0] == 'possible_types':
            param[1] = float

        PARAMS[param[0]] = param[1]

#help(load_params)      

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
  if type(precision) is not float:
    try:
      precision = "{:.16f}".format(float(precision))
      for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
          return i
    except ValueError:
      raise AssertionError('Неверный тип точности!')
      i=-1
      print('Неверный тип точности!')
      return i
  else:
    precision = "{:.16f}".format(precision)
    for i in range(len(str(precision))):
      if float(precision) * 10**i >= 1:
        return i



def calculate(*args, **kwargs):
    """
    _________
    Функция выполняет основные арифметические операции над числами
    _________
    : '*args' - последовательность операндов
    : **kwargs - передаваемые настройки для калькулятора
    (precision, output_type, 'dest', 'possible_types')
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
    
    """
    precision = convert_precision(kwargs['precision'])
    output_type = kwargs['output_type']
    if args[len(args) - 1] == '+':
        result_sum = sum(args[0:len(args) - 1])
        if type(result_sum) != output_type:
            result_sum = output_type(result_sum)

        return round(result_sum, precision)

    elif args[len(args) - 1] == '-':
        result_dif = args[0];
        for i in args[1:len(args) - 1]:
            result_dif -= i

        if type(result_dif) is not output_type:
            result_dif = output_type(result_dif)

        return round(result_dif, precision)

    elif args[len(args) - 1] == '*':
        result_multipl = 1;
        for i in args[0:len(args) - 1]:
            result_multipl *= i

        if type(result_multipl) is not output_type:
            result_multipl = output_type(result_multipl)

        return round(result_multipl, precision)

    elif args[len(args) - 1] == '/':
        result_div = 1;
        for i in args[0:len(args) - 1]:
            result_div /= i

        if type(result_div) is not output_type:
            result_div = output_type(result_div)

        return round(result_div, precision)

    elif args[len(args) - 1] == '**':
        result_pow = args[0] ** args[1];

        if type(result_pow) is not output_type:
            result_pow = output_type(result_pow)
        return round(result_pow, precision)

    elif args[len(args) - 1] == '%':
        result_rem = args[0] % args[1];

        if type(result_rem) is not output_type:
            result_rem = output_type(result_rem)
        return round(result_rem, precision)

    elif args[len(args) - 1] == '//':
        result_div_int = args[0]
        for i in args[1:len(args) - 1]:
            result_div_int //= i

        if type(result_div_int) is not output_type:
            result_div_int = output_type(result_div_int)
        return round(result_div_int, precision)


if __name__ == '__main__':
    def test_loading_params():
        load_params()

        assert PARAMS.get(
            'dest'
        ) == 'history.txt', "Имя файла для записи истории вызовов функции calculate должно быть history.txt"


    def test_packed_calc_sum():
        assert calculate(1.000001, 2.000002, 3.00005, '+',
                         **PARAMS) == 6.000053, "float round"


    test_loading_params()

    # res = calculate(4.3206, 2.2132, '-', **PARAMS)

    res = calculate(6.123456789, 1.0000101, '-', **PARAMS)
    write_log(*(6.123456789, 1.0000101), action='-', result=res)