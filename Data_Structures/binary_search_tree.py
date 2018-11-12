#!/usr/bin/env python3
'''
    Binary search tree (BST) class file
'''


class Node:
    '''
        Node class for binary search tree
    '''

    def __init__(self, value, left=None, right=None):
        '''
            Initialization of Node class for the BST

            Parameters:
                value [integer]: the value of the node
                left [obj]: the left child of the node
                right [obj]: the right child of the node
        '''
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        '''
            Print representation of a node of the BST

            Returns:
                The string representation of the tree
        '''
        return '{}'.format(self.value)


class BinarySearchTree:
    '''
        Binary Search Tree class
    '''

    def __init__(self, root=None):
        '''
            Initialization of the binary search tree structure

            Parameters:
                root [obj]: the root node of the tree
        '''
        self.root = root

    def __repr__(self):
        '''
            Print representation of the binary search tree

            Returns:
                The string representation of the tree
        '''
        tree = []

        def fillTree(root, subtree):
            '''
                Creates a list of lists representation of the BST
                The lists are of the following format:
                [root, [left_subtree], [right_subtree]]

                Parameters:
                    root [obj]: the root of the tree
                    root [list]: the subtree of the root

                Returns:
                    String representation of the tree

                Example:
                            41
                          |    |
                         20    65
                        |  |  |
                       11 32  50

                ==> [41,
                    [20, [11, [], []], [32, [], []]],
                    [65, [50, [], []], []]]
            '''
            if root is not None:
                subtree.append(root.value)
                subtree.append([])
                subtree.append([])
            if root.left:
                fillTree(root.left, subtree[1])
            if root.right:
                fillTree(root.right, subtree[2])
        if self.root is not None:
            fillTree(self.root, tree)
        return '{}'.format(tree)

    def insert(self, value):
        '''
            Inserts a node into the BST
            O(logn)

            Parameters:
                value [integer]: the value to add to the BST

            Returns:
                The BST instance
        '''
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left is None:
                        current.left = newNode
                        return self
                    current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        return self
                    current = current.right

    def contains(self, value):
        '''
            Returns whether a value is in the BST
            O(logn)

            Parameters:
                value [integer]: the value to check in the BST

            Returns:
                True or False based on whether the value is found
        '''
        if self.root is None:
            return False
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def find(self, value):
        '''
            Finds a node with a specified value in the BST
            O(logn)

            Parameters:
                value [integer]: the value to search for in BST

            Returns:
                The node that contains the value
        '''
        if self.root is None:
            return None
        current = self.root
        found = False
        while current and found is False:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        if found is False:
            return None
        return current

    # Tree traversal algorithms
    def breadthFirstSearch(self):
        '''
            Traverses the tree using breadth first search
            Traversal method for unsorted binary tree
            O(n)

            Returns:
                The BST in proper order
        '''
        data = []
        queue = []
        node = self.root
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            data.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    def depthFirstPreorder(self):
        '''
            Depth first preorder traversal
            For traversal of unsorted binary trees
            Traverse root, traverse left, traverse right
            O(n)
            
            Returns:
                A list of all nodes in order
        '''
        data = []

        def traverse(node):
            '''
                Traverses the tree in a specific order

                Parameters:
                    node [obj]: the root node of the subtree
            '''
            data.append(node)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data

    def depthFirstPostorder(self):
        '''
            Depth first preorder traversal
            For traversal of unsorted binary tree
            Traverse left, traverse right, traverse root
            O(n)

            Returns:
                A list of all nodes in order
        '''
        data = []

        def traverse(node):
            '''
                Traverses the tree in a specific order

                Parameters:
                    node [obj]: the root node of the subtree
            '''
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node)
        traverse(self.root)
        return data

    def depthFirstInorder(self):
        '''
            Depth first inorder traversal
            For traversal of unsorted binary tree
            Traverse left, traverse root, traverse right
            O(n)

            
            Returns:
                A list of all nodes in order
        '''
        data = []

        def traverse(node):
            '''
                Traverses the tree in a specific order

                Parameters:
                    node [obj]: the root node of the subtree
            '''
            if node.left:
                traverse(node.left)
            data.append(node)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data
