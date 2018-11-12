#!/usr/bin/env python3
'''
    Hash table implementation
'''


def hash(key, arrayLen):
    '''
        Hashes a key with respect to an array length
    '''
    total = 0
    for char in key:
        value = ord(char) - 96
        total = (total + value) % arrayLen
    return total
