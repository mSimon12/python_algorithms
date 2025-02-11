import pytest
from src.data_structures.graphs import AdjListGraph
from src.search_algorithms.graphs_search import BFS, DFS

class TestBFS:
    # Sample graph (directed graph)
    #
    #            --> A ---
    #            |       |
    #           \|/     \|/
    #            B <---- C ---> D ---> E
    #           /|\             |
    #            ----------------

    @pytest.fixture()
    def sample_graph(self):
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

    @pytest.fixture()
    def bfs_under_test(self, sample_graph):
        return BFS(sample_graph)

    @pytest.fixture()
    def dfs_under_test(self, sample_graph):
        return DFS(sample_graph)

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

    def test_dfs_invalid_source_exception(self, dfs_under_test):
        with pytest.raises(KeyError, match='Source node not in Graph!'):
            dfs_under_test.run("F")

    def test_dfs_from_valid_nodes(self, dfs_under_test):
        dfs_under_test.run("A")
        dfs_under_test.run("B")
        dfs_under_test.run("C")
        dfs_under_test.run("D")
        dfs_under_test.run("E")