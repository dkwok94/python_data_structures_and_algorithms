#!/usr/bin/env python3
'''
    Radix sort algorithm
'''


import math

def getDigit(num, place):
    '''
        Gets the digit in number at a given place value

        Parameters:
            num [int]: the number to get digits of
            place [int]: the place value to get

        Returns:
            The digit at the specified place value
    '''
    if place == 0:
        multiplier = 1
    else:
        multiplier = 10 ** place

    return (num // multiplier) % 10

def digitCount(num):
    '''
        Returns the number of digits in the number

        Parameters:
            num [int]: the number to count the digits of

        Returns:
            The number of digits in the number passed in
    '''
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1

def mostDigits(nums):
    '''
        Returns the number of digits in the largest number in the list

        Parameters:
            nums [list]: a list of numbers

        Returns:
            The number of digits in the largest number of the list
    '''
    maxDigits = 0
    for i in range(0, len(nums)):
        maxDigits = max(maxDigits, digitCount(nums[i]))
    return maxDigits

def radixSort(array):
    '''
        Sort an array of integers using radix sort

        Parameters:
            array [list]: the array to sort

        Returns:
            The sorted array

        Radix Sort:

    '''
    maxDigits = mostDigits(array)
    for place in range(0, maxDigits):
        buckets = [[] for i in range(0, 10)]
        for num in array:
            buckets[getDigit(num, place)].append(num)
        array = [num for bucket in buckets for num in bucket]
    return array