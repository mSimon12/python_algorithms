import math

from src.data_structures.graphs import AdjListGraph, AdjMatrixGraph
from src.data_structures.basic_data_structures import Queue


class SearchNode:
    def __init__(self, node_key):
        self.key = node_key
        self.predecessor = None
        self.visited = False
        self.distance = math.inf
        self.finish = 0


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
            self.__bfs_nodes[vertex] = SearchNode(vertex)

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

class DFS:
    """
        Depth-First Search class to provide graph topological sort
    """
    def __init__(self, graph:AdjListGraph):
        self.__graph = graph.get_graph()
        self.__dfs_nodes = {}
        self.__time = 0

    def __initialize_nodes(self):
        """
            Initialize the nodes for each vertex from the graph
        :return: None
        """
        graph_vertices = self.__graph.keys()

        for vertex in graph_vertices:
            self.__dfs_nodes[vertex] = SearchNode(vertex)

    def __dfs_visit(self, node_key):
        """
            Implements recursive search going deeper as possible
        :param node_key: current node being explored in the graph
        :return: None
        """
        self.__time += 1
        node = self.__dfs_nodes[node_key]
        node.distance = self.__time
        node.visited = True

        for neighbor_key in self.__graph[node_key]:
            neighbor_node = self.__dfs_nodes[neighbor_key]
            if not neighbor_node.visited:
                neighbor_node.predecessor = node
                self.__dfs_visit(neighbor_key)

        self.__time += 1
        node.finish = self.__time

    def run(self, search_source):
        """
            Execute the DFS search
        :param search_source: start point for doing the search for other vertices from graph
        :return: Dictionary with nodes from the graph
        """
        self.__initialize_nodes()

        if search_source not in self.__dfs_nodes.keys():
            raise KeyError("Source node not in Graph!")

        self.__time = 0
        next_node = search_source
        nodes_to_visit = [node.key for node in self.__dfs_nodes.values() if not node.visited]

        while nodes_to_visit:
            if not self.__dfs_nodes[next_node].visited:
                self.__dfs_visit(next_node)

            nodes_to_visit = [node.key for node in self.__dfs_nodes.values() if not node.visited]
            if nodes_to_visit:
                next_node = nodes_to_visit[0]

        return self.__dfs_nodes

    def get_topological_sort(self):
        """
            Perform Topological Sorting using DFS
        :return: None
        """

        if not self.__dfs_nodes:
            raise ChildProcessError("Must run DFS before requesting topological sort!")

        # Sort nodes in descending order of finish time
        sorted_tasks = sorted(self.__dfs_nodes.values(), key=lambda node: node.finish, reverse=True)
        execution_order = [node.key for node in sorted_tasks]

        return execution_order

class Dijkstra:
    """
        Implementation of Dijkstra algorithm
    """
    def __init__(self, graph:AdjMatrixGraph):
        self.__graph = graph.get_graph()
        self.__nodes = {}
        self.__graph_key_map = graph.get_key_idx_map()

    def __initialize_nodes(self):
        """
            Initialize the nodes for each vertex from the graph
        :return: None
        """
        graph_vertices = self.__graph_key_map.keys()

        for vertex in graph_vertices:
            self.__nodes[vertex] = SearchNode(vertex)

    @staticmethod
    def __relax(source_node, target_node, weight):
        """
            Executed node relaxation - verifies if distance can be reduced via another path
        :param source_node: possible new path to the target
        :param target_node: node having the distance checked
        :param weight: weight to move from source_node to target_node
        :return: None
        """
        if target_node.distance > source_node.distance + weight:
            target_node.distance = source_node.distance + weight
            target_node.predecessor = source_node

    def run(self, path_source):
        """
            Executes the Dijkstra algorithm to get the shortest paths starting from path_source
        :param path_source: start point for doing the search for other vertices from graph
        :return: Dictionary with nodes from the graph
        """
        self.__initialize_nodes()

        if path_source not in self.__nodes.keys():
            raise KeyError("Source node not in Graph!")

        source_node = self.__nodes[path_source]
        source_node.distance = 0

        processed_nodes = []
        nodes_to_be_processed = list(self.__nodes.values())

        while nodes_to_be_processed:
            nodes_to_be_processed.sort(key=lambda node: node.distance, reverse=True)
            current_vertex = nodes_to_be_processed.pop()

            current_vertex_idx = self.__graph_key_map[current_vertex.key]
            processed_nodes.append(current_vertex)

            neighbor_idx = 0
            for weight in self.__graph[current_vertex_idx]:
                if weight > 0:
                    neighbor_key = list(self.__graph_key_map.keys())[neighbor_idx]
                    neighbor_node = self.__nodes[neighbor_key]
                    self.__relax(current_vertex, neighbor_node, weight)
                neighbor_idx += 1

        return self.__nodes
