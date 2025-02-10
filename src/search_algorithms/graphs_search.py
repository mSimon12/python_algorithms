import math

from src.data_structures.graphs import AdjListGraph
from src.data_structures.basic_data_structures import Queue


class BFSNode:
    def __init__(self, node_key):
        self.key = node_key
        self.predecessor = None
        self.visited = False
        self.distance = math.inf


class BFS:
    """
        Breadth-First Search class to provide graph the shortest paths
    """
    def __init__(self, graph:AdjListGraph):
        self.__graph = graph.get_graph()
        self.__bfs_source = None
        self.__bfs_nodes = {}

    def __initialize_nodes(self):
        """
            Initialize the nodes for each vertex from the graph
        :return: None
        """
        graph_vertices = self.__graph.keys()

        for vertex in graph_vertices:
            self.__bfs_nodes[vertex] = BFSNode(vertex)

    def run(self, search_source):
        """
            Execute the BFS search
        :param search_source: start point for doing the search for other vertices from graph
        :return: Dictionary with nodes from the graph
        """
        self.__initialize_nodes()
        self.__bfs_source = search_source

        if search_source not in self.__bfs_nodes.keys():
            raise KeyError("Source node not in Graph!")

        self.__bfs_nodes[search_source].visited = True
        self.__bfs_nodes[search_source].distance = 0

        search_queue = Queue()
        search_queue.add(search_source)

        while not search_queue.is_empty():
            node_key = search_queue.remove()
            node = self.__bfs_nodes[node_key]
            for neighbor_key in self.__graph[node_key]:
                neighbor_node = self.__bfs_nodes[neighbor_key]
                if not neighbor_node.visited:
                    neighbor_node.visited = True
                    neighbor_node.distance = node.distance + 1
                    neighbor_node.predecessor = node
                    search_queue.add(neighbor_key)

        return self.__bfs_nodes

    def get_shortest_path(self, source, target):
        """
            Get the shortest path from source to target
        :param source: start vertex
        :param target: final vertex
        :return: distance and path
        """
        if source != self.__bfs_source:
            raise ChildProcessError("Must run BFS with same source!")

        shortest_path = []
        node = self.__bfs_nodes[target]
        while node.predecessor is not None:
            shortest_path.append(node.key)
            node = node.predecessor
        shortest_path.append(node.key)

        shortest_path.reverse()
        return self.__bfs_nodes[target].distance, shortest_path

def main():
    my_graph = AdjListGraph()

    # Add vertices
    my_graph.add_vertice("A")
    my_graph.add_vertice("B")
    my_graph.add_vertice("C")
    my_graph.add_vertice("D")
    my_graph.add_vertice("E")

    # Add edges
    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "D")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "E")
    my_graph.add_edge("D", "C")
    my_graph.add_edge("E", "A")

    bfs = BFS(my_graph)
    bfs_result = bfs.run("A")

    for vertex in bfs_result:
        print(f"Distance from 'A' to '{vertex}': {bfs.get_shortest_path('A', vertex)}")

if __name__ == "__main__":
    main()