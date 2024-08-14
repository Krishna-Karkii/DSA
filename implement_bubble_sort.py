
def bubble_sort(data, length):
    """implement bubble sort algorithm."""
    for i in range(length - 1, -1, -1):
        for j in range(length):
            if j < i:
                if data[j] > data[i]:
                    data = swap_values(j, i, data)


