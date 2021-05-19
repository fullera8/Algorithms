def findSmallest(arr) :
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)) :
        if arr[i] < smallest :
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr) :
    newArray = []
    for i in range(len(arr)) :
        smallest = findSmallest(arr)
        newArray.append(arr.pop(smallest))
    return newArray

print(selectionSort([5,3,6,2,10]))