#!/usr/bin/env python3
'''
    Selection sort algorithm

    Selection sort works so you have two halves of the array:
    the left side is sorted via minimum values and right side
    is not.

    Each time you iterate through the array, you keep track of
    the minimum value and swap this value with the current
    boundary index between left half and right half until sorted
'''


def selectionSort(array):
    '''
        Sorts an array of integers using selection sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Selection Sort:
        1. Store the first element as the minimum value
        2. Loop through the next items until we get to the end
        or a new minimum is found
        3. If smaller number is found, make that the new minimum
        and continue until the end of the array
        4. If the minimum is not the initial index value, swap them
        5. Repeat with next element until array is sorted

        * Builds sorted array on the left side with small values to
        larger values

        Example: [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 34, 22, 10, 19, 17]
        => [0, 2, 10, 22, 34, 19, 17]
        => [0, 2, 10, 17, 34, 19, 22]
        => [0, 2, 10, 17, 19, 34, 22]
        => [0, 2, 10, 17, 19, 22, 34]
    '''
    if len(array) == 0 or len(array) == 1:
        return array

    for i in range(0, len(array) - 1):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array
