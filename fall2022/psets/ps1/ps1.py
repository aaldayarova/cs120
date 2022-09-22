from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univSize, base, array):
    
    arrayPrime = []
    k = math.ceil(math.log2(univSize)/math.log2(base))

    for i in range(len(array)):
        arrayPrime[i][1] = BC(array[i], base, k)
    
    for j in range(k):
        for i in range(len(array)):
            arrayPrime[i][0] = arrayPrime[i][1][j]
            newArray = countSort(base, [arrayPrime[i][0], [array[i][1], arrayPrime[i][1]]])
    
    for i in range(len(array)):
        array[i][0] = sum(arrayPrime[i][1][j]*(base**(k-1)) for j in range(k))
    
    return array

    # # Size of universe U in the new base
    # k = math.ceil(math.log2(univSize)/math.log2(base))

    # # Placeholder array which holds the values of V' and K' we'll compute later;
    # # At this point arrayPrime looks like: arrayPrime = [[0,0], [0,0], [0,0]...] where each
    # # array element holds a list of [K', V'] values 
    
    # # arrayPrime = []
    # # for i in range(len(array)):
    # #     arrayPrime[i] = [0,0]
    # arrayPrime = [[0, 0] for _ in range(len(array))]
    
    # # For each element in our original array, we want our arrayPrime to hold base-change K in 
    # # each of its V' values
    # for i in range(len(array)):
    #     arrayPrime[i][1] = BC(array[i][0], base, k)

    # # For every column/digit
    # for j in range(k):
    #     # For every number
    #     for i in range(len(array)):
    #         # Store the column's/digit's value in K' 
    #         arrayPrime[i][0] = arrayPrime[i][1][j]

    #         # Sort the array by column/digit; output a sorted K-V pair list (the output of CountingSort)
    #         # for l in range(len(array)):
    #         #     countSortArray = countSort(base, [arrayPrime[l][0], [array[l][1], arrayPrime[l][1]]])
    #         countSortArray = countSort(base, [[arrayPrime[i][0], [array[i][1], arrayPrime[i][1]]] for i in range(len(array))])
    #         # Now, take the values from the output of Counting Sort and update the arrayPrime and array,
    #         # after which you can move on to the next column/digit

    #         for m in range(len(array)):
    #             arrayPrime[m][0] = countSortArray[m][0]
    #             array[m][1] = countSortArray[m][1][0]
    #             arrayPrime[m][1] = countSortArray[m][1][1]
    
    # # Bring the K values back to their original base, which was base 10
    # # for i in range(len(array)):
    # #     # Check wether this section is correct
    # #     for j in range(k):
    # #         array[i][0] = sum((arrayPrime[i][1][k-1])*base**(k-1))
    # for i in range(len(array)):
    #     array[i][0] = sum([arrayPrime[i][1][j] * (base ** j) for j in range(k)])
    
    # # Return the array
    # return array