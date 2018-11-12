#!/usr/bin/env python3
'''
    Stack class file (LIFO)
'''


class Node:
    '''
        Node class for the stack structure
    '''

    def __init__(self, data):
        '''
            Initialization of the node class

            Parameters:
                data [integer]: the value of the node
        '''
        self.data = data
        self.next = None

    def __repr__(self):
        '''
            Print representation of the Node class

            Returns:
                The string representation of the node
        '''
        return '{}'.format(self.data)


class Stack:
    '''
        Stack class data structure
    '''

    def __init__(self, first=None, last=None, size=0):
        '''
            Initialization of stack class
            O(1)

            Parameters:
                first [obj]: the first element in the stack
                last [obj]: the last element in the stack
                size [int]: the size of the stack
        '''
        self.first = first
        self.last = last
        self.size = size

    def push(self, data):
        '''
            Pushes a node to the end of the stack
            O(1)

            Parameters:
                data [int]: the value of the node to add to the stack

            Returns:
                The stack instance
        '''
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            self.first.next = temp
        self.size += 1
        return self.size

    def pop(self):
        '''
            Pops off the last node of the stack and returns it
            O(1)

            Returns:
                The removed node from the stack
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
            Print representation of the stack class

            Returns:
                The string representation of the stackcd
        '''
        list = []
        current = self.first
        while current:
            list.append(current.data)
            current = current.next
        return '{}'.format(list)
