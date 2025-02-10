from enum import Enum
import math

from src.data_structures.graphs import AdjListGraph
from src.data_structures.basic_data_structures import Queue

class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class BFSNode:
    def __init__(self):
        self.predecessor = None
        self.color = Color.WHITE
        self.distance = math.inf


class BFS:
    def __init__(self, graph:AdjListGraph):
        self.__graph = graph.get_graph()
        self.__bfs_nodes = {}
        self.__search_queue = Queue()

    def __initialize_nodes(self, ):
        graph_vertices = self.__graph.keys()

        for vertex in graph_vertices:
            self.__bfs_nodes[vertex] = BFSNode()

    def run(self, search_source):
        self.__initialize_nodes()

        if search_source not in self.__bfs_nodes.keys():
            raise KeyError("Source node not in Graph!")

        self.__bfs_nodes[search_source].color = Color.GRAY
        self.__bfs_nodes[search_source].distance = 0

        self.__search_queue.add(self.__bfs_nodes[search_source])

        self.__search_queue.


def main():
    my_graph = AdjListGraph()
    # my_graph = AdjMatrixGraph()

    my_graph.add_vertice("a")
    my_graph.add_vertice("b")
    my_graph.add_vertice("c")
    my_graph.add_edge("a", "b")
    my_graph.add_edge("a", "c")
    my_graph.add_edge("b", "c")
    my_graph.add_edge("c", "b")

    print(my_graph)

if __name__ == "__main__":
    main()