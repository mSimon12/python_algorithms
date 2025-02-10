# Item Search

## Linear Search

```python
from src.search_algorithms.search import LinearSearch

data = [10, -50, 96, 23, 1069]
interest_value = 23

my_searcher = LinearSearch()

value_idx = my_searcher.search(data, interest_value)

if value_idx is not None:
    print(f"The value '{interest_value} is at index {value_idx}")
else:
    print("The searched value is not in the list!")
```

## Binary Search

```python
from src.search_algorithms.search import BinarySearch

data = [10, -50, 96, 23, 1069]
interest_value = 23

my_searcher = BinarySearch()

value_idx = my_searcher.search(data, interest_value)

if value_idx is not None:
    print(f"The value '{interest_value} is at index {value_idx}")
else:
    print("The searched value is not in the list!")
```

# Shortest Path

## BFS - Breadth-First Search

```python
from src.data_structures.graphs import AdjListGraph
from src.search_algorithms.graphs_search import BFS

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
```

