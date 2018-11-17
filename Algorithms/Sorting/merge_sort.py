#!/usr/bin/env python3
'''
    Merge sort algorithm

    Merge sort works by splitting the full array in halves at each
    function call until you are left with a single element array
    or no array

    Then each array is merged with each right array in the same function
    call frame until everything is merged in one final pass
'''


def merge(array1, array2):
    '''
        Merges two arrays together

        Parameters:
            array1 [list]: the first array to merge
            array2 [list]: the second array to merge

        Returns:
            A merged/ordered array consisting of both arrays
            passed in

        Merge Function:
        1. Create an empty array and look at smallest values in input
        arrays
        2. While there are values we have not looked at, compare values
        between the two arrays
            a. If first array has smaller value, push that into the
            created array and move on to the next value in first array
            b. If second array has smaller value, push that into the
            created array and move on to the next value in second array
            c. If one array has been completely pushed into the created
            array, push in all remaining values from the other array

        Example: [1, 3, 5] [2, 4, 6]
        => [1, 2, 3, 4, 5, 6]
    '''
    merged = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged.append(array1[i])
            i += 1

        else:
            merged.append(array2[j])
            j += 1

    while i < len(array1):
        merged.append(array1[i])
        i += 1

    while j < len(array2):
        merged.append(array2[j])
        j += 1

    return merged


def mergeSort(array):
    '''
        Sorts an array of integers using merge sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Merge Sort
        1. Breaks up the array into halves until arrays are empty
        or have one element
        2. With these smaller arrays, merge them with the other
        sorted arrays
        3. Return the merged and sorted array

        * Breaks arrays up until they are single digits and then merge
        them all back together one after the other from smaller arrays
        to larger arrays

        Example: [10, 24, 76, 73, 72, 1, 9]
        => Splitting array: [10, 24, 76] <=> [73, 72, 1, 9]
        => Splitting arrays: [10] [24, 76] <=> [73, 72] [1, 9]
        => Splitting arrays: [10] [24] [76] <=> [73] [72] [1] [9]
        => Merging arrays: [10] [24, 76] <=> [72, 73] [1, 9]
        => Merging arrays: [10, 24, 76] <=> [1, 9, 72, 73]
        => Merging arrays: [1, 9, 10, 24, 72, 73, 76]
    '''
    if len(array) == 1 or len(array) == 0:
        return array

    else:
        mid = len(array) // 2
        left = array[0:mid]
        right = array[mid:]
        arr1 = mergeSort(left)
        arr2 = mergeSort(right)
        return merge(arr1, arr2)
