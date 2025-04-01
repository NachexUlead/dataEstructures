from queue import Queue

class Graph:
    def __init__(self):
        self.__matrix = []
        self.__isDirected = False

    def isDirected(self):
        return self.__isDirected

    def setDirected(self, directed: bool):
        self.__isDirected = directed

    def setMatrix(self, matrix):
        self.__matrix = matrix

    def setNodeQuantity(self, nodeQty: int):
        self.__matrix = [[0 for _ in range(nodeQty)] for _ in range(nodeQty)]

    def printMatrix(self):
        for row in self.__matrix:
            print(" ".join(map(str, row)))

    def addEdge(self, start, end):
        self.__matrix[start][end] = 1
        if not self.__isDirected:
            self.__matrix[end][start] = 1

    def listAdjacentNodes(self, node):
        adjList = self.__matrix[node]
        for index, value in enumerate(adjList):
            if value == 1:
                print(f"Node {node} is connected to Node {index}")

    def breadthFirstSearch(self, start):
        queue = Queue()
        processed = [0] * len(self.__matrix)
        levelList = [len(self.__matrix) + 1000] * len(self.__matrix)
        levelList[start] = 0
        processed[start] = 1
        queue.enqueue(start)
        while not queue.isEmpty():
            currentNode = queue.dequeue()
            adjList = self.__matrix[currentNode]
            for pos, isAdjacent in enumerate(adjList):
                if isAdjacent == 1 and processed[pos] == 0:
                    processed[pos] = 1
                    levelList[pos] = levelList[currentNode] + 1
                    queue.enqueue(pos)
            processed[currentNode] = 2
        print(levelList)

    def depthFirstSearch(self, start):
        visited = set()
        self.__dfsUtil(start, visited)

    def __dfsUtil(self, node, visited):
        visited.add(node)
        print(f"{node}", end=" ")
        for pos, isAdjacent in enumerate(self.__matrix[node]):
            if isAdjacent == 1 and pos not in visited:
                self.__dfsUtil(pos, visited)

    def topologicalSort(self):
        visited = set()
        stack = []
        for i in range(len(self.__matrix)):
            if i not in visited:
                self.__topoSortUtil(i, visited, stack)
        print("Topological Order:", stack[::-1])

    def __topoSortUtil(self, node, visited, stack):
        visited.add(node)
        for pos, isAdjacent in enumerate(self.__matrix[node]):
            if isAdjacent == 1 and pos not in visited:
                self.__topoSortUtil(pos, visited, stack)
        stack.append(node)
