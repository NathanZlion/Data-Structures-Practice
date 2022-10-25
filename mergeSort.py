

def merger(arr1, arr2):
    mergedArr,i,j= [],0,0
    while (i < len(arr1) and j<len(arr2)):
        if arr1[i] > arr2[j]:
            mergedArr.append(arr2[j])
            j+=1
        else:
            mergedArr.append(arr1[i])
            i+=1
    if i < len(arr1): mergedArr+= arr1[i:]
    if j < len(arr2): mergedArr+= arr2[j:]
    return mergedArr


def mergeSort(arr):
    if len(arr) ==1:return arr
    mid = len(arr)//2
    return merger(mergeSort(arr[:mid]),mergeSort(arr[mid:]))

print(mergeSort([1,7,5,3,15,4,32]))
