#!/usr/bin/env python3
'''
    Queue class file (FIFO)
'''


class Node:
    '''
        Node class for the queue data structure
    '''

    def __init__(self, data):
        '''
            Initialization of Node class for queue

            Parameters:
                data [integer]: the value of the node
        '''
        self.data = data
        self.next = None

    def __repr__(self):
        '''
            Print representation of the Node
        '''
        return '{}'.format(self.data)


class Queue:
    '''
        Queue data structure class
    '''

    def __init__(self, first=None, last=None, size=0):
        '''
            Initialization of the queue data structure

            Parameters:
                first [obj]: the beginning of the queue
                last [obj]: the end of the queue
                size [int]: the size of the queue
        '''
        self.first = first
        self.last = last
        self.size = size

    def enqueue(self, data):
        '''
            Adds a node to the end of the queue
            O(1)

            Parameters:
                data [integer]: the value of the node added

            Returns:
                The size of the queue
        '''
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1
        return self.size

    def dequeue(self):
        '''
            Removes a node from the beginning of the queue
            O(1)

            Returns:
                The node removed
        '''
        if self.first is None:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        temp.next = None
        self.size -= 1
        return temp.data

    def __repr__(self):
        '''
            Print representation of the queue data structure

            Returns:
                String representation of the queue
        '''
        list = []
        current = self.first
        while current:
            list.append(current.data)
            current = current.next
        return '{}'.format(list)
