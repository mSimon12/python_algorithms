import pytest
from src.data_structures.graphs import AdjListGraph, AdjMatrixGraph

class TestAdjListGraph:
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

    def test_insert_duplicate_vertice_exception(self, graph_empty_adj_list):
        vertice = "A"
        graph_empty_adj_list.add_vertice(vertice)
        with pytest.raises(KeyError, match="Vertice already in Graph!"):
            graph_empty_adj_list.add_vertice(vertice)

    def test_insert_vertice(self, graph_empty_adj_list):
        vertice = "A"
        graph_empty_adj_list.add_vertice(vertice)
        assert vertice in graph_empty_adj_list.get_graph().keys(), "Fail to add vertice in Adjacency List!"

    def test_insert_edge_to_invalid_vertice_exception(self, graph_empty_adj_list):
        edge = ["A", "B"]   # A --> B

        with pytest.raises(KeyError, match="Invalid source_key!"):
            graph_empty_adj_list.add_edge(edge[0], edge[1])

        graph_empty_adj_list.add_vertice(edge[0])

        with pytest.raises(KeyError, match="Invalid dest_key!"):
            graph_empty_adj_list.add_edge(edge[0], edge[1])

    def test_insert_edge(self, graph_empty_adj_list):
        edge = ["A", "B"]   # A --> B

        graph_empty_adj_list.add_vertice(edge[0])
        graph_empty_adj_list.add_vertice(edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])

        vertice_neighbors = graph_empty_adj_list.get_graph()[edge[0]]
        assert edge[1] in vertice_neighbors, "Fail to add edges in Adjacency List!"

    def test_insert_duplicate_edge(self, graph_empty_adj_list):
        edge = ["A", "B"]  # A --> B

        graph_empty_adj_list.add_vertice(edge[0])
        graph_empty_adj_list.add_vertice(edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])
        graph_empty_adj_list.add_edge(edge[0], edge[1])

        vertice_neighbors = graph_empty_adj_list.get_graph()[edge[0]]
        assert edge[1] in vertice_neighbors, "Fail to add edges in Adjacency List!"

    def test_delete_vertice(self, graph_complete_adj_list):
        vertice = "B"

        graph_complete_adj_list.delete_vertice(vertice)

        graph_after_delete = graph_complete_adj_list.get_graph()
        assert vertice not in graph_after_delete.keys(), "Fail to remove vertice from Adjacency List!"
        for remaining_vertice_edges in graph_after_delete.values():
            assert vertice not in remaining_vertice_edges, "Fail to remove vertice from Adjacency List edges!"

    def test_delete_edge(self, graph_complete_adj_list):
        edge = ["A", "B"]

        graph_complete_adj_list.delete_edge(edge[0], edge[1])

        graph_after_delete = graph_complete_adj_list.get_graph()
        assert edge[1] not in graph_after_delete[edge[0]], "Fail to remove edge from Adjacency List!"

    def test_complete_graph_to_sample(self, graph_complete_adj_list, adj_list_sample):
        assert adj_list_sample == graph_complete_adj_list.get_graph(), "Fail to build Adjacency List for sample Graph!"


class TestAdjMatrixGraph:
    # Test graph (directed graph)
    #
    #            --> A ---
    #            |       |
    #           \|/     \|/
    #            B <---- C ---> D ---> E
    #           /|\             |
    #            ----------------

    @pytest.fixture()
    def adj_matrix_sample(self):
        graph = [[0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]]
        return graph

    @pytest.fixture()
    def graph_empty_adj_matrix(self):
        return AdjMatrixGraph()

    @pytest.fixture()
    def graph_complete_adj_matrix(self, adj_matrix_sample):
        graph_keys = ["A", "B", "C", "D", "E"]

        adj_matrix = AdjMatrixGraph()
        for vertice in graph_keys:
            adj_matrix.add_vertice(vertice)

        for row in range(len(adj_matrix_sample)):
            for col in range(len(adj_matrix_sample)):
                if adj_matrix_sample[row][col] == 1:
                    adj_matrix.add_edge(graph_keys[row], graph_keys[col])

        return adj_matrix

    def test_insert_duplicate_vertice_exception(self, graph_empty_adj_matrix):
        vertice = "A"
        graph_empty_adj_matrix.add_vertice(vertice)
        with pytest.raises(KeyError, match="Vertice already in Graph!"):
            graph_empty_adj_matrix.add_vertice(vertice)

    def test_insert_vertice(self, graph_empty_adj_matrix):
        vertices = ["A", "B"]

        graph_empty_adj_matrix.add_vertice(vertices[0])
        matrix_graph = graph_empty_adj_matrix.get_graph()
        assert 1 ==len(matrix_graph), "Fail to add vertice in Adjacency Matrix!"
        assert [0] == matrix_graph[0], "Fail to add vertice in Adjacency Matrix!"

        graph_empty_adj_matrix.add_vertice(vertices[1])
        matrix_graph = graph_empty_adj_matrix.get_graph()
        assert 2 == len(matrix_graph), "Fail to add vertice in Adjacency Matrix!"
        assert [0, 0] == matrix_graph[0], "Fail to add vertice in Adjacency Matrix!"
        assert [0, 0] == matrix_graph[1], "Fail to add vertice in Adjacency Matrix!"

    def test_insert_edge_to_invalid_vertice_exception(self, graph_empty_adj_matrix):
        edge = ["A", "B"]   # A --> B

        with pytest.raises(KeyError, match="Invalid source_key!"):
            graph_empty_adj_matrix.add_edge(edge[0], edge[1])

        graph_empty_adj_matrix.add_vertice(edge[0])

        with pytest.raises(KeyError, match="Invalid dest_key!"):
            graph_empty_adj_matrix.add_edge(edge[0], edge[1])

    def test_insert_edge(self, graph_empty_adj_matrix):
        edge = ["A", "B"]   # A --> B

        graph_empty_adj_matrix.add_vertice(edge[0])
        graph_empty_adj_matrix.add_vertice(edge[1])
        graph_empty_adj_matrix.add_edge(edge[0], edge[1])

        matrix_graph = graph_empty_adj_matrix.get_graph()
        assert [0, 1] == matrix_graph[0], "Fail to add edges in Adjacency Matrix!"
        assert [0, 0] == matrix_graph[1], "Fail to add edges in Adjacency Matrix!"

    def test_insert_duplicate_edge(self, graph_empty_adj_matrix):
        edge = ["A", "B"]   # A --> B

        graph_empty_adj_matrix.add_vertice(edge[0])
        graph_empty_adj_matrix.add_vertice(edge[1])
        graph_empty_adj_matrix.add_edge(edge[0], edge[1])
        graph_empty_adj_matrix.add_edge(edge[0], edge[1])

        matrix_graph = graph_empty_adj_matrix.get_graph()
        assert [0, 1] == matrix_graph[0], "Fail to add edges in Adjacency Matrix!"
        assert [0, 0] == matrix_graph[1], "Fail to add edges in Adjacency Matrix!"

    def test_delete_vertice(self, graph_complete_adj_matrix):
        vertice = "B"

        graph_before_delete = graph_complete_adj_matrix.get_graph()
        graph_complete_adj_matrix.delete_vertice(vertice)
        graph_after_delete = graph_complete_adj_matrix.get_graph()

        key_map = graph_complete_adj_matrix.get_key_idx_map()
        assert vertice not in key_map.keys(), "Fail to remove vertice from Adjacency Matrix key map!"
        assert len(graph_before_delete) - 1 == len(graph_after_delete), "Fail to remove vertice from Adjacency Matrix!"
        assert len(graph_before_delete[0]) - 1 == len(graph_after_delete[0]), "Fail to remove vertice from Adjacency Matrix!"

    def test_delete_edge(self, graph_complete_adj_matrix):
        edge = ["A", "B"]

        graph_complete_adj_matrix.delete_edge(edge[0], edge[1])

        graph_after_delete = graph_complete_adj_matrix.get_graph()
        key_map = graph_complete_adj_matrix.get_key_idx_map()
        source = key_map[edge[0]]
        dest = key_map[edge[1]]
        assert 0 == graph_after_delete[source][dest], "Fail to remove edge from Adjacency Matrix!"

    def test_complete_graph_to_sample(self, graph_complete_adj_matrix, adj_matrix_sample):
        assert adj_matrix_sample == graph_complete_adj_matrix.get_graph(), "Fail to build Adjacency Matrix for sample Graph!"