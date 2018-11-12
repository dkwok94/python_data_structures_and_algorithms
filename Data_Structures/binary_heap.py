#!/usr/bin/env python3
'''
    Binary heap class file using an array
'''


class MaxBinaryHeap:
    '''
        Max Binary Heap data structure class
    '''

    def __init__(self, values=[]):
        '''
            Initialization of the max binary heap structure

            Parameters:
                values [list]: the binary heap values
        '''
        self.values = values

    def __repr__(self):
        '''
            Print representation of binary heap structure

            Returns:
                The string representation of the heap
        '''
        return '{}'.format(self.values)

    def insert(self, value):
        '''
            Inserts a value into a binary heap
            O(logn)

            Parameters:
                value [integer]: the value to add to the heap
        '''
        self.values.append(value)
        self.bubbleUp()

    def bubbleUp(self):
        '''
            Bubbles a value into position after insertion
        '''
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]
            if element <= parent:
                break
            self.values[parentIdx], self.values[idx] = element, parent
            idx = parentIdx

    def extractMax(self):
        '''
            Removes the maximum value of the binary heap
            (ie. removes the root of the binary heap)
            O(logn)

            Returns:
                The maximum value of the heap
        '''
        if len(self.values) == 0:
            return None
        max = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sinkDown()
        return max

    def sinkDown(self):
        '''
            Sinks down the value replacing the maximum number
            for the function extractMax()
        '''
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            swap = None
            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild > element:
                    swap = leftChildIdx
            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swap is None and rightChild > element) or (
                        swap is not None and rightChild > leftChild):
                    swap = rightChildIdx
            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


class MinBinaryHeap:
    '''
        Min Binary Heap data structure class
    '''

    def __init__(self, values=[]):
        '''
            Initialization of the min binary heap structure

            Parameters:
                values [list]: the binary heap values
        '''
        self.values = values

    def __repr__(self):
        '''
            Print representation of binary heap structure

            Returns:
                The string representation of the heap
        '''
        return '{}'.format(self.values)

    def insert(self, value):
        '''
            Inserts a value into a binary heap
            O(logn)

            Parameters:
                value [integer]: the value to add to the heap
        '''
        self.values.append(value)
        self.bubbleUp()

    def bubbleUp(self):
        '''
            Bubbles a value into position after insertion
        '''
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]
            if element >= parent:
                break
            self.values[parentIdx], self.values[idx] = element, parent
            idx = parentIdx

    def extractMin(self):
        '''
            Removes the minimum value of the binary heap
            (ie. removes the root of the binary heap)
            O(logn)

            Returns:
                The minimum value of the heap
        '''
        if len(self.values) == 0:
            return None
        min = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sinkDown()
        return min

    def sinkDown(self):
        '''
            Sinks down the value replacing the minimum number
            for the function extractMin()
        '''
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            swap = None
            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild < element:
                    swap = leftChildIdx
            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swap is None and rightChild < element) or (
                        swap is not None and rightChild < leftChild):
                    swap = rightChildIdx
            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap
