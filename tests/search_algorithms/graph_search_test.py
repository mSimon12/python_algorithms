import pytest
from src.data_structures.graphs import AdjListGraph, AdjMatrixGraph
from src.search_algorithms.graphs_search import BFS, DFS, Dijkstra

@pytest.fixture()
def sample_graph():
    # Sample graph (directed graph)
    #
    #            --> A ---
    #            |       |
    #           \|/     \|/
    #            B <---- C ---> D ---> E
    #           /|\             |
    #            ----------------
    adj_list = AdjListGraph()

    # Add vertices
    adj_list.add_vertice("A")
    adj_list.add_vertice("B")
    adj_list.add_vertice("C")
    adj_list.add_vertice("D")
    adj_list.add_vertice("E")

    # Add edges
    adj_list.add_edge("A", "B")
    adj_list.add_edge("A", "C")
    adj_list.add_edge("B", "A")
    adj_list.add_edge("C", "B")
    adj_list.add_edge("C", "D")
    adj_list.add_edge("D", "B")
    adj_list.add_edge("D", "E")

    return adj_list


class TestBFS:

    @pytest.fixture()
    def bfs_under_test(self, sample_graph):
        return BFS(sample_graph)

    def test_bfs_invalid_source_exception(self, bfs_under_test):
        with pytest.raises(KeyError, match='Source node not in Graph!'):
            bfs_under_test.run("F")

    def test_bfs_from_valid_nodes(self, bfs_under_test):
        bfs_under_test.run("A")
        bfs_under_test.run("B")
        bfs_under_test.run("C")
        bfs_under_test.run("D")
        bfs_under_test.run("E")

    def test_bfs_get_shortest_path_from_non_processed_source(self, bfs_under_test):
        with pytest.raises(ChildProcessError, match="Must run BFS with same source!"):
            bfs_under_test.get_shortest_path("A", "B")

    def test_bfs_get_shortest_paths(self, bfs_under_test):
        bfs_under_test.run("A")

        distance, path = bfs_under_test.get_shortest_path("A", "C")
        assert 1 == distance, "Fail to process shortest path!"
        assert ["A", "C"] == path, "Fail to process shortest path!"

        distance, path = bfs_under_test.get_shortest_path("A", "D")
        assert 2 == distance, "Fail to process shortest path!"
        assert ["A", "C", "D"] == path, "Fail to process shortest path!"

        distance, path = bfs_under_test.get_shortest_path("A", "E")
        assert 3 == distance, "Fail to process shortest path!"
        assert ["A", "C", "D", "E"] == path, "Fail to process shortest path!"


class TestDFS:

    @pytest.fixture()
    def dfs_under_test(self, sample_graph):
        return DFS(sample_graph)

    def test_dfs_invalid_source_exception(self, dfs_under_test):
        with pytest.raises(KeyError, match='Source node not in Graph!'):
            dfs_under_test.run("F")

    def test_dfs_from_valid_nodes(self, dfs_under_test):
        dfs_under_test.run("A")
        dfs_under_test.run("B")
        dfs_under_test.run("C")
        dfs_under_test.run("D")
        dfs_under_test.run("E")

    def test_dfs_get_topological_sort_without_run(self, dfs_under_test):
        with pytest.raises(ChildProcessError, match="Must run DFS before requesting topological sort!"):
            dfs_under_test.get_topological_sort()

class TestDijkstra:

    @pytest.fixture()
    def weighted_graph_sample(self):
        matrix_graph = AdjMatrixGraph()

        vertices = ["A", "B", "C", "D", "E"]
        for vertex in vertices:
            matrix_graph.add_vertice(vertex)

        # Tasks dependencies
        matrix_graph.add_edge("A", "B", 5)
        matrix_graph.add_edge("A", "C", 10)
        matrix_graph.add_edge("B", "C", 3)
        matrix_graph.add_edge("B", "D", 9)
        matrix_graph.add_edge("B", "E", 2)
        matrix_graph.add_edge("C", "B", 2)
        matrix_graph.add_edge("C", "D", 1)
        matrix_graph.add_edge("D", "E", 4)
        matrix_graph.add_edge("E", "A", 7)
        matrix_graph.add_edge("E", "D", 6)

        return matrix_graph

    @pytest.fixture()
    def dijkstra_under_test(self, weighted_graph_sample):
        return Dijkstra(weighted_graph_sample)

    def test_dijkstra_invalid_source_exception(self, dijkstra_under_test):
        with pytest.raises(KeyError, match='Source node not in Graph!'):
            dijkstra_under_test.run("F")

    def test_dijkstra_from_valid_nodes(self, dijkstra_under_test):
        dijkstra_under_test.run("A")
        dijkstra_under_test.run("B")
        dijkstra_under_test.run("C")
        dijkstra_under_test.run("D")
        dijkstra_under_test.run("E")

    def test_dijkstra_shortest_distances(self, dijkstra_under_test):
        djk_result = dijkstra_under_test.run("A")

        assert 0 == djk_result["A"].distance, "Fail to process shortest path!"
        assert 5 == djk_result["B"].distance, "Fail to process shortest path!"
        assert 8 == djk_result["C"].distance, "Fail to process shortest path!"
        assert 9 == djk_result["D"].distance, "Fail to process shortest path!"
        assert 7 == djk_result["E"].distance, "Fail to process shortest path!"