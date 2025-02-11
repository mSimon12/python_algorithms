import abc
import copy


class GraphInterface(metaclass=abc.ABCMeta):
    _graph = None

    @classmethod
    def __subclasshook__(cls, __subclass):
        return (hasattr(__subclass, '_graph') and
                hasattr(__subclass, 'add_vertice') and
                callable(__subclass.add_vertice) and
                hasattr(__subclass, 'delete_vertice') and
                callable(__subclass.delete_vertice)and
                hasattr(__subclass, 'add_edge') and
                callable(__subclass.add_edge) and
                hasattr(__subclass, 'delete_edge') and
                callable(__subclass.delete_edge) and
                hasattr(__subclass, 'get_graph') and
                callable(__subclass.get_graph) or
                NotImplemented)

    @abc.abstractmethod
    def add_vertice(self, vertice_key):
        """
            Include a new vertice to the graph
        :param vertice_key: key to associate to this vertice
        :return: None
        """
        pass

    @abc.abstractmethod
    def delete_vertice(self, deleted_vertice_key):
        """
            Delete vertice from the graph
        :param deleted_vertice_key: key associated to the vertice to be deleted
        :return: None
        """
        pass

    @abc.abstractmethod
    def add_edge(self, source_key, dest_key):
        """
            Include a new edge between source and destination nodes
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        pass

    @abc.abstractmethod
    def delete_edge(self, source_key, dest_key):
        """
            Delete a new edge between source and destination nodes
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        pass

    def get_graph(self):
        """
            Return the graph structure
        :return: graph
        """
        return copy.deepcopy(self._graph)


    def __str__(self):
        return f"{self._graph}"


class AdjListGraph(GraphInterface):

    def __init__(self):
        self._graph = {}

    def add_vertice(self, vertice_key):
        """
            Include a new vertice to the graph
        :param vertice_key: key to associate to this vertice
        :return: None
        """
        if vertice_key in self._graph.keys():
            raise KeyError("Vertice already in Graph!")

        self._graph[vertice_key] = set()

    def delete_vertice(self, deleted_vertice_key):
        """
            Delete vertice from the graph
        :param deleted_vertice_key: key associated to the vertice to be deleted
        :return: None
        """
        for v_key in self._graph.keys():
            self._graph[v_key].discard(deleted_vertice_key)

        self._graph.pop(deleted_vertice_key)

    def add_edge(self, source_key, dest_key):
        """
            Include a new edge between source and destination nodes
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        if source_key not in self._graph.keys():
            raise KeyError("Invalid source_key!")
        elif dest_key not in self._graph.keys():
            raise KeyError("Invalid dest_key!")

        self._graph[source_key].add(dest_key)

    def delete_edge(self, source_key, dest_key):
        """
            Delete a new edge between source and destination nodes
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        self._graph[source_key].discard(dest_key)


class AdjMatrixGraph(GraphInterface):

    def __init__(self):
        self._graph = []
        self._key_map = []

    def add_vertice(self, vertice_key):
        """
            Include a new vertice to the graph
        :param vertice_key: key to associate to this vertice
        :return: None
        """
        if vertice_key in self._key_map:
            raise KeyError("Vertice already in Graph!")

        self._key_map.append(vertice_key)

        new_vertice_edges = [0] * (len(self._graph))
        self._graph.append(new_vertice_edges)

        for vertice in self._graph:
            vertice.append(0)

    def delete_vertice(self, deleted_vertice_key):
        """
            Delete vertice from the graph
        :param deleted_vertice_key: key associated to the vertice to be deleted
        :return: None
        """
        vertice_idx = self._key_map.index(deleted_vertice_key)

        for graph_rows in self._graph:
            graph_rows.pop(vertice_idx)

        self._graph.pop(vertice_idx)
        self._key_map.remove(deleted_vertice_key)

    def add_edge(self, source_key, dest_key, weight=1):
        """
            Include a new edge between source and destination nodes
        :param weight: the cost/weight from this edge
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        if source_key not in self._key_map:
            raise KeyError("Invalid source_key!")
        elif dest_key not in self._key_map:
            raise KeyError("Invalid dest_key!")

        source_idx = self._key_map.index(source_key)
        dest_idx = self._key_map.index(dest_key)

        self._graph[source_idx][dest_idx] = weight

    def delete_edge(self, source_key, dest_key):
        """
            Delete a new edge between source and destination nodes
        :param source_key: key associated with the source node
        :param dest_key: key associated with the destination node
        :return: None
        """
        source_idx = self._key_map.index(source_key)
        dest_key = self._key_map.index(dest_key)

        self._graph[source_idx][dest_key] = 0

    def get_key_idx_map(self):
        """
            Create a mapping from key name to index in the Adjacency Matrix
        :return: key to idx map
        """
        key_to_idx = {}
        idx = 0
        for key in self._key_map:
            key_to_idx[key] = idx
            idx += 1

        return key_to_idx


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
