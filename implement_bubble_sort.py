import random


def swap_values(j, i, data):
    """swap the values of two indexes"""
    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data


def bubble_sort(data, length):
    """implement bubble sort algorithm."""
    swap_count = 0
    for i in range(length - 1, -1, -1):
        for j in range(length):
            if j < i and data[j] > data[i]:
                data = swap_values(j, i, data)
                swap_count += 1

        # data in sorted form if no swaps
        if swap_count == 0:
            return data

    return data


# Get the length of list from user, fill with random number
length = int(input("Enter the size of random list: "))
data = []
for i in range(length):
    data.append(random.randint(1, 50))

print("Before Sorting: ", data)

# sort the data using bubble sort and print it
sorted_data = bubble_sort(data, length)
print("After Sorting: ", sorted_data)
