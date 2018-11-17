#!/usr/bin/env python3
'''
    Shell sort algorithm

    Shell sort is a bunch of insertion sorts on subarrays
    using an incremental gap that gets smaller each iteration
    until the gap is 1.
'''


def shellSort(array):
    '''
        Sorts an array of integers using shell sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Shell sort:
        1. Calculate the gap as half of the array length
        2. Do an insertion sort with this half array
            a. Start at the index after the first one
            b. If the value here is less than the one before it,
            then swap them
            c. Otherwise, iterate up and compare the new value with
            all values going down
        3. Calculate the next gap length by taking the previous
        gap length and divide by 2
        4. Repeat
    '''
    gap = len(array) // 2
    while gap != 0:

        # Insertion sort with gap increment
        i = 0
        while i <= len(array) - 1:
            currentVal = array[i]
            if i - gap >= 0:
                j = i - gap
                while j >= 0 and array[j] >= currentVal:
                    array[j + gap] = array[j]
                    j -= gap
                array[j + gap] = currentVal
            i += gap
        ###

        gap //= 2
    return array
