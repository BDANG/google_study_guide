import sys
sys.path.insert(0, "..")
from graphs import MatrixGraph
import Dijkstra
if __name__ == "__main__":
    # init a matrix graph with 5 vertices

    #matrixG = MatrixGraph(5)
    #matrixG.populate_matrix([[0,1,2], [0,3,4], [0,4,1], [2,3,2], [1,2,3], [1,4,1], [3,4,4]])

    matrixG1 = MatrixGraph(8, [[0, 1, 2],
                               [0, 3, 4],
                               [0,2,1],
                               [1,4,3],
                               [2, 3, 2],
                               [2, 6, 10],
                               [3, 4, 2],
                               [3, 5, 1],
                               [5, 6, 2],
                               [5, 7, 6],
                               [6,7,3]], directed=True)

    print(Dijkstra.path_and_value(matrixG1, 0, 7))

    print(Dijkstra.path(matrixG1, 1, 6))


    matrixG2 = MatrixGraph(7, [[0, 1, 2],
                               [0, 2, 3],
                               [1, 3, 10],
                               [2, 4, 8],
                               [3, 5, 6],
                               [4, 5, 4],
                               [5, 6, 3]
                              ])
    print(Dijkstra.path_and_value(matrixG2, 0, 6))
