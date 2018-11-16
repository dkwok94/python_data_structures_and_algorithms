#!/usr/bin/env python3
'''
    Heap sort algorithm

    Heap sort constructs a maximum heap out of the array to sort and
    continually places the root of the heap into the end of the array
    since that is where the maximum element is.

    It then decreases the end of the array by one so that the most
    recent swap to the end is not counted (ie. the max of each subarray
    is in the correct position after each iteration)
'''


def heapify(array, start, end):
    '''
        Creates a maximum binary heap in place using an input array
        and considering that the rest of the array is already a heap
        except for the starting index (puts the element at the first
        index in correct position)

        Parameters:
            array [list]: the array to heapify
            start [int]: the starting index of the subarray
            end [int]: the ending index of the subarray

        Returns:
            None/Void - all operations occur in place

        Example:
        [4, 15, 20, 10, 9, 16]
        => [20, 15, 4, 10, 9, 16]
        => [20, 15, 16, 10, 9, 4]
    '''
    maxIdx = start
    leftChildIdx = 2 * start + 1
    rightChildIdx = 2 * start + 2

    if leftChildIdx <= end and array[leftChildIdx] > array[maxIdx]:
        maxIdx = leftChildIdx

    if rightChildIdx <= end and array[rightChildIdx] > array[maxIdx]:
        maxIdx = rightChildIdx

    if maxIdx != start:
        array[start], array[maxIdx] = array[maxIdx], array[start]
        heapify(array, maxIdx, end)
    return array


def build_max_heap(array):
    '''
        Builds the initial maximum binary heap for use in the binary
        heap sort function

        Parameters:
            array [list]: the array to build the heap from

        Returns:
            The array in the form of a binary heap

        1. Start at last index that has children
        2. Swap the value here with the largest child
        3. Go to the previous index
        4. Repeat until you get to the root

        Example:
        [15, 20, 10, 16, 4, 9, 7]
        => start at index 2
        [15, 20, 10, 16, 4, 9, 7]

        => go to index 1
        [15, 20, 10, 16, 4, 9, 7]

        => go to index 0
        [20, 16, 10, 15, 4, 9, 7]
    '''
    lastParent = (len(array) // 2) - 1
    while lastParent >= 0:
        heapify(array, lastParent, len(array) - 1)
        lastParent -= 1
    return array


def heapSort(array):
    '''
        Sorts an array of integers using heap sort by utilizing
        a progressively smaller max heap

        Max Heap: a structure in which every parent is greater than its
        children

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Heap Sort:
        1. Heapify the initial array to build a max heap
        2. Swap the first element in the array with the last element
        since the first element is the largest number in a max heap
        3. Heapify the array from 0 to one less than the last index
        4. Repeat the above recursively with progressively smaller array
        window
    '''
    array = build_max_heap(array)
    end = len(array) - 1
    while end > 0:
        array[0], array[end] = array[end], array[0]
        end -= 1
        heapify(array, 0, end)
    return array
