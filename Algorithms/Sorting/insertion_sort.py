#!/usr/bin/env python3
'''
    Insertion sort algorithm

    Insertion sort is when you break up the array into halves and keep
    the left half of the array sorted while you iterate each index and
    place its value into the correct spot on the left side
'''


def insertionSort(array):
    '''
        Sorts an array of integers using insertion sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Insertion Sort
        1. Start by picking second element in the array
        2. Compare the second element with the one before
        and swap if necessary
        3. Continue to next element and if it is in correct order
        iterate through the sorted portion and place it in the correct
        spot
        4. Repeat until the array is sorted

        * Builds a sorted portion of the array and inserts subsequent
        indices into the correct position in the sorted left half

        Example: [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 22, 34, 10, 19, 17]
        => [0, 2, 10, 22, 34, 19, 17]
        => [0, 2, 10, 19, 22, 34, 17]
        => [0, 2, 10, 17, 19, 22, 34]
    '''
    if len(array) == 0 or len(array) == 1:
        return array

    i = 1
    while i < len(array):
        currentVal = array[i]
        j = i - 1
        while j >= 0 and array[j] > currentVal:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = currentVal
        i += 1
    return array
