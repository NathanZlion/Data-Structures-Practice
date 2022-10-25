

def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]> arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]

arr= [1,5,8,12,9]
bubbleSort(arr)
print(arr)