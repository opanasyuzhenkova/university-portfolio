import threading


def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    l = [element for element in array if element < pivot]
    mid = [element for element in array if element == pivot]
    r = [element for element in array if element > pivot]

    return quicksort(l) + mid + quicksort(r)


def threaded_quicksort(array, depth_limit=0):
    if len(array) <= 1:
        return array

    # Limit the depth of thread creation to avoid excessive threading overhead
    if depth_limit > 2:
        return quicksort(array)

    pivot = array[len(array) // 2]
    l = [element for element in array if element < pivot]
    eq = [element for element in array if element == pivot]
    r = [element for element in array if element > pivot]

    l_thread = threading.Thread(target=lambda: threaded_quicksort(l, depth_limit + 1))
    r_thread = threading.Thread(target=lambda: threaded_quicksort(r, depth_limit + 1))

    l_thread.start()
    r_thread.start()

    l_thread.join()
    r_thread.join()

    return quicksort(l) + eq + quicksort(r)


if __name__ == "__main__":
    unsorted_array = [1, 90, 56, 89, 32, 4, 6, 7, 9]
    sorted_array = threaded_quicksort(unsorted_array)
    print("Original List:", unsorted_array)
    print("Sorted List:", sorted_array)
