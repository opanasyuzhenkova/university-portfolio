PARAMS = {
    'precision': None,
    'output_type': None,
    'possible_types': None,
    'dest': None
}


def load_params(file="/workspaces/university-portfolio/python-sem-5/lab1/params.ini"):
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

    #проверяем вводимую точность на тип, преобразуем к 16f для работы с экспоненциальными значениями 1e-005 и больше

    if type(precision) is not float:
        try:
            precision = "{:.16f}".format(float(precision))
            for i in range(len(str(precision))):
                if float(precision) * 10**i >= 1:
                    return i
        except ValueError:
            raise AssertionError('Неверный тип точности!')
            i = -1
            print('Неверный тип точности!')
            return i
    else:
        precision = "{:.16f}".format(precision)
        for i in range(len(str(precision))):
            if float(precision) * 10**i >= 1:
                return i


#help(convert_precision)
#print(convert_precision('0.0000001'))


def output(arg, precision=None):

    global PARAMS
    if precision == None:
        precision = PARAMS['precision']

    result = arg

    ndigits = convert_precision(precision)
    result = round(result, ndigits)

    return result


load_params()
