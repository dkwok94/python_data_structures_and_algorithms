#!/usr/bin/env python3
'''
    Priority Queue data structure class file
'''


class Node:
    '''
        Priority queue node class
    '''

    def __init__(self, value, priority):
        '''
            Initialization of priority queue node

            Parameters:
                value [string, int]: the value of the node
                priority [integer]: the priority of the node
        '''
        self.value = value
        self.priority = priority

    def __repr__(self):
        '''
            Print representation of priority queue node

            Returns:
                The string format of the node
        '''
        return '[Value: {}, Priority: {}]'.format(self.value, self.priority)


class PriorityQueue:
    '''
        Priority queue class using MinBinaryHeap structure
    '''

    def __init__(self, values=[]):
        '''
            Initialization of priority queue class

            Parameters:
                values [list]: the values of the heap
        '''
        self.values = values

    def __repr__(self):
        '''
            Print representation of binary heap structure

            Returns:
                The string format of the heap
        '''
        return '{}'.format(self.values)

    def enqueue(self, value, priority):
        '''
            Inserts a value into a binary heap

            Parameters:
                value [string, int]: the value of the node added
                priority [int]: the priority of the node added
        '''
        newNode = Node(value, priority)
        self.values.append(newNode)
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
            if element.priority >= parent.priority:
                break
            self.values[parentIdx], self.values[idx] = element, parent
            idx = parentIdx

    def dequeue(self):
        '''
            Removes the min value of the binary heap
            (ie. removes the root of the binary heap)

            Returns:
                The minimum value
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
                if leftChild.priority < element.priority:
                    swap = leftChildIdx
            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swap is None and rightChild.priority < element.priority) or (
                        swap is not None and rightChild.priority < leftChild.priority):
                    swap = rightChildIdx
            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap
