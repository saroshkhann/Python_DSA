

def binary_search(arr,target):
    n = len(arr)
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1

    return -1

lst = [10,40,70,80,91,95] # Data must be in ascending or descending
target = 40

result = binary_search(lst, target)
print(result)