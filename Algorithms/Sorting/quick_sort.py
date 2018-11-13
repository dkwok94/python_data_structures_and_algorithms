#!/usr/bin/env python3
'''
    Quick sort algorithm
'''


def partition(array, start, end):
    '''
        Selects a pivot and organizes values greater than the pivot
        on the right and values less than the pivot on the left

        Parameters:
            array [list]: the array to sort
            start [int]: the starting index
            end [int]: the ending index

        Returns:
            The pivot index

        Pivot Helper Function
        1. Grab pivot from start of array
        2. Store current pivot index in a variable
        3. Loop through array from start to end
            a. If pivot is greater than current element, increment pivot
            index variable and swap current element with pivot index element
        4. Swap the starting element with the pivot index
        5. Return the pivot index
    '''
    pivot = array[start]
    swapIdx = start
    i = start + 1
    while i < len(array):
        if pivot > array[i]:
            swapIdx += 1
            array[i], array[swapIdx] = array[swapIdx], array[i]
        i += 1
    array[start], array[swapIdx] = array[swapIdx], array[start]
    return swapIdx


def quickSort(array):
    '''
        Sorts an array of integers using quick sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Quick Sort:
        1. Call the pivot helper function which organizes items
        less than the pivot on the left of the pivot and items
        greater than the pivot on the right and returns the pivot index
        2. When the helper returns, call the helper function on the left
        of the pivot index returned and to the right of the pivot index
        returned
        3. End the recursion when the subarray is 1 or 0 elements large

        * Takes a pivot and places all elements less than it on the left
        and all elements larger than it on the right so that at some frame
        of the recursion, each pivot is in the correct location
    '''
    def quickSortHelper(array, left, right):
        '''
            Implements the quick sort functionality to allow
            specification of left and right indices

            Parameters:
                array [list]: the array to sort
                left [int]: the left index of the subarray
                right [int]: the right index of the subarray
        '''
        if left < right:
            pivotIdx = partition(array, left, right)
            quickSortHelper(array, left, pivotIdx - 1)
            quickSortHelper(array, pivotIdx + 1, right)

    quickSortHelper(array, 0, len(array) - 1)
    return array
