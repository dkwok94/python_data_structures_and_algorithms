#!/usr/bin/env python3
'''
    Graph data structure implementation
    Uses an adjacency list to represent the graph
'''


class Graph:
    '''
        Graph data structure class (Undirected Graph)
    '''

    def __init__(self):
        '''
            Initialization of the graph structure
            using an adjacency list
        '''
        self.adjacencyList = {}

    def addVertex(self, vertex):
        '''
            Adds a vertex to the adjacency list graph
            O(1)

            Parameters:
                vertex [string]: the key of the new vertex
        '''
        if not self.adjacencyList.get(vertex):
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        '''
            Adds an edge to the adjacency list graph
            O(1)

            Parameters:
                vertex1 [string, int]: one end of the edge
                vertex2 [string, int]: the other end of the edge
        '''
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        '''
            Removes an edge from the adjacency list graph

            Parameters:
                vertex1 [string, int]: one end of the edge
                vertex2 [string, int]: the other end of the edge
        '''
        self.adjacencyList[vertex1] = [
            edge for edge in self.adjacencyList[vertex1] if edge != vertex2]
        self.adjacencyList[vertex2] = [
            edge for edge in self.adjacencyList[vertex2] if edge != vertex1]

    def removeVertex(self, vertex):
        '''
            Removes a vertex from the adjacency list graph

            Parameters:
                vertex [string]: the vertex to remove
        '''
        while len(self.adjacencyList[vertex]):
            adjVert = self.adjacencyList[vertex].pop()
            self.removeEdge(vertex, adjVert)
        del self.adjacencyList[vertex]

    def depthFirstRec(self, start):
        '''
            Traverses the graph via depth first traversal using recursion

            Parameters:
                start [string]: the starting point of the traversal

            Returns:
                A list representing the order of traversal of vertices
        '''
        result = []
        visited = {}
        adjacencyList = self.adjacencyList

        def DFS(vertex):
            '''
                Depth first helper function

                Parameters:
                    vertex [string]: the current vertex being
                    traversed
            '''
            if not vertex:
                return None
            visited[vertex] = True
            result.append(vertex)
            for neighbor in adjacencyList[vertex]:
                if not visited.get(neighbor):
                    DFS(neighbor)
        DFS(start)
        return result

    def depthFirstIter(self, start):
        '''
            Performs depth first traversal using an iterative
            algorithm

            Parameters:
                start [string]: the starting key for the traversal

            Returns:
                An array containing the traversal order
        '''
        visited = {}
        results = []
        stack = [start]

        visited[start] = True
        while len(stack):
            currentVertex = stack.pop()
            results.append(currentVertex)

            for neighbor in self.adjacencyList[currentVertex]:
                if not visited.get(neighbor):
                    visited[neighbor] = True
                    stack.append(neighbor)
        return results

    def breadthFirst(self, start):
        '''
            Traverses the graph using breath first search
            algorithm

            Parameters:
                start [string]: The starting key to use for traversal

            Returns:
                An array showing the traversal order
        '''
        queue = [start]
        results = []
        visited = {}
        visited[start] = True

        while len(queue):
            currentVertex = queue.pop(0)
            results.append(currentVertex)

            for neighbor in self.adjacencyList[currentVertex]:
                if not visited.get(neighbor):
                    visited[neighbor] = True
                    queue.append(neighbor)
        return results
