#ЛАБОРАТОРНАЯ РАБОТА 3. Панасюженкова О. 2-ИВТ-1

"""Пункт 1. Циклы, "в лоб" 

two_sum(): возвращает кортеж из двух индексов элементов списка lst - сумма элементов по этим индексам равна переменной target

Элемент по индексу может быть выбран лишь единожды, значения в списке могут повторяться. Если в списке встречается больше чем два индекса, подходящих под условие - вернуть наименьшие из всех. Элементы находятся в списке в произвольном порядке. """

lst = [1,2,3,4,5,6,7,8]
target = 8
#print(len(lst))
# проход по циклу от 0 до 9 (=len(lst)-1)
  #параллельный проход от 1 до 10 и сравнение с i
  #выход из цикла при первой найденной паре индексов

def get_key(d, value):
  min_k=len(lst)
  for k, v in d.items():
    if v == value:
      if k<min_k:
        return int(k)


def two_sum(lst, target):
  """
  _________
  Функция определяет пару индексов, сумма элементов по которым равна заданному числу
  _________
  : 'lst' - массив значений
  : 'target' - заданная сумма элементов

  >>> two_sum([1,2,3,4,5,6,7,8,9],8) 
  (0, 6)
  >>> two_sum([9,8,7,6,5,4,3,2,1],8) 
  (2, 8)
  >>> two_sum([9,8,8,7,6,5,4,3,2,1],8) 
  (3, 9)
  
  """
  min_j = len(lst)
  for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
      if (lst[j] == target - lst[i] and j<min_j):
        return (i,j)
        break

print('Вызов two_sum(): ', two_sum(lst,target))  

'''Пункт 2 за O(n) для отсортированного списка'''

def two_sum_hashed_sort(lst,target):
  #проход по массиву основываясь на левой и правой границе 
  touple=()
  li = 0 #левый индекс
  ri = len(lst)-1  #правый индекс
  while li != ri:
      cur_sum = lst[li] + lst[ri]
      if (cur_sum < target):
          li+=1
      elif (cur_sum > target):
          ri-=1;
      elif (cur_sum == target):
          touple = touple +(li, ri)
          return(touple)
          break  

#print('вызов two_sum_hashed_sort(): ', two_sum_hashed_sort(lst,target))

'''Пункт 2 за O(n) для НЕотсортированного списка'''

def two_sum_hashed(lst,target):
  touple=()
  a=[]
  for i in range(len(lst)): #для создания словаря - ИНДЕКСЫ
    a.append(i)
  #print(a)
  
  dif_mas=[] # для исключения повторяющися чисел
  new_dic = dict(zip(a,lst))
  #print(new_dic)
  i=0
  new_in=-1
  for i in range(len(lst)-1):
    diff_i = target - lst[i]
    if(diff_i not in dif_mas):
      dif_mas.append(diff_i)
      if diff_i in new_dic.values():
        new_in = get_key(new_dic,diff_i) #получаем ключ по значению
      
      if(((lst[new_in]+lst[i]) == target) and (new_in != i) and (i<new_in)):
        touple = touple+(i,new_in)
        return touple
        touple = ()
    
 
print('Вызов two_sum_hashed(): ', two_sum_hashed(lst,target))


"""Пункт 3. О(n) + вывести все пары индексов в виде кортежей в списке """


#lst = [1,2,3,4,5,6,7,8,9]
def two_sum_hashed_all(lst,target):
  dif_mas=[] # для исключения повторяющися чисел
  touple=()
  a=[]
  for i in range(len(lst)): #для создания словаря - ИНДЕКСЫ
    a.append(i)
  #print(a)
  new_dic = dict(zip(a,lst))
  #print(new_dic)
  res_list = [] #результирующий список
  i=0
  new_in=-1
  for i in range(len(lst)-1):
    diff_i = target - lst[i]
    if(diff_i not in dif_mas):
      dif_mas.append(diff_i)
      if diff_i in new_dic.values():
        new_in = get_key(new_dic,diff_i) #получаем ключ по значению
      if(((lst[new_in]+lst[i]) == target) and (new_in != i) and (i<new_in)):
        touple = touple+(i,new_in)
        res_list.append(touple)
      
      touple = ()
    new_dic[target-lst[i]]=-1
  return res_list


print('Вызов two_sum_hashed_all(): ', two_sum_hashed_all(lst,target))

#help(two_sum)

if __name__ =='__main__':
  import doctest
  doctest.testmod()


if __name__ =='__main__':
  import doctest
  doctest.testmod()