#!/usr/bin/env python3
'''
    Graph data structure implementation
    Uses an adjacency list to represent the graph

    A graph is a data structure that consists of
    vertices and edges that connect these vertices.

    They can be directional and nondirectional and can
    be used to show relationships between vertices
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


class DijkstraPriorityQueue:
    '''
        Simple priority queue to be used for Dijkstra's Shortest
        Path Algorithm
    '''

    def __init__(self):
        '''
            Instantiation of the priority queue
        '''
        self.values = []

    def enqueue(self, val, priority):
        '''
            Enqueues a value into the priority queue and sorts it
            into its proper position
        '''
        self.values.append({"val": val, "priority": priority})
        self.sort()

    def dequeue(self):
        '''
            Removes the value at the beginning of the priority queue
        '''
        return self.values.pop(0)

    def sort(self):
        '''
            Sorts the priority queue in order from smallest to largest
        '''
        self.values.sort(key=lambda x: x['priority'])


class WeightedGraph:
    '''
        Graph with weight values on each edge relationship
    '''

    def __init__(self):
        '''
            Initialization of the weighted graph class
        '''
        self.adjacencyList = {}

    def addVertex(self, vertex):
        '''
            Adds a vertex to the graph

            Parameters:
                vertex [string]: the vertex value
        '''
        if not self.adjacencyList.get(vertex):
            self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2, weight):
        '''
            Adds an edge relationship to the graph

            Parameters:
                vertex1 [string]: the first vertex string value
                vertex2 [string]: the second vertex string value
                weight [int]: the weight of the relationship

        '''
        self.adjacencyList[vertex1].append({"node": vertex2, "weight": weight})
        self.adjacencyList[vertex2].append({"node": vertex1, "weight": weight})

    def Dijkstra(self, start, finish):
        '''
            Performs Dijkstra's shortest path algorithm to find the
            shortest path between the start and finish nodes
        '''
        nodes = DijkstraPriorityQueue()
        distances = {}
        previous = {}
        path = []

        # Initial state
        # Starts the starting node at 0 distance and all others at infinity (ie
        # unknown distance)
        for vertex in self.adjacencyList:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float("inf")
            previous[vertex] = None

        # While there are vertices to visit
        while len(nodes.values):

            # Grabs the current smallest distance from priority queue
            smallest = nodes.dequeue()["val"]
            if smallest == finish:
                # Build shortest path from start to finish in reverse order
                # from finish
                while smallest is not None:
                    path.append(smallest)
                    smallest = previous[smallest]
                break

            if smallest:
                for neighbor in self.adjacencyList[smallest]:

                    # Calculate new distance to the next node
                    candidate = distances[smallest] + neighbor['weight']
                    neighborVal = neighbor['node']
                    if candidate < distances[neighborVal]:

                        # Updates the smallest distance to the neighbor
                        distances[neighborVal] = candidate

                        # Updates the path to the neighbor using smallest
                        # distance
                        previous[neighborVal] = smallest

                        # Enqueue priority queue with new priority
                        nodes.enqueue(neighborVal, candidate)

        # Reverse the path so that it starts at the beginning
        path.reverse()
        return path
