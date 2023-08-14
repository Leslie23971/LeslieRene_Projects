
import random

def QuickSort(inputArray, left, right) :

    if left >= right :
        return
    
    pivotIndex = Partition(inputArray, left, right)

    QuickSort(inputArray, left, pivotIndex-1)
    QuickSort(inputArray, pivotIndex+1, right)

def Partition(inputArray, left, right):

    i = left - 1

    pivotindex = right

    for j in range(left, right) :
        if inputArray[j] < inputArray[pivotindex] :
            i += 1
            inputArray[i], inputArray[j] = inputArray[j], inputArray[i]
        j += 1
    
    # Move pivot to index i+1 so that everything lower than pivot be in indexes smaller than pivot index, 
    # and everything greater than pivot be in indexes greater than pivot index
    inputArray[i + 1], inputArray[right] = inputArray[right], inputArray[i + 1]

    return i+1


def performQuickSort(arr) :
    print("Initial input")
    print(arr)

    QuickSort(arr, 0, len(arr)-1)

    print("Sorted input")
    print(arr)
    print(" *********************************** ***********************************")


performQuickSort([random.randint(0,100) for x in range(15)])
performQuickSort([random.randint(0,999) for x in range(6)])
performQuickSort([random.randint(0,1999) for x in range(25)])
performQuickSort([random.randint(0,999) for x in range(3)])
performQuickSort([random.randint(0,999) for x in range(7)])
performQuickSort([random.randint(0,999) for x in range(47)])
performQuickSort([random.randint(0,999) for x in range(2)])
performQuickSort([random.randint(0,999) for x in range(10)])
