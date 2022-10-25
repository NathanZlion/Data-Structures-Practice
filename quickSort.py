from random import randint

def quickSort(arr):
    if len(arr)<2:return arr
    pivot = arr.pop()
    left,right= [],[]
    for item in arr:
        if item > pivot: right.append(item)
        else: left.append(item)
    return quickSort(left) + [pivot] + quickSort(right)


arr= [randint(0,100) for _ in range(40)]
print(quickSort(arr))