unsorted_list = [12,4,5,1,4,77,86,33]

def selection_sort(arr):
    n =len(arr)

    for i in range(n-1):
        mid_index = i

        for j in range(i+1, n):
            if arr[mid_index] > arr[j]:
                mid_index=j

        arr[i], arr[mid_index] = arr[mid_index], arr[i]
    return arr

result = selection_sort(unsorted_list)
print(result)
print("hello")
print("world")
print("hi")
print("hello world")
print("hello")