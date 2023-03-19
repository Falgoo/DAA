import numpy as np
from datetime import datetime

# use copy() to assign original array to new array to prevent change value of original array
# because if not use copy(), new rray and original array will have same id
# so when change any value in new array will change value in original array.

# ------------Bubble sort and test time run------------
def bubbleSort(array):
    newArray = array.copy()
    for value in range(len(newArray)):
        for run in range(value, len(newArray)):

            if newArray[value] > newArray[run]:
                newArray[value], newArray[run] = newArray[run], newArray[value]
    return newArray

def bubbleSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = bubbleSort(array)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000


# -------------Insertion sort and test time run------------

def insertionSort(array):
    newArray = array.copy()

    for valueIndex in range(1, len(newArray)):

        runIndex = valueIndex - 1
        value = newArray[valueIndex]

        while runIndex >= 0 and value < newArray[runIndex]:
            newArray[runIndex + 1] = newArray[runIndex]
            runIndex -= 1
        newArray[runIndex + 1] = value
    return newArray

def insertionSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = insertionSort(array)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000


# -------------Selection sort and test time run------------

def selectionSort(array):
    newArray = array.copy()

    for valueIndex in range(len(newArray)):
        minIndex = valueIndex
        for runIndex in range(valueIndex+1, len(newArray)):
            if newArray[minIndex] > newArray[runIndex]:
                minIndex = runIndex
    
        newArray[valueIndex], newArray[minIndex] = newArray[minIndex], newArray[valueIndex]
    return newArray

def selectionSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = selectionSort(array)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000

# -------------Quick sort and test time run------------

def partition(array, left, right):

    pi = array[right]
    smElementIndex = left - 1

    for index in range(left, right):
        if array[index] <= pi:
            smElementIndex += 1
            array[smElementIndex], array[index] = array[index], array[smElementIndex]
    array[smElementIndex+1], array[right] = array[right], array[smElementIndex+1]
    return smElementIndex + 1


def quickSort(array, left, right):
    newArray = array.copy()
    if (left < right):
        pi = partition(newArray, left, right)

        newArray = quickSort(newArray, left, pi - 1)
        newArray = quickSort(newArray, pi + 1, right)
    return newArray

def quickSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = quickSort(array, 0, len(array) - 1)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000

# -------------Merge sort and test time run------------

def merge(array, left, middle, right):

    lengthLeft = middle - left + 1
    lengthRight = right - middle

    leftArray = [0] * (lengthLeft)
    rightArray = [0] * (lengthRight)

    for eleIndex in range(0,lengthLeft):
        leftArray[eleIndex] = array[left + eleIndex]
    
    for eleIndex in range(0,lengthRight):
        rightArray[eleIndex] = array[middle + 1 + eleIndex]

    leftIndex = 0
    rightIndex = 0
    mergeIndex = left

    while leftIndex < lengthLeft and rightIndex < lengthRight:
        if leftArray[leftIndex] <= rightArray[rightIndex]:
            array[mergeIndex] = leftArray[leftIndex]
            leftIndex += 1
        else:
            array[mergeIndex] = rightArray[rightIndex]
            rightIndex += 1
        mergeIndex += 1
    
    while leftIndex < lengthLeft:
        array[mergeIndex] = leftArray[leftIndex]
        leftIndex += 1
        mergeIndex += 1
    
    while rightIndex < lengthRight:
        array[mergeIndex] = rightArray[rightIndex]
        rightIndex += 1
        mergeIndex += 1

def mergeSort(array, left, right):
    newArray = array.copy()
    if left < right:
        middle = left + (right - left) // 2

        newArray = mergeSort(newArray, left, middle)
        newArray = mergeSort(newArray, middle + 1, right)
        merge(newArray, left, middle, right)
    return newArray

def mergeSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = mergeSort(array, 0, len(array) - 1)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000

# -------------- Heap sort and test time run------------

def heap(array, lengthArray, index):
    bigest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < lengthArray and array[index] < array[left]:
        bigest = left
    if right < lengthArray and array[bigest] < array[right]:
        bigest = right
    if bigest != index:
        array[index], array[bigest] = array[bigest], array[index]
        heap(array, lengthArray, bigest)

def heapSort(array):
    newArray = array.copy()
    lengthArray = len(newArray)
    for index in range(lengthArray // 2 - 1, -1, -1):
        heap(newArray, len(newArray), index)

    for index in range(lengthArray - 1, 0, -1):
        newArray[index], newArray[0] = newArray[0], newArray[index]
        heap(newArray, index, 0)
    return newArray

def heapSortTest(array):
    sortedArray = array.copy()

    startTime = datetime.now().timestamp() * 1000000
    for i in range(1000):
        sortedArray = heapSort(array)
    endTime = datetime.now().timestamp() * 1000000

    duration = endTime - startTime
    return sortedArray, duration/1000


def main():
    n = 100
    array = list(np.random.randint(1000, size=(n)))
    print("With array has: ", n, "elements random")
    print("Array before sort:\n",array, "\n")
    listSort = []

    arrayBubble, bubbleTime = bubbleSortTest(array)
    listSort.append({"name": "bubble sort", "array": arrayBubble, "time": bubbleTime})

    arrayInsertion, insertionTime = insertionSortTest(array)
    listSort.append({"name": "insertion sort", "array": arrayInsertion, "time": insertionTime})

    arraySelection, selectionTime = selectionSortTest(array)
    listSort.append({"name": "selection sort", "array": arraySelection, "time": selectionTime})

    arrayQuick, quickTime = quickSortTest(array)
    listSort.append({"name": "quick sort", "array": arrayQuick, "time": quickTime})

    arrayMerge, mergeTime = mergeSortTest(array)
    listSort.append({"name": "merge sort", "array": arrayMerge, "time": mergeTime})

    arrayHeap, heapTime = heapSortTest(array)
    listSort.append({"name": "heap sort", "array": arrayHeap, "time": heapTime})

    print("============Result after sort algorithms=============\n")
    print("Array after sorted by bubble sort:\n", arrayBubble, "\n")
    print("Array after sorted by insertion sort:\n", arrayInsertion, "\n")
    print("Array after sorted by selection sort:\n", arraySelection, "\n")
    print("Array after sorted by quick sort:\n", arrayQuick, "\n")
    print("Array after sorted by merge sort:\n", arrayMerge, "\n")
    print("Array after sorted by heap sort:\n", arrayHeap, "\n")

    print("===========Time of sort algorithms==================\n")
    print("Time of bubble sort:", bubbleTime, "microseconds")
    print("Time of insertion sort:", insertionTime, "microseconds")
    print("Time of selection sort:", selectionTime, "microseconds")
    print("Time of quick sort:", quickTime, "microseconds")
    print("Time of merge sort:", mergeTime, "microseconds")
    print("Time of heap sort:", heapTime, "microseconds\n")

    fastestIndex = 0
    for sort in range(len(listSort)):
        if listSort[fastestIndex].get("time") > listSort[sort].get("time"):
            fastestIndex = sort
    print("Fastest sort is: ",listSort[fastestIndex].get("name"))

    lowestIndex = 0
    for sort in range(len(listSort)):
        if listSort[lowestIndex].get("time") < listSort[sort].get("time"):
            lowestIndex = sort
    print("Lowest sort is: ",listSort[lowestIndex].get("name"))

main()