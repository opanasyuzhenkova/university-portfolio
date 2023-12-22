'''Лабораторная работа 1. Панасюженкова О.Д (вариант 12). Рекурсивный вариант функции, генерирующей бинарное дерево

# Root = 12; height = 4, left_leaf = root^3, right_leaf = (root*2)-1
'''


def gen_bin_tree(height=4, root=12) -> dict:
    """Function returns a dictionary, the first key of which is root, and then, with the help of nested dictionaries, there are "branches": 
    left branch = root^3
    right branch = (root * 2)-1
  
    Keyword arguments:
    height -- tree height
    root -- the meaning of the tree root
    """

    left_leaf = root**3
    right_leaf = (root * 2) - 1

    if height == 0: #условие зевершения рекурсии
        return {str(root): []}
    else:
        res = {
            str(root): [
                gen_bin_tree(height - 1, left_leaf),
                gen_bin_tree(height - 1, right_leaf)
            ]
        }
        return res


def gen_bin_tree_json(res_tree):
    """Function encodes the dictionary into a json object

      Keyword arguments:
      res_tree -- dictionary object
  """
    import json
    with open("data_file.json", "w") as write_file:
        json.dump(res_tree, write_file, sort_keys=True, indent=2)
    return json.dumps(res_tree, sort_keys=True, indent=2)


def main():
    res_tree = gen_bin_tree(1, 5)
    print(res_tree)
    print('JSON-формат:', gen_bin_tree_json(res_tree))

    #print('Бин.дерево параметры по умолчанию: ', gen_bin_tree())


if __name__ == '__main__':
    assert gen_bin_tree(height=0, root=5) == {'5': []}, 'для высоты 0'
    main()
