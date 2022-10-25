

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]: min = j
        if min != i: arr[i], arr[min] = arr[min], arr[i]
    return arr

arr= [3,7,1,6,2,5]
print(selectionSort(arr))