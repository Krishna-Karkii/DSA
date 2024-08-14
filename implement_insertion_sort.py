import random


def swap_values(i, j, data):
    """swap value of two indexes."""
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data


def insertion_sort(data, length):
    """implement the insertion sort algorithm."""
    for i in range(1, length):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data = swap_values(j - 1, j, data)
            j = j - 1

    return data


# asking the user for the length of random list
length = int(input("Enter a length of random list: "))

# creating a random list
list_to_sort = []
for i in range(length):
    list_to_sort.append(random.randint(1, 100))

print("Before Sorting: ", list_to_sort)

# Sorting using insertion sort
sorted_list = insertion_sort(list_to_sort, length)
print("After Sorting: ", sorted_list)
