from . import precision as pr


def calculate(op1, op2, act, precision):
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
            res = op1 / op2
        except:
            print("Вы пытаетесь разделить на 0!")
            raise ZeroDivisionError("Вы пытаетесь разделить на 0!")
            res = 0

    elif act == '**':  # возведение в степень
        res = op1**op2
    elif act == '%':  # остаток от деления
        try:
            res = op1 % op2
        except ZeroDivisionError:
            res = 0
            print("Вы пытаетесь разделить на 0!")

    elif act == '//':  # целочисленное деление
        try:
            res = op1 // op2
        except ZeroDivisionError:
            res = 0
            print("Вы пытаетесь разделить на 0!")

    else:
        print('Данная операция отсутствует')

    if precision:
        ndigits = pr.convert_precision(precision)
        res = round(res, ndigits)
    #print(res)
    return res


#help(calculate)
