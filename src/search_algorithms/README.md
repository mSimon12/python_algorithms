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

# Graph Search

Graph Search algorithms present multiple benefits, since they can be very easily
modified to fit the problem in question. Some example applications are:
- Verify which nodes are reachable.
- Verify node existence in the graph.
- Find a path or the smallest one between 2 nodes.
- Count the amount of direct or undirected connections.
- Identify possible infinite cycles.

## BFS - Breadth-First Search
Breadth-ﬁrst search is so named because it expands the frontier between discovered 
and undiscovered vertices uniformly across the breadth of the frontier. That is, 
the algorithm discovers all vertices at distance k from s before discovering any 
vertices at distance k+1.

## DFS - Depth-First Search
Depth-ﬁrst search explores edges out of the most recently discovered vertex v that 
still has unexplored edges leaving it. Once all of v’s edges have been explored, 
the search “backtracks” to explore edges leaving the vertex from which v was 
discovered.


```python
from src.data_structures.graphs import AdjListGraph
from src.search_algorithms.graphs_search import BFS, DFS

my_graph = AdjListGraph()

# Add vertices
my_graph.add_vertice("A")
my_graph.add_vertice("B")
my_graph.add_vertice("C")
my_graph.add_vertice("D")
my_graph.add_vertice("E")
my_graph.add_vertice("F")

# Add edges
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "E")
my_graph.add_edge("D", "C")
my_graph.add_edge("E", "A")
my_graph.add_edge("F", "A")
my_graph.add_edge("F", "E")

bfs = BFS(my_graph)
bfs_result = bfs.run("F")

for vertex in bfs_result:
    print(f"Distance from 'F' to '{vertex}': {bfs.get_shortest_path('F', vertex)}")

dfs = DFS(my_graph)
dfs_result = dfs.run("F")

for vertex in dfs_result:
    print(f"Start from '{vertex}': {dfs_result[vertex].distance}")
    print(f"End from '{vertex}': {dfs_result[vertex].finish}")
```


