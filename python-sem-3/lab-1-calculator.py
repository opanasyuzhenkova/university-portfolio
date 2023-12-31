# Лабораторная работа 1. Панасюженкова О.Д 2-ИВТ-1
# : Добавить 2 дополнительных действия для двух операндов

def main():

    op1 = float(input("Введите операнд 1:"))
    op2 = float(input("Введите операнд 2:"))
    act = input("Введите действие:")
    res = calculate(op1, op2, act)
    print("Результат: ", res)


def calculate(op1, op2, act):
  #документация docstring + несколько doctest (запуск из __name__==__main__)
    """
    _________
    Функция выполняет основные арифметические операции над числами
    _________
    : 'op1','op2' - операнды
    : 'act' - арифметическая операция
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
      except ZeroDivisionError:
        res = 0
        print('Вы пытаетесь разделить на 0!')
      finally:
        return res
    elif act == '**':  # возведение в степень
      res = op1**op2
    elif act == '%':  # остаток от деления
      res = op1 % op2
    elif act == '//':  # целочисленное деление
      try:
        res = op1 // op2
      except ZeroDivisionError:
        res = 0
        print('Вы пытаетесь разделить на 0!')
      finally:
        return res
    else:
        print('Данная операция отсутствует')

    
    return res   

main()