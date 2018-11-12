#!/usr/bin/env python3
'''
    Linear search algorithm
'''


def linearSearch(array, element):
    '''
        Searches an array of integers using linear search

        Parameters:
            array [list]: the array to search
            element [integer]: the element to search for

        Returns:
            The index of where the element is found in the array
    '''
    for i in range(0, len(array)):
        if array[i] == element:
            return i
    return None
