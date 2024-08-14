def swap_values(i, j, data):
    """swap value of two indexes."""
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data


def insertion_sort(data, length):
    """implement the insertion sort algorithm."""
    for i in range(length):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data = swap_values(j - 1, j, data)
            j = j - 1

    return data


sorted_data = insertion_sort([7, 5, 4, 6, 1, 2, 3], length=7)
print(sorted_data)
