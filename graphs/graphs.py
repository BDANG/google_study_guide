class Graph:
    def __init__(self, numVertices, numEdges, directed):
        self.numVertices = numVertices
        self.numEdges = numEdges
        self.directed = directed



class MatrixGraph(Graph):
    def __init__(self, numVertices, edgeList=None, directed=False):
        '''
        If weighted, assumes that none of the weights are 0!
        '''
        self.matrix = [[0 for i in range(numVertices)] for i in range(numVertices)]

        if edgeList:
            Graph.__init__(self, numVertices, len(edgeList), directed)
            self.populate_matrix(edgeList)
        elif not edgeList:
            Graph.__init__(self, numVertices, 0, directed)



    def populate_matrix(self, edges):
        weighted = False
        numValidEdges = 0
        for edge in edges:
            fro = edge[0]
            to = edge[1]
            weight = 1

            if len(edge) == 3:
                weight = edge[2]

            if self.directed:
                self.matrix[fro][to] = weight
            else:
                self.matrix[fro][to] = weight
                self.matrix[to][fro] = weight

            numValidEdges+=1
        self.numEdges = numValidEdges

    def get_neighbors(self, vertexNum):
        neighbors = []
        others = self.matrix[vertexNum]
        for vertex in range(len(others)):
            weight = others[vertex]
            if weight != 0:
                neighbors.append((vertex, weight))
        return neighbors

    def is_neighbor(self, vertexNum, neighbor):
        return self.get_neighbors(vertexNum)[neighbor]
