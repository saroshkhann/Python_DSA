unsorted_list = [12, 25, 11, 34, 90, 22]
n = len(unsorted_list)


def binary_search(arr):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


sorted_list = binary_search(unsorted_list)
print(sorted_list)
