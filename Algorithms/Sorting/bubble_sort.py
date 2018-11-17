#!/usr/bin/env python3
'''
    Bubble sort algorithm

    Bubble sort iterates through the array and swaps neighboring
    indices so that the maximum ends up on the right side, in place.

    Then, it goes through again with a smaller subarray and does the
    same thing. 
'''


def bubbleSort(array):
    '''
        Sorts an array of integers using bubble sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Bubble Sort:
        1. Loop an index called limit from the end of the array
        to the beginning
        2. Loop an index called i in the inner loop from 0 to limit - 1
        3. At each index i, compare arr[i] and arr[i + 1] and swap them
        if [i] is greater than [i + 1]
        4. Return the array

        * Builds a sorted array on the right side from max values
        downwards

        Example: [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 22, 34, 10, 19, 17]
        => [0, 2, 22, 10, 34, 19, 17]
        => [0, 2, 22, 10, 19, 34, 17]
        => [0, 2, 22, 10, 19, 17, 34]
        => [0, 2, 10, 22, 19, 17, 34]
        => [0, 2, 10, 19, 22, 17, 34]
        => [0, 2, 10, 19, 17, 22, 34]
        => [0, 2, 10, 17, 19, 22, 34]
    '''
    limit = len(array) - 1
    while limit > 0:
        noSwaps = True
        i = 0
        while i < limit:
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                noSwaps = False
                print(array)
            i += 1
        limit -= 1
        if noSwaps is True:
            break
    return array
