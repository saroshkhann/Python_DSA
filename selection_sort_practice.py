unsorted_list = [12,25,9,90,45,67,43,78]

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

result = selection_sort(unsorted_list)
print(result)