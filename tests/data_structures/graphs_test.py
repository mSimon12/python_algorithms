import pytest
from pandas.core.computation.expressions import get_test_result

from src.data_structures.graphs import AdjListGraph, AdjMatrixGraph

class TestBinaryTree:
    # Test graph (directed graph)
    #
    #            --> A ---
    #            |       |
    #           \|/     \|/
    #            B <---- C ---> D ---> E
    #           /|\             |
    #            ----------------

    @pytest.fixture()
    def adj_list_sample(self):
        graph = {
            "A": {"B", "C"},
            "B": {"A"},
            "C": {"B"},
            "D": {"B", "E"},
            "E": set()
        }
        return graph

    @pytest.fixture()
    def adj_matrix_sample(self):
        graph = [[0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]]
        return graph

    @pytest.fixture()
    def graph_empty_adj_list(self):
        return AdjListGraph()

    @pytest.fixture()
    def graph_complete_adj_list(self, adj_list_sample):
        adj_list = AdjListGraph()
        for vertice in adj_list_sample.keys():
            adj_list.add_vertice(vertice)

        for vertice in adj_list_sample.keys():
            for neighbor in adj_list_sample[vertice]:
                adj_list.add_edge(vertice, neighbor)

        return adj_list

    @pytest.fixture()
    def graph_empty_adj_matrix(self):
        return AdjMatrixGraph()

    def test_adj_list_graph_insert_vertice(self, graph_empty_adj_list):
        vertice = "A"
        graph_empty_adj_list.add_vertice(vertice)
        assert vertice in graph_empty_adj_list.get_graph().keys(), "Fail to add vertice in Adjacency List!"

    def test_adj_list_graph_insert_duplicate_vertice_exception(self, graph_empty_adj_list):
        vertice = "A"
        graph_empty_adj_list.add_vertice(vertice)
        with pytest.raises(KeyError, match="Vertice already in Graph!"):
            graph_empty_adj_list.add_vertice(vertice)

    def test_adj_list_graph_insert_edge(self, graph_empty_adj_list):
        edge = ["A", "B"]   # A --> B

        graph_empty_adj_list.add_vertice(edge[0])
        graph_empty_adj_list.add_vertice(edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])

        vertice_neighbors = graph_empty_adj_list.get_graph()[edge[0]]
        assert edge[1] in vertice_neighbors, "Fail to add edges in Adjacency List!"

    def test_adj_list_graph_insert_edge_to_invalid_vertice(self, graph_empty_adj_list):
        edge = ["A", "B"]   # A --> B

        with pytest.raises(KeyError, match="Invalid source_key!"):
            graph_empty_adj_list.add_edge(edge[0], edge[1])

        graph_empty_adj_list.add_vertice(edge[0])

        with pytest.raises(KeyError, match="Invalid dest_key!"):
            graph_empty_adj_list.add_edge(edge[0], edge[1])

    def test_adj_list_graph_insert_duplicate_edge(self, graph_empty_adj_list):
        edge = ["A", "B"]  # A --> B

        graph_empty_adj_list.add_vertice(edge[0])
        graph_empty_adj_list.add_vertice(edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])

        vertice_neighbors = graph_empty_adj_list.get_graph()[edge[0]]
        assert edge[1] in vertice_neighbors, "Fail to add edges in Adjacency List!"

    def test_adj_list_graph_delete_vertice(self, graph_complete_adj_list):
        vertice = "B"

        graph_complete_adj_list.delete_vertice(vertice)

        graph_after_delete = graph_complete_adj_list.get_graph()
        assert vertice not in graph_after_delete.keys(), "Fail to remove vertice from Adjacency List!"
        for remaining_vertice_edges in graph_after_delete.values():
            assert vertice not in remaining_vertice_edges, "Fail to remove vertice from Adjacency List edges!"

    def test_adj_list_graph_delete_edge(self, graph_complete_adj_list):
        edge = ["A", "B"]

        graph_complete_adj_list.delete_edge(edge[0], edge[1])

        graph_after_delete = graph_complete_adj_list.get_graph()
        assert edge[1] not in graph_after_delete[edge[0]], "Fail to remove edge from Adjacency List!"

    def test_adj_matrix_graph_insert(self, graph_empty_adj_matrix):
        pass


