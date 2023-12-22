import string


def input_args():
    act = input("Введите действие:")
    try:
        op1 = float(input("Введите операнд 1:"))
        op2 = float(input("Введите операнд 2:"))
    except ValueError:
        res = 0
        print('Вводите числа типа float или int!')
        return 0
    pr = input("Введите точность:")
    if (pr == -1):
        print("Результат: ", 0)
    if (pr == ''):
        print('Используется стандартная точность = 0.000001')
        #   res = calculate(op1, op2, act, settings.get('precision'))
        #   print("Результат: ", res)
        # else:
        #   res = calculate(op1, op2, act,pr)
        #   print("Результат: ", res)

    return [op1, op2, act, pr]


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

    from prettytable import PrettyTable
    symbols = {}
    # разложим входные аргументы по переменным
    mytable = PrettyTable()
    res = inp_args[-1]
    #print(res)
    act = inp_args[-2]
    #print(act)
    operands = inp_args[:-2]
    #print(operands)
    #write_log(*(operands), action = act, result = res)

    _i = 0  # присваиваем аргументам значения A, B, C

    for op in operands:
        symbols[string.ascii_uppercase[_i]] = op
        _i += 1

    #print(symbols)
    #d = list(symbols.keys())
    '''ИСПРАВЛЕНИЕ'''

    def print_list_of_symbols(symbols):
        # 1 строка 1 ячейка
        strA = ",".join(symbols.keys())
        return strA

    def print_sum_of_symbols(symbols):
        # 1 строка 2 ячейка
        if act == "D":
            output = f'Среднее кв.отклонение'
        else:
            output = ''
            for symb in symbols.keys():
                if symb == (list(symbols.keys())[-1]):
                    output += (f'{symb}')
                    break
                output += (f'{symb}{act}')
        return output

    def print_values(operands):
        #2 строка 2 ячейка
        output = ''
        for inp_arg in operands:
            if inp_arg == operands[-1]:
                output += (f'{inp_arg}')
                break
            output += (f'{inp_arg}') + ' '
        return output

    a1_1 = print_list_of_symbols(symbols)
    a1_2 = print_sum_of_symbols(symbols)
    a2_1 = print_values(operands)
    a2_2 = res

    mytable.field_names = [a1_1, a1_2]
    mytable.add_row([a2_1, a2_2])
    print(mytable)
