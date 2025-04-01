from graph import Graph

def main():
    myGraph = Graph()

    # Preguntar si el grafo es dirigido
    isDirected = input("Is the graph directed? (Y/N): ").strip().upper()
    myGraph.setDirected(isDirected == "Y")

    # Configurar número de nodos
    nodeCount = int(input("How many nodes does the graph have? "))
    myGraph.setNodeQuantity(nodeCount)
    myGraph.printMatrix()

    # Agregar rutas (aristas)
    addEdge = input("Do you want to add an edge? (Y/N): ").strip().upper()
    while addEdge == "Y":
        startNode = int(input("Enter start node: "))
        endNode = int(input("Enter end node: "))
        myGraph.addEdge(startNode, endNode)
        myGraph.printMatrix()
        addEdge = input("Do you want to add another edge? (Y/N): ").strip().upper()

    # Mostrar nodos adyacentes
    nodeToCheck = int(input("Which node's adjacent list do you want to see? "))
    myGraph.listAdjacentNodes(nodeToCheck)

    # Ejemplo de ordenamiento topológico
    # myGraph.setMatrix([
    #     [0, 1, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 1, 1],
    #     [0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 1]
    # ])
    
    print("++++++ Topological Sort ++++++")
    myGraph.topologicalSort()

    print("********* Depth First Search *********")
    myGraph.depthFirstSearch(0)

if __name__ == "__main__":
    main()
