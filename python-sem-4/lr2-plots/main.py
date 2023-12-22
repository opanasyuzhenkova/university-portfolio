"""
Лабораторная работа 2.
Сравнение алгоритмов. Графики
"""

import matplotlib.pyplot as plt
import timeit
import tkinter


def recursive_tree(height=4, root=12) -> dict:
    """Function returns a dictionary (using a recursive algorithm), the first key of which is the root, and then, using nested dictionaries, there are "branches": 
    left branch = root^3
    right branch = (root * 2)-1
  
    Keyword arguments:
    height -- tree height
    root -- the meaning of the tree root
    """

    left_leaf = root**3
    right_leaf = (root * 2) - 1

    if height == 0:
        return {str(root): []}
    else:
        res = {
            str(root): [
                recursive_tree(height - 1, left_leaf),
                recursive_tree(height - 1, right_leaf)
            ]
        }
        return res


def non_recursive_tree(height: int, root: int) -> dict:
    left_leaf = lambda x: x**3
    right_leaf = lambda x: (x * 2) - 1
    if height == 0:
        roots = [root]
        return roots
    roots = [[root]]

    for leaf in range(height):
        if (len(roots) == 1):
            r = roots[0]
        else:
            r = [item for s in roots[-1] for item in s]
        leaves = list(
            map(
                lambda root_value:
                [left_leaf(root_value),
                 right_leaf(root_value)], r))
        roots.append(leaves)

    roots.reverse()

    tree = dict()

    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x: [{
        str(x[0]): []
    }, {
        str(x[1]): []
    }], roots[0]))

    for i in range(height):
        sublist = roots[i]
        sublist.reverse()
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i + 1][j // 2][j % 2] = {str(roots[i + 1][j // 2][j % 2]): x}

    tree = roots[-1][0][0]
    return tree


def calculate_time(h: int, func) -> float:
    """
    The function returns the running time of the function: 

    Keyword arguments:
    n -- tree height (variable)
    root -- the meaning of the tree root

"""
    root = 3
    d_time = 0
    start_time = timeit.default_timer()
    func(h, root)
    d_time += timeit.default_timer() - start_time

    return d_time


tree = {"5": [{"125": []}, {"9": []}]}


def main():
    print(recursive_tree(3, 5))
    print(non_recursive_tree(3, 5))

    rec = []
    norec = []
    for n in range(10):
        rec.append(calculate_time(n, recursive_tree))
        norec.append(calculate_time(n, non_recursive_tree))
    plt.plot(rec, label="recursive algorithm")
    plt.plot(norec, label="non recursive algorithm")
    plt.legend()
    plt.show()


if __name__ == '__main__':

    main()
