def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Enter the elements of the array (space seperated):")
array = list(map(int,input().strip().split()))
print("Array before sorting:",array)
result = bubbleSort(array)
print("Sorted array is:",result)