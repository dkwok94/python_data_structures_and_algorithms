#!/usr/bin/env python3
'''
    Singly Linked List class
'''


class Node:
    '''
        Linked List node class
    '''

    def __init__(self, data=None, next=None):
        '''
            Linked list node initialization
            O(1)

            Parameters:
                data [int]: the value of the node
                next [obj]: the next node
        '''
        self.data = data
        self.next = next

    def __repr__(self):
        '''
            Print representation of the Node class

            Returns:
                The string representation of the node
        '''
        return '{}'.format(self.data)


class SinglyLinkedList:
    '''
        Singly linked list class
    '''

    def __init__(self, head=None, tail=None, length=0):
        '''
            Singly linked list initialization
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
            Pushes a new node to the end of the linked list
            O(1)

            Parameters:
                data [int]: the value of the node to add

            Returns:
                The linked list instance
        '''
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
        return self

    def pop(self):
        '''
            Removes the last node of the linked list and returns it
            O(n)

            Returns:
                The removed node
        '''
        current = self.head
        newTail = current
        if self.head is None:
            return None
        while(current.next):
            newTail = current
            current = current.next
        self.tail = newTail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        '''
            Removes a node from the beginning of the linked list
            O(1)

            Returns:
                The removed node
        '''
        oldHead = self.head
        if self.head is None:
            return None
        self.head = oldHead.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return oldHead

    def unshift(self, data):
        '''
            Inserts a new node to the beginning of the linked list
            O(1)

            Parameters:
                data [int]: the value of the node to add

            Returns:
                The linked list instance
        '''
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self

    def get(self, index):
        '''
            Retrieves a node by its position in the linked list
            O(n)

            Parameters:
                index [int]: the index to get the value of
            
            Returns:
                The node at the specified index
        '''
        count = 0
        current = self.head
        if index < 0 or index >= self.length:
            return None
        while(count != index):
            current = current.next
            count += 1
        return current

    def set(self, index, data):
        '''
            Changes the value of a node at a specific position
            O(n)

            Parameters:
                index [int]: the index to set the value
                data [int]: the new value of the node

            Returns:
                True or False regarding set success
        '''
        node = self.get(index)
        if node:
            node.data = data
            return True
        return False

    def insert(self, index, data):
        '''
            Adds a node at a specific position in the linked list
            O(n)

            Parameters:
                index [int]: the index to insert the node to
                data [int]: the data contained in the new node

            Returns:
                True or False regarding insert success
        '''
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            self.push(data)
            return True
        if index == 0:
            self.unshift(data)
            return True

        prevNode = self.get(index - 1)
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.length += 1
        return True

    def remove(self, index):
        '''
            Removes a node from a specific position of linked list
            O(n)

            Parameters:
                index [int]: the index to remove from

            Returns:
                The node that was removed
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        prevNode = self.get(index - 1)
        removedNode = prevNode.next
        prevNode.next = removedNode.next
        self.length -= 1
        return removedNode

    def reverse(self):
        '''
            Reverses a linked list in place
            O(n)

            Returns:
                The reversed linked list instance
        '''
        node = self.head
        self.head = self.tail
        self.tail = node
        next = None
        prev = None
        for _ in range(0, self.length):
            next = node.next
            node.next = prev
            prev = node
            node = next
        return self

    def __repr__(self):
        '''
            Linked list print representation
            O(n)

            Returns:
                The string representation of the linked list
        '''
        list = []
        current = self.head
        while current:
            list.append(current.data)
            current = current.next
        return '{}'.format(list)
