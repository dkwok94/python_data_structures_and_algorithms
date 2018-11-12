#!/usr/bin/env python3
'''
    Doubly linked list class file
'''


class Node:
    '''
        Linked list node class
    '''

    def __init__(self, data, next=None, prev=None):
        '''
            Initialization of doubly linked list node
            O(1)

            Parameters:
                data [integer]: the value of the node
                next [obj]: the next node
                prev [obj]: the previous node
        '''
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        '''
            Print representation of the Node class

            Returns:
                The string representation of the linked list
        '''
        return '{}'.format(self.data)


class DoublyLinkedList:
    '''
        Doubly linked list class
    '''

    def __init__(self, head=None, tail=None, length=0):
        '''
            Initialization of doubly linked list instance
            O(1)

            Parameters:
                head [obj]: the head of the linked list
                tail [obj]: the tail of the linked list
                length [integer]: the length of the linked list
        '''
        self.head = head
        self.tail = tail
        self.length = length

    def push(self, data):
        '''
            Inserts a node at the end of the linked list
            O(1)

            Parameters:
                data [integer]: the data of the node to add

            Returns:
                The linked list instance
        '''
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        '''
            Removes a node from the end of the linked list
            O(1)

            Returns:
                The node that was removed
        '''
        poppedTail = self.tail
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = poppedTail.prev
            self.tail.next = None
            poppedTail.prev = None
        self.length -= 1
        return poppedTail

    def shift(self):
        '''
            Removes a node from the beginning of the linked list
            O(1)

            Returns:
                The node that was removed
        '''
        if self.head is None:
            return None
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next
            self.head.prev = None
            oldHead.next = None
        self.length -= 1
        return oldHead

    def unshift(self, data):
        '''
            Adds a node at the beginning of the linked list
            O(1)

            Parameters:
                data [integer]: the data of the node to add

            Returns:
                The linked list instance
        '''
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    def get(self, index):
        '''
            Accesses a node in a linked list by its position
            O(n)

            Parameters:
                index [integer]: the index to get the value of

            Returns:
                The node at the specified index
        '''
        if index < 0 or index >= self.length:
            return None
        if index <= self.length // 2:
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
        else:
            count = self.length - 1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
        return current

    def set(self, index, data):
        '''
            Replaces the value of the node at a specified position
            O(n)

            Parameters:
                index [integer]: the index to set the value of
                data [integer]: the new value of the index

            Returns:
                True or False based on set success
        '''
        node = self.get(index)
        if node:
            node.data = data
            return True
        return False

    def insert(self, index, data):
        '''
            Adds a new node at a specified position in the linked list
            O(n)

            Parameters:
                index [integer]: the index to insert to
                data [integer]: the value of the node to insert

            Returns:
                True or False on insertion success
        '''
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.unshift(data)
            return True
        if index == self.length:
            self.push(data)
            return True

        newNode = Node(data)
        beforeNode = self.get(index - 1)
        afterNode = beforeNode.next
        beforeNode.next = newNode
        newNode.prev = beforeNode
        newNode.next = afterNode
        afterNode.prev = newNode
        self.length += 1
        return True

    def remove(self, index):
        '''
            Removes a node at a specific position in the linked list
            O(n)

            Parameters:
                index [integer]: the index of the node to remove

            Returns:
                The node that is removed
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()

        removeNode = self.get(index)
        prevNode = removeNode.prev
        nextNode = removeNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        removeNode.next = None
        removeNode.prev = None
        self.length -= 1
        return removeNode

    def print_reverse(self):
        '''
            Prints the doubly linked list in reverse

            Returns:
                The reversed linked list
        '''
        list = []
        current = self.tail
        while current:
            list.append(current.data)
            current = current.prev
        return list

    def __repr__(self):
        '''
            Print representation of doubly linked list

            Returns:
                The string format of the linked list
        '''
        list = []
        current = self.head
        while current:
            list.append(current.data)
            current = current.next
        return '{}'.format(list)
